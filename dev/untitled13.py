# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 18:36:23 2023

@author: taichi.mitsuhashi
"""

from selenium import webdriver
from bs4 import BeautifulSoup as bs
import time
import chromedriver_binary
from selenium.webdriver.common.by import By
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
import matplotlib

initial_dt=dt.datetime.now()
initial_date=dt.date.today()
str_date=dt.datetime.strftime(initial_date,"%Y%m%d")
print(str_date)


options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

"""
#テスト用
list_yyyymmdd=[
    "20130505","20130512","20130519","20130526",
    "20130602","20130609","20130616","20130623","20130630",
    "20130707","20130714","20130721","20130728",
    "20130804","20130811","20130818","20130825",
    "20130901","20130908","20130915","20130922","20130929",
    "20131006","20131013","20131020","20131027",
    "20131103","20131110","20131117","20131124",
    "20131201","20131208","20131215","20131222","20131229"
    ]

"""

"""
list_yyyymmdd=[
    "20230604","20230611","20230618","20230625",
    "20230709","20230716","20230723","20130730",
    "20230806"
    ]
"""

#最初のスクレイピングで、提供されている日付を取得
list_yyyymmdd=[]
initial_url="https://coinmarketcap.com/historical/"
driver.get(initial_url)
initial_html = driver.page_source
initial_soup = bs(initial_html,'html.parser')

for elem_link in initial_soup.find_all("a",class_="historical-link cmc-link"):
    #print(elem_link["href"])
    i_date=elem_link["href"]
    i_date=i_date[12:20]
    #print(i_date)
    if i_date!="20130428":
        list_yyyymmdd.append(i_date)



def get_annual_data(list_yyyymmdd):
    print("a")
    temp_url="https://coinmarketcap.com/historical/"
    #market cap用
    dic_summary_mc={}
    list_row_mc=[]
    #circulating supply用
    dic_summary_cs={}
    list_row_cs=[]
    
    list_i_date_str=[]
    
    for i_date in list_yyyymmdd:
        
        driver.get(temp_url+i_date)

        i_date_dt=dt.datetime.strptime(i_date,"%Y%m%d")
        i_date_str=dt.datetime.strftime(i_date_dt,"%Y-%m-%d")
        list_i_date_str.append(i_date_str)
        #
        dic_summary_mc={"timestamp":i_date_str}
        dic_summary_cs={"timestamp":i_date_str}
        
        #スクレイピング先のページ情報の取得
        #driver.implicitly_wait(5)
        
        #loaded_item = driver.execute_script("return document.getElementsByClassName('cmc-historical-detail__table-footer')")
        #driver.implicitly_wait(500)
        #driver.execute_script("document.getElementsByClassName('cmc-historical-detail__table-footer')[%d].scrollIntoView(true)" % int(len(loaded_item)-1))        
        #driver.implicitly_wait(500)
        #for i in range(1,1000):
        #    print(i)
        #    driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
        #driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
        
        #driver.execute_script("return document.getElementsByClassName('cmc-historical-detail__table-footer')")
        #driver.implicitly_wait(500)
        #driver.execute_script("window.scrollBy(0, 1000);")
        #driver.implicitly_wait(500)
        
        ###########################
        initial_height=driver.execute_script("return window.innerHeight")
        initial_top=1
        while True:
            present_bottom=driver.execute_script("return document.body.scrollHeight")
            present_top=initial_top
            while present_top<present_bottom:
                present_top+=int(initial_height*0.8)
                driver.execute_script("window.scrollTo(0,%d)" % present_top)
                driver.implicitly_wait(1)
                
                
                loadmore_button=driver.execute_script("return document.getElementsByClassName('cmc-table-listing__loadmore')")
                print(loadmore_button)
                """
                if loadmore_button!=[]:
                    present_height=driver.execute_script("return document.body.scrollHeight")
                    driver.execute_script("document.getElementsByClassName('cmc-table-listing__loadmore')[0].click()")
                    driver.implicitly_wait(1)
                    
                    #下記のtimeoutを回避する必要がある
                    #TimeoutException: timeout: Timed out receiving message from renderer: 300.000
                    #  (Session info: headless chrome=115.0.5790.171)
                    sw=0
                    while sw<10:
                        if driver.execute_script("return document.body.scrollHeight")>present_height:
                            #print(loadmore_button)
                            driver.execute_script("document.getElementsByClassName('cmc-table-listing__loadmore')[0].click()")
                            driver.implicitly_wait(1)
                            sw+=1
                """
            driver.implicitly_wait(1)
            latest_bottom=driver.execute_script("return document.body.scrollHeight")
            
            #
            if present_bottom==latest_bottom:
                break
        
        ###########################
        

        html = driver.page_source
        soup = bs(html,'html.parser')
        #html_elements=[]
        for elem_table in soup.find_all("table"):
            for elem_tr in elem_table.find_all("tr",class_="cmc-table-row"):
                val_symbol=""
                val_market_cap=""
                val_circulating_supply=""
                for elem_td_sy in elem_tr.find_all("td",class_="cmc-table__cell--sort-by__symbol"):
                    for s in elem_td_sy.contents[0]:
                        val_symbol=s
                for elem_td_mc in elem_tr.find_all("td",class_="cmc-table__cell--sort-by__market-cap"):
                    for mc in elem_td_mc.contents[0]:
                        val_market_cap=mc
                        dic_summary_mc[val_symbol]=val_market_cap
                for elem_td_cs in elem_tr.find_all("td",class_="cmc-table__cell--sort-by__circulating-supply"):
                    val_circulating_supply=elem_td_cs.get_text()
                    dic_summary_cs[val_symbol]=val_circulating_supply
                    """
                    for cs in elem_td_cs.contents:
                        #cs.replace("<div>","")
                        #cs.replace("</div>","")
                        print(cs.type)
                        print(len(cs))
                        val_circulating_supply=cs
                        dic_summary_cs[val_symbol]=val_circulating_supply
                        """
        
        list_row_mc.append(dic_summary_mc)
        list_row_cs.append(dic_summary_cs)
        
    
    df_mc=pd.DataFrame(list_row_mc,index=list_i_date_str)
    df_mc=df_mc.T
    num_index_mc=len(df_mc.index)
    df_mc=df_mc[df_mc.index[1]:df_mc.index[num_index_mc-1]]
    df_mc.to_csv(f"CSV_Store_CMC\\data_cmc_marketcap_{str_date}.csv")
    
    df_cs=pd.DataFrame(list_row_cs,index=list_i_date_str)
    df_cs=df_cs.T
    num_index_cs=len(df_cs.index)
    df_cs=df_cs[df_cs.index[1]:df_cs.index[num_index_cs-1]]
    df_cs.to_csv(f"CSV_Store_CMC\\data_cmc_circulatingsupply_{str_date}.csv")
    
    #print(len(df_mc.index))
    
    #dfからcsvとpngを改めて作成
    for val_symbol in df_mc.index:
        if val_symbol!="timestamp":
        #if val_symbol=="BTC":
            df_mc.loc[[val_symbol]].to_csv(f"CSV_Store_CMC\\data_cmc_{val_symbol}_mc_{str_date}.csv")
            
            list_x=df_mc.columns
            print("list_x****************")
            print(list_x)
            print(list_x[0])
            list_y=[]
            for val in df_mc.loc[val_symbol]:
                if type(val)!="float" and type(val)!="int":
                    val=str(val).replace("$","")
                    val=str(val).replace(",","")
                    list_y.append(float(val))
                else:
                    list_y.append(val)
            print("list_y****************")
            print(list_y)
            print(list_y[0])
            
            fig,ax=plt.subplots()
            
            ax.xaxis.set_major_locator(ticker.LinearLocator(10))
            ax.plot(list_x,list_y,"d")
            ax.tick_params(axis="x",labelrotation=90)
            ax.set_title(f"Fig_{val_symbol}")
            
            ax.set_xlabel("date")
            ax.set_ylabel("Market Cap(USD)")
            
            """
            plt.plot(list_x,list_y)
            
            plt.title(f"Fig_{val_symbol}")
            plt.xlabel("date")
            plt.ylabel("Market Cap(USD)")
            plt.xticks(rotation=90)
            """
            plt.savefig(f"Image_Store_CMC\\fig_cmc_{val_symbol}_mc_{str_date}.png")
            plt.show()
            
            
    
    
    #処理時間
    print(initial_dt)
    print(dt.datetime.now())
    

get_annual_data(list_yyyymmdd)




