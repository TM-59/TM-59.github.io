# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 18:20:08 2023

@author: taichi.mitsuhashi
"""

# FASMBC_XDR
# Monetary, Central Bank Survey, Monetary Base, Currency In Circulation, Domestic Currency

import pandas as pd
import requests
import matplotlib.pyplot as plt
import string
import numpy as np
import datetime as dt
from iso3166 import countries

import matplotlib.dates as mdates
import matplotlib.ticker as ticker
import matplotlib

initial_dt=dt.datetime.now()
print(initial_dt)

initial_date=dt.date.today()
str_date=dt.datetime.strftime(initial_date,"%Y%m%d")

print(str_date)

###################################
# create_new_dict()と全く同じ
dic_summary={}
"""
list_year=[y for y in range(1995,2023+1)]
#print(list_year)
list_month=[m for m in range(1,12+1)]
#print(list_month)

str_nm=""
for a in list_year:
    for b in list_month:
        str_nm=str(a)+"-"+str(b).zfill(2)
        #print(str_nm)
        # あらかじめnull回避のdictionary作成
        # dic_summary={{"2000-01":0},{"2020-01":0}}
        dic_summary[str_nm]=0
#print(dic_summary)
"""
###################################
"""
# 上と同じ
def create_new_dict():
    dic_summary={}
    list_year=[y for y in range(1995,2023+1)]
    #print(list_year)
    list_month=[m for m in range(1,12+1)]
    #print(list_month)
    
    str_nm=""
    for a in list_year:
        for b in list_month:
            str_nm=str(a)+"-"+str(b).zfill(2)
            #print(str_nm)
            dic_summary[str_nm]=0
    
    #print(dic_summary)
    return dic_summary

#print(data_iso[100])
"""
###################################
# IMFデータを取得し、それを整形し、dic_summaryを作成
def get_dict_of_country(country_code):
    api_url = "http://dataservices.imf.org/REST/SDMX_JSON.svc/CompactData/"
    col_df = []
    temp_url = api_url+"IFS/M."+country_code+".FASMBC_XDC"
    #print(temp_url)
    ex=""
    try:
        #temp_url
        # "http://dataservices.imf.org/REST/SDMX_JSON.svc/CompactData/IFS/M.JP.FASMBC_XDC"
        # "http://dataservices.imf.org/REST/SDMX_JSON.svc/CompactData/IFS/M.ZW.FASMBC_XDC"
        data = requests.get(temp_url).json()
        #print(data['CompactData']['DataSet']['Series']['Obs'])
        # "JP"のcol_df
        # {"@TIME_PERIOD":{"2000-01","2020-11"},"@OBS_VALUE":{0,12345678}}
        col_df=pd.DataFrame(data['CompactData']['DataSet']['Series']['Obs'])
        #col_df.append(pd.DataFrame(data))
        #print(col_df)
    except Exception as e:
        #print(country_code+"失敗")
        ex=e
        
    #辞書を初期化
    #dic_summary=create_new_dict()
    #dic_summary={"country":country_code}
    
    ex_2=""
    if ex=="":
        if len(col_df["@TIME_PERIOD"])>0:
            dic_summary={"country":country_code}
            for k in range(len(col_df["@TIME_PERIOD"])):
                try:
                    #dic_summary[col_df["@TIME_PERIOD"][k]]+=0
                    #print("ok")
                    print("TIME_PERIOD精査中")
                except KeyError as e2:
                    print("KeyError",e2)
                    ex_2=e2
                
                if ex_2=="":
                    dic_summary[col_df["@TIME_PERIOD"][k]]=float(col_df["@OBS_VALUE"][k])
                    #print("success")
                    
                #print(dic_summary)
                #x=col_df["@TIME_PERIOD"]
                #y=col_df["@OBS_VALUE"]
                #list_dic.append(dic_summary)
            return dic_summary
    #return [x,y]
    #return dic_summary

###################################
"""
# 作成されたdic_summary={{"2000-01":0},{"2020-01":0}}で、全て0であれば、sum=0
# 作成されたdic_summary={{"2000-01":0},{"2020-01":12345678}}で、全て0でなければ、sum>0
def return_sum(dic_summary):
    #初期化
    sum = 0
    for i in dic_summary: 
        sum = sum + dic_summary[i]
    return sum
"""
###################################
"""
# テスト用
# dic_summaryから、グラフのみ表示する
def create_graph(dic_summary):
    x=[]
    y=[]
    for key, val in dic_summary.items():
        x.append(key)
        y.append(val)
    
    #print(x)
    #print(y)
    
    fig=plt.figure()
    axes=plt.axes()
    #axes.set_ylim([0,500])
    
    plt.plot(x,y)
    
    plt.xlabel("year and month")
    plt.ylabel("Monetary, Central Bank Survey, Monetary Base, Currency In Circulation, Domestic Currency")
    
    label_x=[]
    for i in range(len(x)):
      if i%10==0:
        label_x.append(x[i])
      else:
        label_x.append("")
    plt.xticks(x,label_x,rotation=90)
    
    label_y=[]
    for i in range(len(y)):
      if i%10==0:
        label_y.append(y[i])
      else:
        label_y.append("")
    plt.yticks(y,label_y)
    #print(label_y)
    #print(y)
    
    #xmin,xmax,ymin,ymax
    #plt.axis(["","",0,""])
    #plt.ylim(bottom=0,top=200)
    
    plt.show()
"""

rep=0
list_country=[]
list_dic=[]

#dic_df_summary={"World":create_new_dict()}
alpha=string.ascii_uppercase
for i in range(len(alpha)):
    for j in range(len(alpha)):
        #print(alpha[i]+alpha[j])
        var_alpha2=alpha[i]+alpha[j]
        #dic_summary=get_dict_of_country(var_alpha2)
        list_country.append(var_alpha2)
        list_dic.append(get_dict_of_country(var_alpha2))
        
        """
        if return_sum(dic_summary)>0:
            #create_graph(dic_summary)
            rep+=1
            dic_df_summary[var_alpha2]=dic_summary
            for key_p,key_q in dic_summary.items():
                dic_df_summary["World"][key_p]+=float(key_q)
                print(rep)
            #list_country.append(var_alpha2)
            #print(var_alpha2)
        """


df_test=pd.DataFrame(list_dic,index=list_country)
for c in list_country:
    print("****************")
    print(c)
    print(df_test.loc[c])
    df_test2=pd.DataFrame(df_test.loc[c])
    #df_test2.to_csv(f"CSV_Store\\data_{c}_test.csv")


#df_test.to_csv("CSV_Store\\data_test.csv")


#for test20230803
#dic_df_summary={}
#dic_summary=get_dict_of_country("JP")
#dic_df_summary["JP"]=dic_summary

###################################
"""
# 本番用
# dic_summaryから、csvとpngを作成し保存し、グラフを表示する

# dic_df_summary:{{"JP":get_dict_of_country("JP")},{"ZW":get_dict_of_country("ZW")}}
# key:"JP","ZW"
# val:get_dict_of_country("JP")={{"2000-01":"0"},{"2020-11":"12345678"}}
for key, val in dic_df_summary.items():
    country_code=key
    dict_temp=val
    x2=[]
    y2=[]
    # dic_temp:{{"2000-01":"0"},{"2020-11":"12345678"}}
    # key2:"2000-01","2020-11"
    # val2:0,12345678
    for key2, val2 in dict_temp.items():
        x2.append(key2)
        y2.append(val2)
    
    df_temp=pd.DataFrame(dict_temp,index=[country_code])
    #df_temp.to_csv(f"CSV_Store\\data_{country_code}_{str_date}.csv")
    
    
    fig,ax=plt.subplots()
    
    ax.xaxis.set_major_locator(ticker.LinearLocator(10))
    ax.plot(x2,y2,"d")
    ax.tick_params(axis="x",labelrotation=90)
    
    ax.set_xlabel("year and month")
    ax.set_ylabel("Monetary, Central Bank Survey, Monetary Base, Currency In Circulation, Domestic Currency")
    
    country_name=""
    if country_code!="World":
        country_name=countries.get(country_code)[0]
    else:
        country_name=country_code
    
    df_temp.to_csv(f"CSV_Store\\data_{country_name}_{str_date}.csv")
    
    ax.set_title(f"Fig_{country_name}")        


    plt.plot(x2,y2)
    
    plt.xlabel("year and month")
    country_name=""
    if country_code!="World":
        country_name=countries.get(country_code)[0]
    else:
        pass
    if country_name!="":
        plt.title(f"Fig of FASMBC_{country_name}")
    else:
        plt.title(f"Fig_{country_code}")
        
    plt.ylabel("Monetary, Central Bank Survey, Monetary Base, Currency In Circulation, Domestic Currency")
    
    label_x=[]
    for i in range(len(x2)):
      if i%10==0:
        label_x.append(x2[i])
      else:
        label_x.append("")
    plt.xticks(x2,label_x,rotation=90)
    
    label_y=[]
    for i in range(len(y2)):
      if i%10==0:
        label_y.append(y2[i])
      else:
        label_y.append("")
    plt.yticks(y2,label_y)
    #print(label_y)
    #print(y)
    
    #xmin,xmax,ymin,ymax
    #plt.axis(["","",0,""])
    #plt.ylim(bottom=0,top=200)

    plt.savefig(f"Image_Store\\fig_{country_name}_{str_date}.png")
    plt.show()


#print(rep)

print(initial_dt)
print("から")
print(dt.datetime.now())

#print(list_country)

#for simple test
#dic_summary=get_dict_of_country("JP")
#if return_sum(dic_summary)>0:
#    create_graph(dic_summary)

#dic_summary=get_dict_of_country("US")
#if return_sum(dic_summary)>0:
#    create_graph(dic_summary)
"""
