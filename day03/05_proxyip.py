'''
向测试网站发请求，打印响应内容，查看origin对应的IP是什么
'''

import requests
from fake_useragent import UserAgent

url='http://httpbin.org/get'
headers={'User-Agent':UserAgent().random}
proxies={
    'http':'http://115.210.47.85:9999',
    'https':'https://115.210.47.85:9999',
}
html=requests.get(url=url,proxies=proxies,headers=headers).text
print(html)