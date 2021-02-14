'''
向京东官网发请求，拿到响应内容
'''

import requests

# get()方法:获取的是响应对象
# <Response [200]>
resp=requests.get(url='https://www.jd.com/')
print(resp)

# text属性： 获取响应内容 --字符串（网页源代码）
# html=resp.text
# print(html)

# content属性： 获取响应内容 --字节串（抓取图片、文件、音频、视频...）
html=resp.content
print(html)

# status_code属性： 获取HTTP响应码
code=resp.status_code

# url属性：返回实际数据的URL地址
url=resp.url
