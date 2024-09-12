#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from bs4 import BeautifulSoup
import requests
import time
import datetime
import smtplib


# In[ ]:


url = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"

page = requests.get(url)

soup = BeautifulSoup(page.text,"html")
print(soup)


# In[ ]:


table = soup.find_all("table")[1]
print(table)


# In[ ]:


world_titles = table.find_all('th')


# In[ ]:


world_titles


# In[ ]:


world_table_titles = [title.text.strip() for title in world_titles]
print(world_table_titles)


# In[ ]:


get_ipython().system('pip install pandas')


# In[ ]:


import pandas as pd


# In[ ]:


df = pd.DataFrame(columns = world_table_titles)

df


# In[ ]:


column_data = table.find_all('tr')
print(column_data)


# In[ ]:


for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    
    length = len(df)
    df.loc[length] = individual_row_data


# In[ ]:


df


# In[ ]:


df.to_csv(r'C:\Users\archanasundar\Desktop\companies.csv',index= False)


# In[ ]:




