'''
代理IP 存入mysql
create database proxydb charset utf8;
use proxydb;
create table proxytab(
ip varchar(50),
port varchar(10)
)charset utf8;
'''
import requests
from lxml import etree
import time
import random
from fake_useragent import UserAgent
import pymysql
class KuaiProxy:
    def __init__(self):
        self.url='https://www.kuaidaili.com/free/inha/{}/'
        self.test_url='http://httpbin.org/get'
        self.headers={'User-Agent':UserAgent().random}
        self.db=pymysql.connect('localhost','root','123456','proxydb',charset='utf8')
        self.cur=self.db.cursor()


    def get_proxy(self,url):
        html=requests.get(url=url,headers=self.headers).text
        self.parse_html(html)

    def parse_html(self,html):
        eobj=etree.HTML(html)
        kuai_list=eobj.xpath('//table/tbody/tr')
        for kuai in kuai_list:
            proxy=kuai.xpath('.//td[@data-title="IP"]/text()')[0]
            port=kuai.xpath('.//td[@data-title="PORT"]/text()')[0]
            self.test_proxy(proxy,port)

    def test_proxy(self,proxy,port):
        '''测试一个代理IP是否可用'''
        proxies={
            'http':'http://{}:{}'.format(proxy,port),
            'https': 'https://{}:{}'.format(proxy,port),
        }
        try:
            resp=requests.get(url=self.test_url,proxies=proxies,headers=self.headers,timeout=3)
            print(proxy,port,'可用')
            ins='insert into proxytab values(%s,%s)'
            self.cur.execute(ins,[proxy,port])
            self.db.commit()
        except Exception as e:
            print(proxy,port,'不可用')

    def crawl(self):
        for page in range(1,1001):
            page_url=self.url.format(page)
            self.get_proxy(url=page_url)
            time.sleep(random.randint(0,2))

if __name__ == '__main__':
    spider=KuaiProxy()
    spider.crawl()


