#!/usr/bin/python
#
#

import glob
import os
import sys
import re
import csv
import pandas as pd


#using dictionary method
Month_x={} 
Date_x={} 
Hour_x={}
Minute_x={}
Second_x={}
all_date={}

def filebrowser(ext=""):
    "Returns files with an extension"
    return [f for f in glob.glob(f"*{ext}")]
    #return [f for f in glob.glob("*")]

x = filebrowser(".jpg")
#new_x=x[1].split('.jpg')
for i in range(len(x)):
    start = x[i].find('-')-4
    end = x[i].find('-', start)-2
    Month_x[i]=x[i][start:end]

    start = x[i].find('-')-2
    end = x[i].find('-', start)
    Date_x[i]=x[i][start:end]
    
#    Date_x[i]=re.sub(r'.*2020(.*)-.*', r'\1', x[i])

    start = x[i].find('-')+1
    end = x[i].find('.jpg', start)-4
    Hour_x[i]=x[i][start:end]

    start = x[i].find('-')+3
    end = x[i].find('.jpg', start)-2
    Minute_x[i]=x[i][start:end]

    start = x[i].find('-')+5
    end = x[i].find('.jpg', start)
    Second_x[i]=x[i][start:end]

#print(Date_x)    
#print(Hour_x)
#print(Minute_x)
#print(Second_x)

#w = csv.writer(open("output.csv", "w"))
#for key, val in Date_x.items():
#    w.writerow([key, val])
df_Month_x = pd.DataFrame(data=Month_x, index=['Month'])
df_Date_x = pd.DataFrame(data=Date_x, index=['Date'])
df_Hour_x = pd.DataFrame(data=Hour_x, index=['Hour'])
df_Minute_x = pd.DataFrame(data=Minute_x, index=['Minute'])
df_Second_x = pd.DataFrame(data=Second_x, index=['Second'])

df_Month_x = (df_Month_x.T)
df_Date_x = (df_Date_x.T)
df_Hour_x = (df_Hour_x.T)
df_Minute_x = (df_Minute_x.T)
df_Second_x = (df_Second_x.T)

#df_Month_x.to_excel('output_0.xlsx')
#df_Date_x.to_excel('output_1.xlsx')
#df_Hour_x.to_excel('output_2.xlsx')
#df_Minute_x.to_excel('output_3.xlsx')
#df_Second_x.to_excel('output_4.xlsx')

all_data = pd.merge(df_Month_x, df_Date_x, left_index=True, right_index=True)
all_data = pd.merge(all_data, df_Hour_x, left_index=True, right_index=True)
all_data = pd.merge(all_data, df_Minute_x, left_index=True, right_index=True)
all_data = pd.merge(all_data, df_Second_x, left_index=True, right_index=True)
all_data['SUM'] = '2020'+'-'+all_data['Month']+'-'+all_data['Date']+' '+all_data['Hour']+':'+all_data['Minute']+':'+all_data['Second']
all_data.to_csv('all_data.csv')


