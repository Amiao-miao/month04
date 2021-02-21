import requests
from fake_useragent import UserAgent
from lxml import etree
import time
import random
import pymongo

class lianJiaSpider:
    def __init__(self):
        self.url='https://bj.lianjia.com/ershoufang/pg{}/'
        self.conn=pymongo.MongoClient('localhost',27017)
        self.db=self.conn['lianjiadb']
        self.myset=self.db['lianjiaset']

    def get_html(self,url):
        headers={'User-Agent':UserAgent().random}
        html=requests.get(url=url,headers=headers).text
        self.parse_html(html)

    def parse_html(self,html):
        eobj=etree.HTML(html)
        lianjia_list=eobj.xpath('//ul/li[@class="clear LOGVIEWDATA LOGCLICKDATA"]')
        for lianjia in lianjia_list:
            item={}
            area_list=lianjia.xpath('.//div[@class="positionInfo"]/a[1]/text()')
            item['area']=area_list[0] if area_list else None

            address_list = lianjia.xpath('.//div[@class="positionInfo"]/a[2]/text()')
            item['address'] = address_list[0] if address_list else None

            info_list=lianjia.xpath('.//div[@class="houseInfo"]/text()')
            item['info'] = info_list[0] if info_list else None

            total_list = lianjia.xpath('.//div[@class="totalPrice"]/span/text()')
            item['total'] = total_list[0] if total_list else None

            unit_list = lianjia.xpath('.//div[@class="unitPrice"]/span/text()')
            item['unit'] = unit_list[0] if unit_list else None

            print(item)
            self.myset.insert_one(item)

    def crawl(self):
        for page in range(1,5):
            page_url=self.url.format(page)
            self.get_html(url=page_url)
            time.sleep(random.randint(1,2))

if __name__ == '__main__':
    spider=lianJiaSpider()
    spider.crawl()


