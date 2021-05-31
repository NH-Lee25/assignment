# -*- coding: utf-8 -*-
"""
Created on Fri May 14 18:31:03 2021

@author: nabu9
"""
"프로젝트 : 사진 찍는 전시회는 싫어!"

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

#-----------------------------
#셀레늄 초기설정
"""
options = Options()
#options.add_argument('--start-fullscreen')
#options.add_argument("headless")

dr = webdriver.Chrome('C:/Users/nabu9/Desktop/2021 1학기/딥러닝/전시회/chromedriver.exe',chrome_options=options)
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
"""

#-------------------------------
#포스터 정보 한글화
import pytesseract
import cv2
import numpy as np

pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR"
config = ('-l kor+eng --oem 3 --psm 4')

#im=cv2.imread(r"C:\Users\nabu9\Desktop\2021 1학기\딥러닝\전시회\test.jpg")

#img_array = np.fromfile("C:/Users/nabu9/Desktop/2021-1/deep_learing/jusi/test.jpg", np.uint8)
#img_gray = cv2.imdecode(img_array, cv2.IMREAD_GRAYSCALE)

img_gray=cv2.imread("C:/Users/nabu9/Desktop/2021-1/deep_learing/jusi/test.jpg",cv2.IMREAD_GRAYSCALE)
gray_text=pytesseract.image_to_string(img_gray)
