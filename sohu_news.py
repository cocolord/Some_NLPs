# -*- coding:UTF-8 -*-
# Writen by Lusen Dong
# 2018.5.1
# 以搜狐历史频道来测试
import os
import re
import requests
import time
import traceback
from bs4 import BeautifulSoup

Alink = 'link.txt'
linkobj = open(Alink,'w')

class CrawlData:
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Connection': 'keep-alive',
        'Accept-Encoding': 'gzip,deflate',
        'Accept-Language': 'zh-CN;zh;q=0.9',
        'Cache-Control': 'no-cache',
        'referer': 'http://news.ifeng.com/listpage/4764/2/1/53979570/54630696/list.shtml',
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
    }
    Linkset = set()
    def getPageLink(self):
        # j决定了文章目录的页数
        for j in range(1,21):
            #把你想要的频道的URL写进Menulink
            Menulink = "http://news.ifeng.com/listpage/4766/" + str(j) + "/1/53099657/list.shtml"
            OldMenulink = "http://news.ifeng.com/history/zhuanjialunshi/list_0/"+str(j)+".shtml"
            Mreq = requests.get(OldMenulink, headers=self.headers).text
            Msoup = BeautifulSoup(Mreq, 'html.parser')
            pat = r'<h2><a href="(.*)" target="_blank" title=".*">.*</a></h2>"'
            pat = "http://news.ifeng.com/a/.*"
            AA = Msoup.find_all('a',href = re.compile('http://news.ifeng.com/a/'))
            # print(AA)
            for link in AA:
                link = link.get('href')
                if(len(link)<55):
                    self.Linkset.add(link)
                    print(link)
                    linkobj.writelines(link)
        linkobj.close()
    def getArticleContent(self):
        count = 1
        for link in self.Linkset:
            req = requests.get(link, headers=self.headers).content.decode('utf-8')
            soup = BeautifulSoup(req, 'html.parser')
            #需要看一下页面的源代码,决定用哪种格式
            pat = r'<!--mainContent begin-->(.*)<!--mainContent end-->'
            pat2 = r'<!-- 正文begin -->(.*)<!-- 正文end -->'
            text = re.findall(pat, req, re.S | re.M)
            with open(str(count)+'.txt','w',encoding='utf-8') as his:
                print(text)
                his.writelines(text)
                count += 1

if __name__ == "__main__":
    instance = CrawlData()
    instance.getPageFromLink()
    instance.getArticleContent()