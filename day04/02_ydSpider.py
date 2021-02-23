import requests
import json
import time
from hashlib import md5
import random


class YdSpider:
    def __init__(self):
        self.post_url='http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
        self.headers={
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Content-Length": "239",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Cookie": "OUTFOX_SEARCH_USER_ID=722428891@10.169.0.83; JSESSIONID=aaa9gWl8GncnvfKhURdFx; OUTFOX_SEARCH_USER_ID_NCOO=927962974.4188644; ___rl__test__cookies=1613895789454",
            "Host": "fanyi.youdao.com",
            "Origin": "http://fanyi.youdao.com",
            "Pragma": "no-cache",
            "Referer": "http://fanyi.youdao.com/",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
        }
        # 输入要翻译的单词
        self.word=input('请输入要翻译的单词：')


    def md5_string(self,string):
        m=md5()
        m.update(string.encode())
        return m.hexdigest()


    def get_ts_salt_sign(self):
        '''获取ts salt sign'''
        ts=str(int(time.time()*1000))
        salt=ts+str(random.randint(0,9))
        string="fanyideskweb" + self.word + salt + "Tbh5E8=q6U3EXe+&L[4c@"
        sign=self.md5_string(string)

        return ts,salt,sign


    def attack_yd(self):
        '''逻辑函数'''
        ts,salt,sign=self.get_ts_salt_sign()
        data={
            "i": self.word,
            "from": "AUTO",
            "to": "AUTO",
            "smartresult": "dict",
            "client": "fanyideskweb",
            "salt": salt,
            "sign": sign,
            "lts": ts,
            "bv": "93ab8a54b571f3ceac16a13fbb95fb1c",
            "doctype": "json",
            "version": "2.1",
            "keyfrom": "fanyi.web",
            "action": "FY_BY_REALTlME",
        }
        #.json():把json格式的字符串转为python数据类型
        # .json() 等同于 json.loads('{}')
        html=requests.post(url=self.post_url,data=data,headers=self.headers).json()
        return html['translateResult'][0][0]['tgt']


if __name__ == '__main__':
    spider=YdSpider()
    print(spider.attack_yd())