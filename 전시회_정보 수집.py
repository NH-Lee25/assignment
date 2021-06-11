# -*- coding: utf-8 -*-
"""
Created on Fri May 14 18:31:03 2021

@author: nabu9
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re


#-----------------------------
#셀레늄 초기설정
options = Options()
#options.add_argument('--start-fullscreen')
#options.add_argument("headless")

dr = webdriver.Chrome('C:/Users/nabu9/Desktop/2021-1/deep_learning/junsi/chromedriver.exe',chrome_options=options)
# 페이지 접속
dr.get('https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%A0%84%EC%8B%9C%ED%9A%8C')


#----------------------------
# 전시회 이름, 기간, 전시장소 담기
df_junsi=pd.DataFrame(columns=["junsi_name","start","end","place"]) #초기화

while(True):
    time.sleep(5)
    
    for i in range(1,5):
        
        try:
            name = dr.find_element_by_css_selector("#mflick > div > div > div > div > div:nth-child("+str(i)+") > div.data_area > div > div.title > div > strong > a").text
            due = dr.find_element_by_css_selector("#mflick > div > div > div > div > div:nth-child("+str(i)+") > div.data_area > div > div.info > dl:nth-child(1) > dd").text
            location=dr.find_element_by_css_selector("#mflick > div > div > div > div > div:nth-child("+str(i)+") > div.data_area > div > div.info > dl:nth-child(2) > dd > a").text
                
            #시작 날짜와 끝 날짜 계산
            start=re.sub("\~.*","",due)
            end=re.sub("^.*\.~","",due)
            
            #데이터 베이스 값 추가
            df_junsi.loc[len(df_junsi)]=name,start,end,location
            
        except:
            break
    
    
    #페이지 넘기기
    try: 
        next_page=dr.find_element_by_css_selector("#main_pack > div.sc_new.cs_common_module.case_list.color_1._kgs_art_exhibition > div.cm_content_wrap > div > div > div.cm_paging_area._page > div > a.pg_next.on")
        next_page.click()
    
    except:
        dr.close()
        dr.quit()
        break    

df_junsi.to_csv("C:/Users/nabu9/Desktop/2021-1/deep_learning/junsi/0602_0311.csv",encoding='utf-8-sig',index=None)




