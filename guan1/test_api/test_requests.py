import requests


def test_get():
    r = requests.get('https://api.github.com/events')
    print(r)
    print(r.json())
    print(r.text)


url = 'http://httpbin.org'


def test_post():
    r = requests.post(url=url + '/post', data={'key': 'value'})
    print(r.json())


def test_head():
    r = requests.head('http://httpbin.org/get')
    print(r.text, type(r.text))


import jsonschema


def test_schema():
    schema = {"type": "object",
              "properties": {
                  "price": {"type": "number"},
                  "name": {"type": "string"},
              }, }
    jsonschema.validate(instance={"name": "Eggs", "price": 34}, schema=schema)
