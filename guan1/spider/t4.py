import urllib3
import requests

urls = 'https://app.yuebuy.net/api/order/goods_loadpage'
data = {'discount_coupon': 1, 'comprehensivz': 0, 'page': 1, 'pagesize': 20, 'id': 259}

'''
id:259是纸尿裤
id:95 玩具
id:'''

res = requests.request('POST', urls, data=data,
                       headers={'User-agent': 'Mozilla/5.0 (Linux; Android 10; TAS-AL00 Build/HUAWEITAS-AL00; wv) '
                                              'AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 Mobile '
                                              'Safari/537.36'})

print(res.text)
