'''
https://www.guazi.com/huzhou/buy/o2/#bread
第一页：o1
第二页：o2
……
第n页：on
'''
url='https://www.guazi.com/huzhou/buy/o{}/#bread'
for page in range(1,51):
    page_url=url.format(page)
    print(page_url)