'''
lxml+xpath 抓取豆瓣图书top250
'''

import requests
import re
import time
import random
from lxml import etree
from fake_useragent import UserAgent

class BookSpider:
    def __init__(self):
        self.url='https://book.douban.com/top250?start={}'



    def get_html(self,url):
        headers = {
            'User-Agent': UserAgent().random
        }
        html=requests.get(url=url,headers=headers).text
        self.parse_html(html)

    def parse_html(self,html):
        '''lxml+xpath解析提取数据'''

        # 1.创建解析对象
        eobj=etree.HTML(html)
        table_list=eobj.xpath('//table')
        # print(table_list)
        for table in table_list:
            item={}
            title_list=table.xpath('.//div[@class="pl2"]/a/@title')
            item['title']=title_list[0] if title_list else None

            info_list=table.xpath('.//p[@class="pl"]/text()')
            item['info']=info_list[0] if info_list else None

            score_list=table.xpath('.//span[@class="rating_nums"]/text()')
            item['score'] = score_list[0] if score_list else None

            commit_list=table.xpath('.//span[@class="pl"]/text()')
            item['commit']=commit_list[0][1:-1].strip() if commit_list else None

            comment_list=table.xpath('.//span[@class="inq"]/text()')
            item['comment']=comment_list[0] if comment_list else None

            print(item)

    def crawl(self):
        for page in range(1,11):
            start=(page-1)*25
            page_url=self.url.format(start)
            self.get_html(url=page_url)
            time.sleep(random.uniform(0,2))
if __name__ == '__main__':
    spider=BookSpider()
    spider.crawl()