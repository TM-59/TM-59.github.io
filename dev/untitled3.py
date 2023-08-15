# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 10:17:53 2023

@author: taichi.mitsuhashi
"""

import requests
import pandas as pd
import csv

url_structure = 'http://dataservices.imf.org/REST/SDMX_JSON.svc/DataStructure/IFS'
data = requests.get(url_structure).json()
data_codelist = [x['@codelist'] for x in data['Structure']['KeyFamilies']['KeyFamily']['Components']['Dimension']]

url_codelist = "http://dataservices.imf.org/REST/SDMX_JSON.svc/CodeList/"
code_codelist = data_codelist[2]
data_request = requests.get(url_codelist + code_codelist).json()

data_output = []
key_count=0
keyword="Financial"
for code in data_request['Structure']['CodeLists']['CodeList']['Code']:
    val=code['@value']
    txt=code['Description']['#text']
    key_count+=txt.count(keyword)
    data_output.append((val,txt))
df_indicator = pd.DataFrame(data_output,columns=['indicator','description'])

#print(df_indicator.shape)
#print(df_indicator)
print(keyword)
print(key_count)

#CSVの出力
df_indicator.to_csv("list_indicator.csv", encoding = "shift_jis", index = None)

with open("C:\\Users\\taichi.mitsuhashi\\.spyder-py3\\02_Data_Store\\list_indicator_keywords.csv", "a") as f:
    writer=csv.writer(f,lineterminator="\n")
    writer.writerow([keyword,key_count])

with open("C:\\Users\\taichi.mitsuhashi\\.spyder-py3\\02_Data_Store\\list_indicator_keywords.csv", "rb") as f:
    print(f.read())