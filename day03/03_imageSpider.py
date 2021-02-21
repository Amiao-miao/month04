'''
将图片抓取到本地
'''

import requests
from fake_useragent import UserAgent


image_url='https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fn.sinaimg.cn%2Fsinacn16%2F618%2Fw873h545%2F20180808%2F850e-hhkuskt8842029.png&refer=http%3A%2F%2Fn.sinaimg.cn&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1616055194&t=9494389a4f8963a6d8bd24508addf90b'
headers={'User-Agent':UserAgent().random}
image_html=requests.get(url=image_url,headers=headers).content
with open('bai.jpg','wb') as f:
    f.write(image_html)