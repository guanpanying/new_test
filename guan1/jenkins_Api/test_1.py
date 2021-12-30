import requests


def test_1():
    url = "http://root:root@123.57.221.39:8088/job/first/build"
    res = requests.post(url)
    print(res.text)
