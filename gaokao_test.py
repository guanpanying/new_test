import requests

host = 'https://gaokao.qknode.com'
new_provinceId = [48]
sorcelist = [600,300,750]
uuid = "9e03599372a1466ea4b23e373bffb7a9"

def updateReports(provinceId,sorce,uuid):
    #第一步更改个人信息
    url = f'{host}/gaokao/user/v1/saveUser?uuid={uuid}&nickname=&type=1'
    data = {
    "platform":1,
    "realname":"",
    "gender":1,
    "isScience":2,
    "provinceId":provinceId,
    "physicIsSelected":1,
    "chemistryIsSelected":1,
    "biologicalIsSelected":1,
    "politicalIsSelected":0,
    "historyIsSelected":0,
    "geographyIsSelected":0,
    "techniqueIsSelected":0,
    "modelId":101,
    "score":sorce,
    "rank":"",
    "batch":"本科批"
    }
    headers = {"Accept-Token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiI5ZTAzNTk5MzcyYTE0NjZlYTRiMjNlMzczYmZmYjdhOSIsInQiOjE2MjQ2OTg3NTI1MDIsImV4cCI6MTYyNTMwMzU1Mn0.cF8hUZsLC2nVHDJ4HueB9HeYod1DwM1D5Ex3cM9m9oc","Version":"v1.3.7"}
    step1 = requests.post(url=url,data=data,headers=headers)
    #print(step1.json())

    #更新报告
    url = f'{host}/gaokao/report/v1/updateReports?type=1'
    data={"uuid":uuid,"reportType":101}
    step2 = requests.post(url=url,data=data,headers=headers)
    #print(step2.json())

    #查询报告
    url = f'{host}/gaokao/sonReport/v1/getAllUnionRecommend?type=1&cwbType=&uuid={uuid}&srid=65193&batch=%E6%9C%AC%E7%A7%91%E6%89%B9&isProvince=0&provinceId=&level=&campusType=&universityType=&majorLevels=&majorLevels2=&majorLevels3=&pageNo=0&checkType=3'
    step3 = requests.get(url=url,headers=headers)
    try:
        yuanxiao = step3.json()["data"]
        list = yuanxiao["list"]
        n = 5
        if len(list) < n:
            print(f"省份：{provinceId} 分数：{sorce} 推荐数据少")
            print(yuanxiao["list"])
        else:
            print(f"省份：{provinceId} 分数：{sorce} 推荐数据大于{n}条，测试通过")
    except Exception as E:
        print(f"数据异常：{step3.json()}")


for provinceId in new_provinceId:
    for sorce in sorcelist:
        updateReports(provinceId,sorce,uuid)
