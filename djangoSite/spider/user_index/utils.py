
from urllib.parse import urlencode


base_url = 'https://search.bilibili.com/upuser?'


def get_url(name):
    request_args = {
        'keyword': name
    }
    url = base_url + urlencode(request_args)
    return url