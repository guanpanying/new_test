# print(type('string'.encode()),'string'.encode())
# print(type('string'.encode('utf-8')),'string'.encode('utf-8'))

from urllib.request import Request, urlopen
from urllib.parse import urlencode
import json
import ssl

context = ssl._create_unverified_context()

ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'

d = {'type': 'movie',
     'tag': '热门',
     'page_limit': 10,
     'page_start': 0}

base_url = f'https://movie.douban.com/j/search_subjects?{urlencode(d)}'
print(base_url)

req = Request(base_url, headers={'User-agent': ua})

res = urlopen(req, context=context)

with res:
    a = json.loads(res.read().decode())
    print(len(a['subjects']))
    print(a['subjects'])
    # print(res.read().decode())
