# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 15:39:30 2023

@author: taichi.mitsuhashi
"""


# FASMBC_EUR
# Monetary, Central Bank Survey, Monetary Base, Currency In Circulation, Euros


import pandas as pd
import requests
import numpy as np
import datetime as dt
from iso3166 import countries
import string
import json

initial_dt=dt.datetime.now()
print(initial_dt)

initial_date=dt.date.today()
str_date=dt.datetime.strftime(initial_date,"%Y%m%d")

print(str_date)


url_structure = 'http://dataservices.imf.org/REST/SDMX_JSON.svc/DataStructure/IFS'
data = requests.get(url_structure).json()
data_codelist = [x['@codelist'] for x in data['Structure']['KeyFamilies']['KeyFamily']['Components']['Dimension']]

url_codelist = "http://dataservices.imf.org/REST/SDMX_JSON.svc/CodeList/"
code_codelist = data_codelist[2]
data_request = requests.get(url_codelist + code_codelist).json()


dict_indicator={}
for code in data_request['Structure']['CodeLists']['CodeList']['Code']:
    #print(code)
    #indicatorの値
    val=code['@value']
    #indicatorの説明text
    txt=code['Description']['#text']
    dict_indicator[val]=txt
    #data_output.append((val,txt))
#df_indicator = pd.DataFrame(data_output,columns=['indicator','description'])
#print(dict_indicator)

#AMQ
def get_indicator():
    test_alpha="M"
    print("##### "+test_alpha+" #####")
    api_url = f"http://dataservices.imf.org/REST/SDMX_JSON.svc/CompactData/IFS/{test_alpha}.JP"
    data = requests.get(api_url).json()
    #print(type(data))
    #repn=0
    dict_output={}
    for item in data["CompactData"]["DataSet"]["Series"]:
        #print(type(val))
        val_indicator=item["@INDICATOR"]
        if dict_indicator[val_indicator]:
            dict_output[val_indicator]=dict_indicator[val_indicator]
        
        #repn+=1
        #print("#"*10)
        #print(repn)
        
    print(dict_output)
    df_output=pd.DataFrame(dict_output,index=["a"])
    df_output.T.to_csv("Indicators_by_Country\\test_list_1.csv")
    #df=pd.DataFrame(data["CompactData"])
    #df=pd.DataFrame(data["CompactData"]["DataSet"]["Series"])
    #print(df.iloc[0,1])
    #print(len(df.iloc[0,1]))
    #df.to_csv("Indicators_by_Country\\test_list.csv")

get_indicator()

"""

def list_indicators(period_symbol,country_code):
    dict_indicators={}

    base_url = "http://dataservices.imf.org/REST/SDMX_JSON.svc/CompactData/"
    
    for i in period_symbol:
        temp_url = base_url+f"IFS/{i}.{country_code}"
        ex=""
        try:
            data = requests.get(temp_url).json()
            #print(data)
            #print(data['CompactData']['DataSet']['Series']['Obs'])
        except Exception as e:
            #print(country_code+"失敗")
            ex=e
            if e=="":                
                print(ex)
                dict_indicators[period_symbol]=data['CompactData']['DataSet']['Series']['Obs']["@INDICATOR"]
            print(dict_indicators)
            
        #df_temp=pd.DataFrame(dict_temp,index=[country_code])
        #df_temp.to_csv(f"CSV_Store\\data_FPECS_IX_{country_code}_{str_date}.csv")
    #print(dict_indicators)

rep=0
period_symbol=["A","M","Q"]
alpha=string.ascii_uppercase
for i in range(len(alpha)):
    for j in range(len(alpha)):
        #print(alpha[i]+alpha[j])
        var_alpha2=alpha[i]+alpha[j]
        rep+=1
        list_indicators(period_symbol,var_alpha2)
    
    country_name=""
    #if country_code!="World":
    #    country_name=countries.get(country_code)[0]
    #else:
    #    pass
"""

print(initial_dt)
print("から")
print(dt.datetime.now())

