url='https://www.baidu.com/s?wd=白敬亭&pn={}'
for page in range(100):
    page_url=url.format(page*10)
    print(page_url)