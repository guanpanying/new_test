import requests


class TestTimeout:
    def test_one(self):
        r = requests.post('https://httpbin.testing-studio.com/post', verify=False
                          )
        print(r.text)

    def test_two(self):
        proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}
        r = requests.post('https://httpbin.testing-studio.com/post', timeout=3, proxies=proxies, verify=False)
        print(r.json())

    def test_three(self):
        r = requests.post('https://httpbin.testing-studio.com/post', verify=False
                          )
        print(r.json())
