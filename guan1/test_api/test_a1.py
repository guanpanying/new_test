import requests


def test_a1():
    r = requests.get('https://www.baidu.com')
    print(r)
    # print(r.text)
    print(r.json())

    r1 = requests.post()
