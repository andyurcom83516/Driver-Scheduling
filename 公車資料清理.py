# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 16:34:08 2020

@author: user
"""
from pandas import Timestamp
import pandas as pd
import numpy as np
import datetime
import time
import calendar

#%%
file = pd.read_csv(r"D:\Desktop\bus data\168east\168east_rawdata.csv")
file = pd.DataFrame(file)

file['on_time'] = file['on_time'].astype('str')
file['on_date'] = file['on_date'].astype('str')
file['on_stop'] = file['on_stop'].astype('str')
file['on_time'] = file['on_time'].apply(lambda x:x.zfill(6))

file['on_Hour']=file['on_time'].apply(lambda x:x[:2])
file['on_Minute']=file['on_time'].apply(lambda x:x[2:4])
file['on_time']=file['on_Hour']+file['on_Minute']+file['on_stop']


file['on_time'] = file['on_time'].apply(lambda x:on_time_cal(x))
#%%
file['on_date'] = pd.to_datetime(file['on_date'],format='%Y-%m-%d')


file['Day of Week'] = file['on_date'].apply(lambda time: time.dayofweek)
file['Day of Week'] = file['Day of Week'].astype('str')
dmap = {'0':'weekday','1':'weekday','2':'weekday','3':'weekday','4':'weekday','5':'weekend','6':'weekend'}
file['Day of Week'] = file['Day of Week'].map(dmap)

#%%

weekend_list = [Timestamp('2019-09-13 00:00:00') , Timestamp('2019-10-10 00:00:00') , Timestamp('2020-01-01 00:00:00') , Timestamp('2020-01-24 00:00:00'), Timestamp('2020-01-25 00:00:00') , Timestamp('2020-01-26 00:00:00') , Timestamp('2020-01-27 00:00:00') , Timestamp('2020-01-28 00:00:00') , Timestamp('2020-01-29 00:00:00'), Timestamp('2020-01-30 00:00:00') , Timestamp('2020-01-31 00:00:00') , Timestamp('2020-02-28 00:00:00') , Timestamp('2020-04-02 00:00:00') , Timestamp('2020-04-03 00:00:00'), Timestamp('2020-06-25 00:00:00') , Timestamp('2020-06-26 00:00:00')]
file.loc[file['on_date'].isin(weekend_list) == True,'Day of Week'] = 'weekend'

#%%

df1 = pd.pivot_table(file,index=['on_time'],columns=['Day of Week'],fill_value = 0, aggfunc='count') 

#%%
df1.to_excel("168east.xlsx")


#%%
def on_time_cal(x):
    if len(x) == 5:
        time = int(x[:4])
        stop = int(x[-1])
        
    else:
        time = int(x[:4])
        stop = int(x[-2:])
    
    time = int(time)
    stop = int(stop)
    
    num = 1.46
    
    spend = int(round(num * stop,0))
    
    h = time // 100
    m = time % 100
    
    while m - spend < 0:
        h = h - 1
        m = m + 60
        
    m = m - spend
    
    ans = str(h)+str(m).zfill(2)
    
    return ans