# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 15:33:20 2019

@author: macbook
"""

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from requests_html import HTMLSession
import pandas as pd


session=HTMLSession()    
for i in range(0,40,20):
    url='https://movie.douban.com/subject/4739952/reviews?start='+ str(i)
    r=session.get(url)
    sel='#content > div > div.article > div.paginator > span.next > a'
    print (url)

browser= webdriver.Chrome('C:\python\chromedriver')
browser.get(url)

def get_text_from_xpath(brower,xpath):
#strip()
    tup = ()
    critic = brower.find_element_by_xpath(xpath + '/div/header/a[2]').text.strip()
    commenttime = brower.find_element_by_xpath(xpath + '/div/header/span[2]').text.strip()
    commenttitle = brower.find_element_by_xpath(xpath + '/div/div/h2/a').text.strip()
    useful = brower.find_element_by_xpath(xpath + '/div/div/div[3]/a[1]').text.strip()
    useless = brower.find_element_by_xpath(xpath + '/div/div/div[3]/a[2]').text.strip()
    responsive = brower.find_element_by_xpath(xpath + '/div/div/div[3]/a[3]').text.strip()
            
    tup=(critic,commenttime,commenttitle,useful,useless,responsive)
    return tup

def CrawlingDouban():
    list=browser.find_elements(By.XPATH,'//div[@class=\'review-list  \']/div')
    liNum= len(list)
    print('当前页数据总数：%s'%liNum)
    lists=[]
    index=1
    while index<21:
        xpath='//*[@id="content"]/div/div[1]/div[1]/div[%s]' %index
        index +=1
        lists.append(get_text_from_xpath(browser,xpath))
    return lists


time.sleep(3)


df=pd.DataFrame(CrawlingDouban())
print(df)
df.columns=['评论人','评论时间 ','评论标题','有用数','无用数','反应数']
df.to_csv('初恋这件小事评论2.csv',encoding='UTF-8',index=True)

CrawlingDouban()

browser.close()