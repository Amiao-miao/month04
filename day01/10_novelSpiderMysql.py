'''


笔趣阁小说爬虫，抓取数据：href、title、author、comment
思路步骤：
    1.确认数据来源（查看网页源代码->搜索关键字）
    2.确认静态：观察URL地址规律
    3.写正则表达式
'''
import requests
import re
import time
import random
import pymysql


class NovelSpider:
    def __init__(self):
        self.url='https://www.biqukan.cc/fenlei1/{}.html'
        self.headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'}
        # 连接数据库，创建游标对象
        self.db=pymysql.connect('localhost','root','123456','noveldb',charset='utf8')
        self.cur=self.db.cursor()

    def get_html(self,url):
        html=requests.get(url=url,headers=self.headers).text
        # 直接调用解析函数
        self.parse_html(html)

    def parse_html(self,html):
        regex='<div class="caption">.*?href="(.*?)" title="(.*?)">.*?<small class="text-muted fs-12">(.*?)</small>.*?>(.*?)</p>'
        # r_list:[(href、title、author、comment),(),...]
        r_list=re.findall(regex,html,re.S)
        # 直接调用数据处理函数
        self.save_html(r_list)

    def save_html(self,r_list):
        ins='insert into novel_tab values(%s,%s,%s,%s)'
        for r in r_list:
            # execute(): 第二个参数可以为列表，也可为元组
            self.cur.execute(ins,r)
            self.db.commit()


    def run(self):
        for page in range(1,3):
            page_url=self.url.format(page)
            self.get_html(url=page_url)
            time.sleep(random.randint(1,3))
        # 所有的数据抓取完成后断开连接
        self.cur.close()
        self.db.close()

if __name__ == '__main__':
    spider=NovelSpider()
    spider.run()
