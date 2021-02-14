'''
贴吧名：李钟硕吧
起始页：2
终止页：6
李钟硕吧_第2页.html  李钟硕吧_第3页.html  ...
'''
import requests
import time
import random
class TieBaSpider:
    def __init__(self):
        '''定义常用变量'''
        self.url='https://tieba.baidu.com/f?kw={}&pn={}'
        self.headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'}
    def get_html(self,url):
        '''请求函数'''
        html=requests.get(url=url,headers=self.headers).text
        return html

    def parse_html(self):
        '''解析函数'''
        pass

    def save_html(self,filename,html):
        '''数据处理函数'''
        with open(filename,'w',encoding='utf-8') as f:
            f.write(html)

    def crawl(self):
        '''爬虫逻辑函数'''
        name=input('贴吧名：')
        start=int(input('起始页：'))
        end=int(input('终止页：'))
        for page in range(start,end+1):
            # 拼接多页的url地址
            pn=(page-1)*50
            page_url=self.url.format(name,pn)
            # 发请求、数据处理(调用上面的函数)
            page_html = self.get_html(url=page_url)
            filename=f'{name}_第{page}页.html'
            self.save_html(filename,page_html)
            print(filename,'抓取成功')
            # 控制数据抓取的频率
            time.sleep(random.randint(1,2))
if __name__ == '__main__':
    spider=TieBaSpider()
    spider.crawl()