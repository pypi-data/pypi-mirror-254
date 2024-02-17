from urllib.parse import urlparse
import json


def path_from_url(url):

    return urlparse(url).path

def authority_from_url(url):

    p = urlparse(url)
    return f'{p.scheme}://{p.netloc}'

def to_pretty_json(value):
    return json.dumps(value, sort_keys=True,
                      indent=4, separators=(',', ': '))