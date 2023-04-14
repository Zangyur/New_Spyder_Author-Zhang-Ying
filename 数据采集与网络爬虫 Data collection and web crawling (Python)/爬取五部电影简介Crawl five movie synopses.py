# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 16:21:51 2019

@author: Administrator
"""
import requests
from lxml import etree
import pandas as pd


###初恋这件小事

url='https://movie.douban.com/subject/4739952/'
data=requests.get(url).text
s=etree.HTML(data)
film=s.xpath('//*[@id="content"]/h1/span[1]/text()')
years=s.xpath('//*[@id="content"]/h1/span[2]/text()')
score=s.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()')
evaluation=s.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/div/div[2]/a/span/text()')
fivestar=s.xpath('//*[@id="interest_sectl"]/div[1]/div[3]/div[1]/span[2]/text()')
fourstar=s.xpath('//*[@id="interest_sectl"]/div[1]/div[3]/div[2]/span[2]/text()')
treestar=s.xpath('//*[@id="interest_sectl"]/div[1]/div[3]/div[3]/span[2]/text()')
twostar=s.xpath('//*[@id="interest_sectl"]/div[1]/div[3]/div[4]/span[2]/text()')
onestar=s.xpath('//*[@id="interest_sectl"]/div[1]/div[3]/div[5]/span[2]/text()')
print('影名:',film)
print('年份:',years)
print('评分:',score)
print('评价人数:',evaluation)
print('5星:',fivestar)
print('4星:',fourstar)
print('3星:',treestar)
print('2星:',twostar)
print('1星:',onestar)

d={"影名" : film,
   "年份" : years,
   "评分" : score,
   "评价人数" : evaluation,
   "5星" : fivestar,
   "4星" : fourstar,
   "3星" : treestar,
   "2星" : twostar,
   "1星" : onestar
   }

df = pd.DataFrame(d)
df.to_csv('初恋这件小事简介.csv', encoding='UTF-8', index=True)

###一出好戏

url='https://movie.douban.com/subject/26985127/'
data=requests.get(url).text
s=etree.HTML(data)
film=s.xpath('//*[@id="content"]/h1/span[1]/text()')
years=s.xpath('//*[@id="content"]/h1/span[2]/text()')
score=s.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()')
evaluation=s.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/div/div[2]/a/span/text()')
fivestar=s.xpath('//*[@id="interest_sectl"]/div[1]/div[3]/div[1]/span[2]/text()')
fourstar=s.xpath('//*[@id="interest_sectl"]/div[1]/div[3]/div[2]/span[2]/text()')
treestar=s.xpath('//*[@id="interest_sectl"]/div[1]/div[3]/div[3]/span[2]/text()')
twostar=s.xpath('//*[@id="interest_sectl"]/div[1]/div[3]/div[4]/span[2]/text()')
onestar=s.xpath('//*[@id="interest_sectl"]/div[1]/div[3]/div[5]/span[2]/text()')
print('影名:',film)
print('年份:',years)
print('评分:',score)
print('评价人数:',evaluation)
print('5星:',fivestar)
print('4星:',fourstar)
print('3星:',treestar)
print('2星:',twostar)
print('1星:',onestar)

e={"影名" : film,
   "年份" : years,
   "评分" : score,
   "评价人数" : evaluation,
   "5星" : fivestar,
   "4星" : fourstar,
   "3星" : treestar,
   "2星" : twostar,
   "1星" : onestar
   }

df = pd.DataFrame(e)
df.to_csv('一出好戏简介.csv', encoding='UTF-8', index=True)

###小森林(夏秋篇)

url='https://movie.douban.com/subject/25814705/'
data=requests.get(url).text
s=etree.HTML(data)
film=s.xpath('//*[@id="content"]/h1/span[1]/text()')
years=s.xpath('//*[@id="content"]/h1/span[2]/text()')
score=s.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()')
evaluation=s.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/div/div[2]/a/span/text()')
fivestar=s.xpath('//*[@id="interest_sectl"]/div[1]/div[3]/div[1]/span[2]/text()')
fourstar=s.xpath('//*[@id="interest_sectl"]/div[1]/div[3]/div[2]/span[2]/text()')
treestar=s.xpath('//*[@id="interest_sectl"]/div[1]/div[3]/div[3]/span[2]/text()')
twostar=s.xpath('//*[@id="interest_sectl"]/div[1]/div[3]/div[4]/span[2]/text()')
onestar=s.xpath('//*[@id="interest_sectl"]/div[1]/div[3]/div[5]/span[2]/text()')
print('影名:',film)
print('年份:',years)
print('评分:',score)
print('评价人数:',evaluation)
print('5星:',fivestar)
print('4星:',fourstar)
print('3星:',treestar)
print('2星:',twostar)
print('1星:',onestar)

g={"影名" : film,
   "年份" : years,
   "评分" : score,
   "评价人数" : evaluation,
   "5星" : fivestar,
   "4星" : fourstar,
   "3星" : treestar,
   "2星" : twostar,
   "1星" : onestar
   }

df = pd.DataFrame(g)
df.to_csv('小森林简介.csv', encoding='UTF-8', index=True)





###秒速五厘米

url='https://movie.douban.com/subject/2043546/'
data=requests.get(url).text
s=etree.HTML(data)
film=s.xpath('//*[@id="content"]/h1/span[1]/text()')
years=s.xpath('//*[@id="content"]/h1/span[2]/text()')
score=s.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()')
evaluation=s.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/div/div[2]/a/span/text()')
fivestar=s.xpath('//*[@id="interest_sectl"]/div[1]/div[3]/div[1]/span[2]/text()')
fourstar=s.xpath('//*[@id="interest_sectl"]/div[1]/div[3]/div[2]/span[2]/text()')
treestar=s.xpath('//*[@id="interest_sectl"]/div[1]/div[3]/div[3]/span[2]/text()')
twostar=s.xpath('//*[@id="interest_sectl"]/div[1]/div[3]/div[4]/span[2]/text()')
onestar=s.xpath('//*[@id="interest_sectl"]/div[1]/div[3]/div[5]/span[2]/text()')
print('影名:',film)
print('年份:',years)
print('评分:',score)
print('评价人数:',evaluation)
print('5星:',fivestar)
print('4星:',fourstar)
print('3星:',treestar)
print('2星:',twostar)
print('1星:',onestar)

c={"影名" : film,
   "年份" : years,
   "评分" : score,
   "评价人数" : evaluation,
   "5星" : fivestar,
   "4星" : fourstar,
   "3星" : treestar,
   "2星" : twostar,
   "1星" : onestar
   }

df = pd.DataFrame(c)
df.to_csv('秒速五厘米简介.csv', encoding='UTF-8', index=True)





###祈祷落幕时

url='https://movie.douban.com/subject/27040737/'
data=requests.get(url).text
s=etree.HTML(data)
film=s.xpath('//*[@id="content"]/h1/span[1]/text()')
years=s.xpath('//*[@id="content"]/h1/span[2]/text()')
score=s.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()')
evaluation=s.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/div/div[2]/a/span/text()')
fivestar=s.xpath('//*[@id="interest_sectl"]/div[1]/div[3]/div[1]/span[2]/text()')
fourstar=s.xpath('//*[@id="interest_sectl"]/div[1]/div[3]/div[2]/span[2]/text()')
treestar=s.xpath('//*[@id="interest_sectl"]/div[1]/div[3]/div[3]/span[2]/text()')
twostar=s.xpath('//*[@id="interest_sectl"]/div[1]/div[3]/div[4]/span[2]/text()')
onestar=s.xpath('//*[@id="interest_sectl"]/div[1]/div[3]/div[5]/span[2]/text()')
print('影名:',film)
print('年份:',years)
print('评分:',score)
print('评价人数:',evaluation)
print('5星:',fivestar)
print('4星:',fourstar)
print('3星:',treestar)
print('2星:',twostar)
print('1星:',onestar)

f={"影名" : film,
   "年份" : years,
   "评分" : score,
   "评价人数" : evaluation,
   "5星" : fivestar,
   "4星" : fourstar,
   "3星" : treestar,
   "2星" : twostar,
   "1星" : onestar
   }

df = pd.DataFrame(f)
df.to_csv('祈祷落幕时简介.csv', encoding='UTF-8', index=True)

