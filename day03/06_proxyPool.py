'''
建立代理ip池--开放代理
'''

import requests
from fake_useragent import UserAgent
class ProxyPool:
    def __init__(self):
        self.api_url=''
        self.test_url='http://httpbin.org/get'
        self.headers={'User-Agent':UserAgent().random}


    def get_proxy(self):
        '''获取代理ip'''
        html=requests.get(url=self.api_url,headers=self.headers).text
        proxy_list=html.split('\r\n')
        for proxy in proxy_list:
            # 测试函数
            self.test_proxy(proxy)

    def test_proxy(self,proxy):
        '''测试一个代理IP是否可用'''
        proxies={
            'http':'http://{}'.format(proxy),
            'https': 'https://{}'.format(proxy),
        }
        try:
            resp=requests.get(url=self.test_url,proxies=proxies,headers=self.headers,timeout=3)
            print(proxy,'可用')
        except Exception as e:
            print(proxy,'不可用')


if __name__ == '__main__':
    spider=ProxyPool()
    spider.get_proxy()