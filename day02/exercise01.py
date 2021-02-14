'''
库名：guazidb
集合名：guaziset
插入一条文档：{'title':'特斯拉modely','km':'594公里','price':'33.99万'}
'''

import pymongo

conn=pymongo.MongoClient('localhost',27017)
db=conn['guazidb']
myset=db['guaziset']
myset.insert_one({'title':'特斯拉modely','km':'594公里','price':'33.99万'})