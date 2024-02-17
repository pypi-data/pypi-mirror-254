import sys
import json
from marko.ext.gfm import gfm as markdown
import collections
from cerberus import Validator, DocumentError

from watchtower_browser_testing import exceptions


def trim(docstring):
    if not docstring:
        return ''
    # Convert tabs to spaces (following the normal Python rules)
    # and split into a list of lines:
    lines = docstring.expandtabs().splitlines()
    # Determine minimum indentation (first line doesn't count):
    indent = sys.maxsize
    for line in lines[1:]:
        stripped = line.lstrip()
        if stripped:
            indent = min(indent, len(line) - len(stripped))
    # Remove indentation (first line is special):
    trimmed = [lines[0].strip()]
    if indent < sys.maxsize:
        for line in lines[1:]:
            trimmed.append(line[indent:].rstrip())
    # Strip off trailing and leading blank lines:
    while trimmed and not trimmed[-1]:
        trimmed.pop()
    while trimmed and not trimmed[0]:
        trimmed.pop(0)
    # Return a single string:
    return '\n'.join(trimmed)


def build_html(structure):

    html = f'<div class="{structure["type"]}" id="{structure["id"]}">'
    html += markdown.render(structure.get('description') or '')
    if 'children' in structure and structure['children']:
        for child_structure in structure['children']:
            html += build_html(child_structure)
    html += '</div>'
    return html


class ExtendedEncoder(json.JSONEncoder):

    def default(self, obj):
        if callable(obj):
            return obj.__name__
        return super().default(obj)

class Storage(collections.UserDict):

    def get(self, key, default=None):

        value = super().get(key, default)

        if value is None:
            value = self.key_name_string(key)

        return value

    @staticmethod
    def key_name_string(key):
        return f'<{key}>'

class WtValidator(Validator):

    rows_key = '__rows'

    def __init__(self,
                 *args,
                 **kwargs):

        self.is_dict_list = kwargs.pop('is_dict_list', False)
        super(WtValidator, self).__init__(*args, **kwargs)

    def validate(
            self,
            document,
            *args,
            **kwargs):

        schema = kwargs.get('schema') or self.schema

        if self.is_dict_list:
            if self.rows_key not in schema:
                schema = {
                    self.rows_key: {
                        'type': 'list',
                        'required': True,
                        'schema': {
                            'type': 'dict',
                            'schema': schema
                        }
                    }
                }
                kwargs['schema'] = schema

            if self.rows_key not in document:
                document = {self.rows_key: document}

        return super(WtValidator, self).validate(document, *args, **kwargs)

    @property
    def errors(self):
        errors = super(WtValidator, self).errors
        if self.is_dict_list and self.rows_key in errors:
            return errors[self.rows_key]
        else:
            return errors

class CombinedSelector(object):

    def __init__(self, selectors, operator='and'):

        self.selectors = selectors
        self.operator = operator

    def __and__(self, other):

        return CombinedSelector(selectors=[self, other], operator='and')

    def __or__(self, other):

        return CombinedSelector(selectors=[self, other], operator='or')

    def select(self, document):

        if self.operator == 'and':
            return all(s.select(document) for s in self.selectors)
        elif self.operator == 'or':
            return any(s.select(document) for s in self.selectors)
        else:
            raise exceptions.InvalidInputError(f'Unknown operator {self.operator}')

class WtSelector(object):

    def __and__(self, other):
        return CombinedSelector(selectors=[self, other], operator='and')

    def __or__(self, other):
        return CombinedSelector(selectors=[self, other], operator='or')

class Selector(WtSelector, WtValidator):

    def select(self, document):

        try:
            return super(WtSelector, self).validate(document=document)
        except DocumentError:
            return False

class ExactMatchSelector(WtSelector):

    def __init__(self, value, inverse=False):

        self.value = value
        self.inverse = inverse

    def select(self, document):

        if self.inverse:
            return not (document is self.value)

        return document is self.value

class MissingSelector(ExactMatchSelector):

    def __init__(self, inverse=False):
        super(MissingSelector, self).__init__(value=None, inverse=inverse)
