#encoding: utf--8
import re
import os

with open('22.txt','r',encoding='utf-8') as file:
    buff = file.readlines()
    content = ''
    for item in buff:
        content += item
    print(content)
    # <span style="font-family: 楷体_GB2312, 楷体;"><span style="font-size: 14px;">至元十九年，&ldquo;海盗们&rdquo;开启了中国海上漕运史前无古人的冒险之旅。此后他们又相继摸索出两条新航线，海运效率大增。顺利的话，最快10天就可以由浙江抵达大都。据《大元海运记》《元史&middot;食货志》统计，海运运粮数量呈阶梯式蹿升，最多时一年可达350万石。途中粮食损耗也由最初的25%下降到1%。海上漕运从此成为关乎元大都存亡的经济命脉。</span></span>
    buff = re.sub(r'<span style="font-family: 楷体_GB2312, 楷体;">.*</span></span>','',content)
    buff = re.sub(r'<p class="detailPic">.*<p class="picIntro">','',buff)
    buff = re.sub(r'<strong>.*?<strong>','',buff)
    buff = re.sub(r'<strong>.*?</strong>', '', buff)
    buff = re.sub(r'<span>.*?</span>','',buff)
    buff = re.sub(r'<p>本文摘自.*?</p>','',buff)
    # buff = re.sub(r'</strong>','',buff)
    buff = re.sub(r'<span class="ifengLogo">.*</span>','',buff)
    buff = re.sub(r'</span>','',buff)
    buff = re.sub(r'</strong>','',buff)
    print(buff)