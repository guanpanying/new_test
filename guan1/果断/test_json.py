import json


def test_w_json():
    a = {'a': 1111, 'b': 123}
    # b1=json.dumps(a)
    # print(b1)

    with open('./aaaa.json', 'w') as f:
        # json.dump(a,f)

        json.dumps(a)
    #
    # with open('./aaaa.json') as f:
    #     b=json.load(f)
    #     print(b,type(b),'b')
