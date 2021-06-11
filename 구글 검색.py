# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 18:35:03 2021

@author: nabu9
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib import parse
import re

df_junsi=pd.read_csv("C:/Users/nabu9/Desktop/2021-1/deep_learning/junsi/0602_0311.csv",encoding='utf-8-sig')
Description_table=pd.DataFrame(columns=["google1","google2","google3"])

#207 0 대체 뭐지
for junsi_num in range(0,len(df_junsi)):
    print("start",junsi_num)
    
    #검색결과 상위 3개 링크 수집
    #특수문자 # 제거
    junsi_name_search=re.sub("#","",df_junsi["junsi_name"][junsi_num])
    url = "https://www.google.com/search?q="+str(junsi_name_search)+" "+str(df_junsi["place"][junsi_num])+"&aqs=chrome..69i57.6397j0j7&sourceid=chrome&ie=UTF-8"
                                                                              
    response = requests.get(url)
    
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    a = soup.select("a")
    
    i=1
    google_search=[]
    for link in a:
        #print(i,"\n",link.attrs['href'])
        if(i>=18 and i<=20):
            google_search.append(link.attrs['href'])
            
        if(i>=20):
            break
        i+=1
        
    for i in range(0,3):
        google_search[i]=re.sub("^.*q=","",google_search[i])
        google_search[i]=re.sub("&sa=.*$","",google_search[i])
        google_search[i]=parse.unquote(google_search[i])
        
    #--------------------------------------------------------------------------
    description_total=["","",""]
    for page_num in range(0,3):
        print("page_num : ",page_num)
        page_url=google_search[page_num]
        
        try:
            response_page = requests.get(page_url)
            html_page = response_page.text
            soup_page = BeautifulSoup(html_page, 'html.parser')
            p = soup_page.select("p")
        except:
            print("call error")
    
        for p_text in p:
            description_total[page_num]=(description_total[page_num])+(p_text.text)+"\n"
            #print(p_text.text+"\n")
            
            
        #artbava 사이트의 경우, 데이터가 있는 경우는 많지만, text에 이상한 단어가 섞임
        if("artbava.com" in google_search[page_num]):
            print("artvana")
            p_span = soup_page.select("span")
            delete=[]

            for p_text in p_span:
                delete.append(p_text.text)

            delete=list(set(delete))        
            for i in range(0,len(delete)):
                if(len(delete[i])!=6):
                    delete[i]=""

            delete = list(filter(None, delete)) #이상한 단어의 모음
            
            for i in range(0,len(delete)):
                description_total[page_num]=re.sub(delete[i],"",description_total[page_num])
            
        
    Description_table.loc[len(Description_table)]=(description_total[0],description_total[1],description_total[2])
    print("Add value; junsi_num : ",junsi_num)

#Description_table.loc[4][2]
#Description_table.to_csv("C:/Users/nabu9/Desktop/2021-1/deep_learning/junsi/decription_table_208~.csv",encoding='utf-8-sig',index=None)

