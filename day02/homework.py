'''
瓜子二手车：二级页面抓取
'''
import sys

import requests
import re
import time
import random
import redis
import pymongo
from hashlib import md5

class GuaZiSpider:
    def __init__(self):
        self.url='https://www.guazi.com/huzhou/buy/o{}/#bread'
        self.headers={
            'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
            'Cookie':'uuid=c8e1ba9c-0782-4042-8f62-1ceffe3f3474; ganji_uuid=8941194292297897799817; cityDomain=huzhou; antipas=Q2sxg586fI481n5940192W74907h6; user_city_id=30; close_finance_popup=2021-02-15; lg=1; clueSourceCode=%2A%2300; sessionid=d728e10b-c269-479d-9601-ac6e7aac5302; Hm_lvt_bf3ee5b290ce731c7a4ce7a617256354=1613215481,1613375752,1613377537; cainfo=%7B%22ca_a%22%3A%22-%22%2C%22ca_b%22%3A%22-%22%2C%22ca_s%22%3A%22self%22%2C%22ca_n%22%3A%22self%22%2C%22ca_medium%22%3A%22-%22%2C%22ca_term%22%3A%22-%22%2C%22ca_content%22%3A%22-%22%2C%22ca_campaign%22%3A%22-%22%2C%22ca_kw%22%3A%22-%22%2C%22ca_i%22%3A%22-%22%2C%22scode%22%3A%22-%22%2C%22keyword%22%3A%22-%22%2C%22ca_keywordid%22%3A%22-%22%2C%22display_finance_flag%22%3A%22-%22%2C%22platform%22%3A%221%22%2C%22version%22%3A1%2C%22client_ab%22%3A%22-%22%2C%22guid%22%3A%22c8e1ba9c-0782-4042-8f62-1ceffe3f3474%22%2C%22ca_city%22%3A%22huzhou%22%2C%22sessionid%22%3A%22d728e10b-c269-479d-9601-ac6e7aac5302%22%7D; preTime=%7B%22last%22%3A1613377667%2C%22this%22%3A1613215479%2C%22pre%22%3A1613215479%7D; Hm_lpvt_bf3ee5b290ce731c7a4ce7a617256354=1613377668'
        }
        self.r = redis.Redis(host='localhost', port=6379, db=0)
        self.conn=pymongo.MongoClient('localhost',27017)
        self.db=self.conn['guazidb']
        self.myset=self.db['guaziset']

    def get_html(self,url):
        html=requests.get(url=url,headers=self.headers).content.decode('utf-8')
        return html

    def func(self,regex,html):
        r_list=re.findall(regex,html,re.S)
        return r_list

    def md5_href(self,href):
        m=md5()
        m.update(href.encode())
        return m.hexdigest()


    def parse_html(self,first_url):
        first_html=self.get_html(url=first_url)
        first_regex='<li data-scroll-track=.*? href="(.*?)" '
        first_list=self.func(first_regex,first_html)
        for first in first_list:
            finger=self.md5_href(first)
            if self.r.sadd('car:spiders',finger)==1:
                # print(item)
                self.get_two_html(first)
                time.sleep(random.randint(1,2))
            else:
                sys.exit('更新完成')

    def get_two_html(self,first):
        second_url='https://www.guazi.com'+first
        second_html=self.get_html(url=second_url)
        second_regex='<h1 class="titlebox">(.*?)(?:<span class="labels">|</h1>)'
        second_list=self.func(second_regex,second_html)
        if second_list:
            item={}
            item['name']=second_list[0].strip()
            print(item)
            self.myset.insert_one(item)
        else:
            print('次辆汽车提取失败')


    def crawl(self):
        for page in range(1,3):
            page_url=self.url.format(page)
            self.parse_html(page_url)
            time.sleep(random.randint(1, 2))

if __name__ == '__main__':
    spider=GuaZiSpider()
    spider.crawl()