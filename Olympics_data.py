#!/usr/bin/env python
# coding: utf-8

# In[18]:


#importing pandas
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[21]:


athletes =   pd.read_csv('athlete_events.csv')#reading csv using pandas
region   =   pd.read_csv('noc_regions.csv')


# In[4]:


athletes.head()#showing head of dataframe


# In[22]:


region.head()


# In[24]:


#combining athlete and region data frame
athlete_merge = athletes.merge(region,how = 'left',on ='NOC')


# In[26]:


athlete_merge.head()


# In[28]:


#Checking the number of records
athlete_merge.shape


# In[32]:


#Renaming Column names
athlete_merge.rename(columns={'region':'Region','notes':'Notes'},inplace=True)


# In[33]:


athlete_merge.head()


# 

# In[35]:


athlete_merge.info()


# In[36]:


#statistical info using describe
athlete_merge.describe()


# In[42]:


# check which column  has null values(not needed)
null_value   = athlete_merge.isna()
null_columns = null_value.any()
null_columns


# In[43]:


#calculating the number of null values on each column
athlete_merge.isnull().sum()


# In[51]:


#Details of specific country
athlete_merge.query('Team == "India"').head()


# In[59]:


#top 20 countries 
top_20_countries = athlete_merge.Team.value_counts().sort_values(ascending=False).head(20)


# In[60]:


top_20_countries


# In[65]:


# Bar plot
plt.figure(figsize=(24,6))
plt.title('Top participants in Olympics')
sns.barplot(x=top_20_countries.index,y=top_20_countries,palette = 'Set1')


# In[88]:


#Age Distribution of athletes
plt.figure(figsize=(12,6))
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('No. of Participants')
plt.hist(athlete_merge.Age, bins = np.arange(10,80,2),edgecolor = 'Black');


# In[93]:


#Gender Distribution
gender_count = athlete_merge.Sex.value_counts()
gender_count


# In[104]:


#pie chart for gender distribution
plt.figure(figsize=(24,6))
plt.title('Gender Distribution')
plt.pie(gender_count,labels=gender_count.index,startangle = 90,autopct = '%1.f%%')


# In[107]:


#Total medal count
athlete_merge.Medal.value_counts()


# In[136]:


WomenInOlympics = athlete_merge[(athlete_merge.Sex=='F')&(athlete_merge.Season=='Summer')]


# In[137]:


#women participation
sns.set(style="darkgrid")
plt.figure(figsize=(20,10))
sns.countplot(x='Year',data=WomenInOlympics,palette="Spectral")
plt.title('Women Participation')


# In[128]:


#Female athletes in olympics
female_athlete= athlete_merge[(athlete_merge.Sex == 'F') & (athlete_merge.Season == 'Winter')][['Sex','Year']]
female_athlete=female_athlete.groupby('Year').count().reset_index()
female_athlete


# In[147]:


#gold beyond 40
athlete_gold = athlete_merge[(athlete_merge.Sex == 'M') &  (athlete_merge.Medal == 'Gold')]
athlete_gold


# In[149]:


#gold medal above  the age of 40
gold_40 = athlete_gold[(athlete_gold.Age>=40)]
gold_40


# In[ ]:




