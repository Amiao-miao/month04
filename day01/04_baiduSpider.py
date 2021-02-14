'''
请输入关键字：白敬亭
最终保存到本地：白敬亭.html
'''
import requests
# 1.拼接url
keyword=input('关键字：')
url='http://tieba.baidu.com/s?wd={}'.format(keyword)
headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'}
# 2.发请求获取响应内容
html=requests.get(url=url,headers=headers).content.decode('utf-8')
# 3.保存文件
filename='{}.html'.format(keyword)
with open(filename,'w') as f:
    f.write(html)
