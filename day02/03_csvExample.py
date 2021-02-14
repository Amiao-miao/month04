'''
csv模块示例
'''
import csv
with open('fengyun.csv','w') as f:
    writer=csv.writer(f)
    writer.writerow(['捏风','学瘾狂刀','梦'])
    writer.writerow(['步惊云', '绝世好剑', '楚楚'])


f=open('fengyun.csv','a')
writer=csv.writer(f)
writer.writerow(['亲爽','天双全','孔慈'])
f.close()