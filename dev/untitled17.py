# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 19:00:15 2023

@author: taichi.mitsuhashi
"""

import PyPDF2
import pandas as pd

#from translate import Translator
#translator=Translator(from_lang="en",to_lang="ja")


with open("C:\\Users\\taichi.mitsuhashi\\Downloads\\IFS World and Country Notes_Latest.pdf", "rb") as f:
    reader = PyPDF2.PdfReader(f)
    dic_summary={}
    list_page=[]
    for p in range(358):
        #if p<=6:
        page = reader.pages[p]
        print(f"***********{p}")
        #print(page.extract_text())
        txt_data=page.extract_text()
        #txt_data_ja=translator.translate(txt_data)
        txt_data=txt_data.replace("\n","")
        #dic_summary[f"page_{p}"]=txt_data
        dic_summary[f"page_{p}"]=txt_data
        list_page.append(f"page_{p}")
            
    df=pd.DataFrame(list(dic_summary.items()))
    df.to_csv("C:\\Users\\taichi.mitsuhashi\\.spyder-py3\\02_Data_Store\\PDF_Data\\pages_data.csv")
    
    count_bm=0
    list_bm=[]
    for key,val in dic_summary.items():
        #if val.find("Broad Money")>0 and not val.find("Broad Money:")>0:
        if val.find("Broad Money:")>0:
            list_bm.append(key)
            count_bm+=1
    print(count_bm)

    df=pd.DataFrame(list_bm)
    df.to_csv("C:\\Users\\taichi.mitsuhashi\\.spyder-py3\\02_Data_Store\\PDF_Data\\list_bm.csv")
