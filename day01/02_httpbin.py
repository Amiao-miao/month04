'''
向测试网站发请求，确认请求头中的User-Agent是什么
养成好习惯，发送请求带User-Agent，这是爬虫和反爬虫斗争的第一步
'''

import requests
url='http://httpbin.org/get'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'}
html=requests.get(url=url,
                  headers=headers).text


print(html)