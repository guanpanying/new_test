import json

import yaml
import requests

def test_1():
    a={1:'aaa',2:'bbb'}
    print('-'*30)
    print(yaml.dump(a))

def test_2():

    b=yaml.safe_load(open('aa.yaml'))
    print(b)

def test_3():
    a1={'aa':1,'bb':2}
    print(json.dumps(a1))

def test_4():

    pass