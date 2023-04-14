# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 22:33:42 2019

@author: macbook
"""

import requests
from lxml import etree
import pandas as pd


#初恋这件小事
url='https://movie.douban.com/subject/4739952/comments?status=P'

data=requests.get(url).text
s=etree.HTML(data)

shortreview=s.xpath('//*[@id="content"]/h1/text()')
seen=s.xpath('//*[@id="content"]/div/div[1]/div[1]/ul/li[1]/span/text()')
wanttosee=s.xpath('//*[@id="content"]/div/div[1]/div[1]/ul/li[2]/a/text()')
praise=s.xpath(' //*[@id="content"]/div/div[1]/div[3]/label[2]/span[2]/text()')
commonly=s.xpath('//*[@id="content"]/div/div[1]/div[3]/label[3]/span[2]/text()')
negativecomment=s.xpath('//*[@id="content"]/div/div[1]/div[3]/label[4]/span[2]/text()')

print('短评:',shortreview)
print('看过:',seen)
print('想看:',wanttosee)
print('好评：',praise)
print('一般:',commonly)
print('差评:',negativecomment)

c={"短评" : shortreview,
   "看过" : seen,
   "想看" : wanttosee,
   "好评" : praise,
   "一般" : commonly,
   "差评" : negativecomment
   }

df = pd.DataFrame(c)
df.to_csv('初恋这件小事.csv', encoding='gbk', index=True)




#一出好戏

url='https://movie.douban.com/subject/26985127/comments?status=P'

data=requests.get(url).text
s=etree.HTML(data)

shortreview=s.xpath('//*[@id="content"]/h1/text()')
seen=s.xpath('//*[@id="content"]/div/div[1]/div[1]/ul/li[1]/span/text()')
wanttosee=s.xpath('//*[@id="content"]/div/div[1]/div[1]/ul/li[2]/a/text()')
praise=s.xpath('//*[@id="content"]/div/div[1]/div[3]/label[2]/span[2]/text()')
commonly=s.xpath('//*[@id="content"]/div/div[1]/div[3]/label[3]/span[2]/text()')
negativecomment=s.xpath('//*[@id="content"]/div/div[1]/div[3]/label[4]/span[2]/text()')

print('短评:',shortreview)
print('看过:',seen)
print('想看:',wanttosee)
print('好评：',praise)
print('一般:',commonly)
print('差评:',negativecomment)

d={"短评" : shortreview,
   "看过" : seen,
   "想看" : wanttosee,
   "好评" : praise,
   "一般" : commonly,
   "差评" : negativecomment
   }

df = pd.DataFrame(d)
df.to_csv('一出好戏.csv', encoding='gbk', index=True)



#小森林

url='https://movie.douban.com/subject/25814705/comments?status=P'

data=requests.get(url).text
s=etree.HTML(data)

shortreview=s.xpath('//*[@id="content"]/h1/text()')
seen=s.xpath('//*[@id="content"]/div/div[1]/div[1]/ul/li[1]/span/text()')
wanttosee=s.xpath('//*[@id="content"]/div/div[1]/div[1]/ul/li[2]/a/text()')
praise=s.xpath('//*[@id="content"]/div/div[1]/div[3]/label[2]/span[2]/text()')
commonly=s.xpath('//*[@id="content"]/div/div[1]/div[3]/label[3]/span[2]/text()')
negativecomment=s.xpath('//*[@id="content"]/div/div[1]/div[3]/label[4]/span[2]/text()')

print('短评:',shortreview)
print('看过:',seen)
print('想看:',wanttosee)
print('好评：',praise)
print('一般:',commonly)
print('差评:',negativecomment)


e={"短评" : shortreview,
   "看过" : seen,
   "想看" : wanttosee,
   "好评" : praise,
   "一般" : commonly,
   "差评" : negativecomment
   }

df = pd.DataFrame(e)
df.to_csv('小森林.csv', encoding='gbk', index=True)


#秒速五厘米

url='https://movie.douban.com/subject/2043546/comments?status=P'

data=requests.get(url).text
s=etree.HTML(data)

shortreview=s.xpath('//*[@id="content"]/h1/text()')
seen=s.xpath('//*[@id="content"]/div/div[1]/div[1]/ul/li[1]/span/text()')
wanttosee=s.xpath('//*[@id="content"]/div/div[1]/div[1]/ul/li[2]/a/text()')
praise=s.xpath('//*[@id="content"]/div/div[1]/div[3]/label[2]/span[2]/text()')
commonly=s.xpath('//*[@id="content"]/div/div[1]/div[3]/label[3]/span[2]/text()')
negativecomment=s.xpath('//*[@id="content"]/div/div[1]/div[3]/label[4]/span[2]/text()')

print('短评:',shortreview)
print('看过:',seen)
print('想看:',wanttosee)
print('好评：',praise)
print('一般:',commonly)
print('差评:',negativecomment)

f={"短评" : shortreview,
   "看过" : seen,
   "想看" : wanttosee,
   "好评" : praise,
   "一般" : commonly,
   "差评" : negativecomment
   }

df = pd.DataFrame(f)
df.to_csv('秒速五厘米.csv', encoding='gbk', index=True)



#祈祷落幕时

url='https://movie.douban.com/subject/27040737/comments?status=P'

data=requests.get(url).text
s=etree.HTML(data)

shortreview=s.xpath('//*[@id="content"]/h1/text()')
seen=s.xpath('//*[@id="content"]/div/div[1]/div[1]/ul/li[1]/span/text()')
wanttosee=s.xpath('//*[@id="content"]/div/div[1]/div[1]/ul/li[2]/a/text()')
praise=s.xpath('//*[@id="content"]/div/div[1]/div[3]/label[2]/span[2]/text()')
commonly=s.xpath('//*[@id="content"]/div/div[1]/div[3]/label[3]/span[2]/text()')
negativecomment=s.xpath('//*[@id="content"]/div/div[1]/div[3]/label[4]/span[2]/text()')

print('短评:',shortreview)
print('看过:',seen)
print('想看:',wanttosee)
print('好评：',praise)
print('一般:',commonly)
print('差评:',negativecomment)

g={"短评" : shortreview,
   "看过" : seen,
   "想看" : wanttosee,
   "好评" : praise,
   "一般" : commonly,
   "差评" : negativecomment
   }

df = pd.DataFrame(g)
df.to_csv('祈祷落幕时.csv', encoding='gbk', index=True)
