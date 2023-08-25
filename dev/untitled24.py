# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 10:20:38 2023

@author: taichi.mitsuhashi
"""

import pandas as pd
import requests
import numpy as np
from iso3166 import countries
import string
import json
import matplotlib.pyplot as plt
import datetime as dt

from translate import Translator
translator=Translator(from_lang="en",to_lang="ja")

initial_dt=dt.datetime.now()
print(initial_dt)
initial_date=dt.date.today()
str_date=dt.datetime.strftime(initial_date,"%Y%m%d")
print(str_date)

plt.style.use("ggplot")
plt.rcParams["figure.figsize"]=[12,9]
plt.rcParams["font.size"]=14

country_code="US"

#データ読み込み
df_indicator=pd.read_csv(f"list_indicator_{country_code}.csv",parse_dates=True)
process_length=len(df_indicator)
print(process_length)

df_mc_ETH=pd.read_csv("C:\\Users\\taichi.mitsuhashi\\.spyder-py3\\02_Data_Store\\CSV_Store_CMC\\data_cmc_ETH_mc_20230810.csv",index_col=0)
df_mc_ETH=df_mc_ETH.T
df_mc_ETH.index=pd.to_datetime(df_mc_ETH.index)
df_mc_ETH["ETH"]=df_mc_ETH["ETH"].replace('[\$,]', '', regex=True).astype(float)

x_data_ETH=list(df_mc_ETH.index)
y_data_ETH=list(df_mc_ETH["ETH"])
#print(type(y_data_ETH))

def create_plot(df,val_indicator,val_description):
    fig,ax1=plt.subplots()
    fig.suptitle(val_description)
    #IMFのデータ
    x_data=df["@TIME_PERIOD"]
    y_data=df["@OBS_VALUE"]
    ax1.plot(x_data,y_data,label=val_indicator)
    ax1.set_ylabel="imf"
    #IMFデータの凡例の情報
    hans1,labs1=ax1.get_legend_handles_labels()
    
    #CMCのデータ
    ax2=ax1.twinx()
    ax2.plot(x_data_ETH,y_data_ETH,label="market cap of ETH",color="c")    
    ax2.set_ylabel="cmc_ETH"
    #CMCデータの凡例の情報
    hans2,labs2=ax2.get_legend_handles_labels()

    #translated_description=translator.translate(val_description)
    #ax.set_title(translated_description,fontname="MS Gothic")
    ax1.set_xlabel("month")
    #ax.axvline(dt.datetime(2022,1,1),color="blue")
    #ax.axvline(dt.datetime(2023,1,1),color="blue")
    ax1.legend(hans1+hans2,labs1+labs2,loc="best")
    plt.show()


def get_imf_data(val_indicator,val_description):
    #periodは、A（年間）、M（月間）、Q（四半期）の3種類
    period="M"
    country_code="US"
    api_url = f"http://dataservices.imf.org/REST/SDMX_JSON.svc/CompactData/IFS/{period}.{country_code}."
    temp_url=str(api_url+val_indicator)
    try:
      json_data=requests.get(temp_url).json()
      obs=json_data['CompactData']['DataSet']['Series']['Obs']
      #print(type(obs))
      df=pd.DataFrame(obs)
      df["@TIME_PERIOD"]=pd.to_datetime(df["@TIME_PERIOD"])
      df["@OBS_VALUE"]=pd.to_numeric(df["@OBS_VALUE"])
      #print(type(df["@TIME_PERIOD"]))
      #print(df["@TIME_PERIOD"][10])
      #df=df.dropna()
      #print(val_description)
      #print(df["@TIME_PERIOD"])
      #print(df["@OBS_VALUE"])
      
      #関数呼び出し
      create_plot(df,val_indicator,val_description)
      #print(df)
      
    except Exception as e:
        if e!="":
          print(e)


#ループ実行
#print(len(df_indicator))
for i in range(len(df_indicator)):
    process_length-=1
    print(process_length)
    val_indicator=df_indicator.iloc[i,0]
    val_description=df_indicator.iloc[i,1]
    #if i>100:break
    #関数呼び出し
    get_imf_data(val_indicator,val_description)



print(initial_dt)
print("から")
print(dt.datetime.now())

