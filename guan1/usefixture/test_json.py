import json


def test_js():
    bb = json.load(open('./a.json'))
    print(bb, type(bb))

    print(bb['aa'], type(bb['aa']))
