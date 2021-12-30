#
# from urllib import parse
#
# d={'wd':'中'}
#
# p=parse.urlencode(d)
# url = f'https://www.baidu.com/s?{p}'
# print(url)
#
#
# print('中'.encode('utf-8'))
#
# print(parse.unquote(p))
# print(11,'中'.encode('utf-8').decode())


from urllib import parse
from urllib.request import Request, urlopen
import ssl

context = ssl._create_unverified_context()

qs = {'wd': '中'}
p = parse.urlencode(qs)
url = f'https://www.baidu.com/s?{p}'
print(url)

req = Request(url=url, headers={"User-agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
                                              'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'})

response = urlopen(req, context=context)

with response:
    with open('./a.html', 'wb+') as f:
        print(type(response.read()))  # <class 'bytes'>
        f.write(response.read())
