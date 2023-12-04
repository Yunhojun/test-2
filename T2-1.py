#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


import pandas as pd


# In[3]:


from pandas import Series, DataFrame


# In[4]:


import csv


# In[5]:


data = pd.read_csv('2019_kbo_for_kaggle_v2.csv', encoding='UTF-8')


# In[6]:


list1 = ['H','avg','HR','OBP']


# In[7]:


years = [2015, 2016, 2017, 2018]
for y in years:
    frame1 = pd.DataFrame(columns=list1)
    for i in list1:
        frame1[i] = data[data.year == y].sort_values(i, ascending=False).iloc[:10, 0].values
    print("\n1-", y-2014, ") Top 10 players in ", y, sep="")
    print(frame1)


# In[8]:


list2 = ['포수', '1루수', '2루수', '3루수', '유격수', '좌익수', '중견수', '우익수']


# In[9]:


frame2 = pd.DataFrame(columns=list2)
for i in list2:
    frame2[i] = data[(data.cp == i) & (data.year == 2018)].sort_values('war', ascending=False).iloc[:1, 0].values


# In[10]:


print("\n2) The player with highest war by cp.")
print(frame2)


# In[11]:


import pandas_datareader.data as web


# In[12]:


list3 = ['R', 'H', 'HR', 'RBI', 'SB', 'war', 'avg', 'OBP', 'SLG']


# In[13]:


frame3 = pd.DataFrame(columns=list3)
for i in list3:
    frame3[i] = data[i]


# In[14]:


print("\n3-1) Correlations with salary")
print(frame3.corrwith(data.salary))


# In[15]:


print("\n3-2) The highest correlation with salary")
print(frame3.corrwith(data.salary).sort_values(ascending=False)[:1])

