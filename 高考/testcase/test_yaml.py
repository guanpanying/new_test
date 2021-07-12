import yaml


def test_a():
    with open('./a.yml',"r") as f:
        a = yaml.safe_load(f)
        print(a)

        # print(a["hb"]["provinceId"])
        # print(a["hb"]["maxMin"])
        # print(a["hb"]["score"])
        # print(a["hb"]["score"][1][0])
        # # for i in a["hb"]["maxMin"]:


        for i in range(len(a)):
            print(a[i]["name"])




def test_b():
    a=[1,2,3]
    print(len(a))
    for i in range(len(a)):
        print(a[i])


def test_byml():
    with open('./b.yml',"r") as f:
        a = yaml.safe_load(f)
        print(a)

        # print(a["hb"]["provinceId"])
        # print(a["hb"]["maxMin"])
        # print(a["hb"]["score"])
        # print(a["hb"]["score"][1][0])
        # # for i in a["hb"]["maxMin"]:


        for i in range(len(a)):
            print(a[i]["provinceId"])