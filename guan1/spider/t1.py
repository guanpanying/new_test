from urllib.request import urlopen, Request
from http.client import HTTPResponse
from selenium_js.base import Base1

url = 'http://cn.bing.com/'

response = urlopen(url=url)

with response:
    print(type(response))
    # print(response.status)      #200
    # print(response.info())    #headers
    # print(response.geturl()) #http://cn.bing.com/
    # print(response._method)    #GET
    # print(response.read())
print(response.closed)


class Ab:
    def a1(self):
        print(123)


print(type(Ab))
print(Base1)
