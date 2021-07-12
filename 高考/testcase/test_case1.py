import requests


url = 'https://gaokaotest.qknode.com/gaokao/user/v1/saveUser'
header = {
    "Content-Type":"application/x-www-form-urlencoded"

}
params = {
    "uuid":"d974b3f4c3a04ee7ba8d43df8906a7e3",
    "nickname":"",
    "type":"1"
}

data={
    "platform":"1",
    "realname":"",
    "gender":"0",
    "isScience":"3",
    "provinceId":provinceid,
    "physicIsSelected":1, #物理
    "chemistryIsSelected":0,#化学
    "biologicalIsSelected":1,#生物
    "politicalIsSelected":political,#政治
    "historyIsSelected":history,
    "geographyIsSelected":geography, #地理
    "modelId":"101",
    "score":score,
    "rank":rank, #排名
    "batch":"本科"
}
r = requests.post(url,headers=header,data=data)