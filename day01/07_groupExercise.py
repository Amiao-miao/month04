import re

html='''
<div class="animal">
    <p class="name">
			<a title="Tiger"></a>
    </p>
    <p class="content">
			Two tigers two tigers run fast
    </p>
</div>

<div class="animal">
    <p class="name">
			<a title="Rabbit"></a>
    </p>

    <p class="content">
			Small white rabbit white and white
    </p>
</div>
'''
# r_list:[(),()]
r_list=re.findall('<div class="animal">.*?<a title="(.*?)".*?<p class="content">(.*?)</p>',html,re.S)
for r in r_list:
    print('动物名称:',r[0])
    # .strip()去字符串两边的空白
    print('动物描述:', r[1].strip())