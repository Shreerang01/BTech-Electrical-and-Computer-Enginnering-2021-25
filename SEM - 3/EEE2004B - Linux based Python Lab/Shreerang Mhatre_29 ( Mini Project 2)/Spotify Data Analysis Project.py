#!/usr/bin/env python
# coding: utf-8

# # LBPL PROJECT- SPOTIFY DATA ANALYSIS 

# NAME: SHREERANG MHATRE 
# ROLLNO: 29
# BATCH: A2
# PRN: 1032211745

# ANALYSIS:-

# In[1]:


import numpy as np              # Importing Numpy Library
import pandas as pd             # Importing Pandas Library
import matplotlib.pyplot as plt # Importing Matplot Lib Library
import seaborn as sns           # Importing Seaborn Library


# # To get info of first 5 rows

# In[2]:


# Dataset Links: 
# Sourcce: Kaggle.com
# https://www.kaggle.com/datasets/zaheenhamidani/ultimate-spotify-tracks-db
# https://www.kaggle.com/datasets/lehaknarnauli/spotify-datasets?select=artists.csv


# In[3]:


df_tracks = pd.read_csv("D:/Datasets/tracks.csv") #This is the first dataset taken from kaggle.com
df_tracks.head() # To return the first five dataset


# # To check for null values

# In[4]:


pd.isnull(df_tracks).sum() 


# # Use of info method to get the detailed information about the dataset

# In[5]:


df_tracks.info()


# # To get the least popular songs from dataset

# In[6]:


sorted_df = df_tracks.sort_values('popularity', ascending = True).head(10) # use of sort_values fun for sorting
sorted_df


# # To get descriptive statistics from numerical values in dataset

# In[7]:


# Use of describe() & transpose() function
# Returns statistical output

df_tracks.describe().transpose()


# # To get the most popular songs which >90

# In[8]:


# use of query function from pandas
# inplace is not to change in dataset
most_popular = df_tracks.query('popularity>90', inplace = False).sort_values('popularity',ascending = False)
most_popular[:10] # use of slicing operator


# # To name first column to release_date using set_index function

# In[9]:


# here we have changed the first column name to release_date in the original data set
# use of index fun
df_tracks.set_index("release_date", inplace=True)
df_tracks.index=pd.to_datetime(df_tracks.index)
df_tracks.head()


# # To get the name of the artist at given row

# In[10]:


# use of iloc function to get details at a specific row

df_tracks[["artists"]].iloc[18]


# # To convert duration in miliseconds to seconds only

# In[11]:


# Use of lambda function to convert miliseconds into seconds

df_tracks["duration"]= df_tracks["duration_ms"].apply(lambda x: round(x/1000))
df_tracks.drop("duration_ms", inplace=True, axis=1)


# In[12]:


df_tracks.duration.head()


# # Data Visualization:-

# In[13]:


# A correlation map
# Droping unwanted columns
# using Pearson corelation method
# Using seaborn 'heatmap' for the map
# fmt string formatting quote
# cmap is 'sns colormap'

corr_df=df_tracks.drop(["key","mode","explicit"],axis=1).corr(method="pearson")
plt.figure(figsize=(14,6))
heatmap=sns.heatmap(corr_df,annot=True,fmt=".1g", vmin=-1, vmax=1, center=0, cmap="inferno", linewidth=1, linecolor="Black")
heatmap.set_title("Correlation HeatMap Between Variables")
heatmap.set_xticklabels(heatmap.get_xticklabels(), rotation=90)


# # Regression models of Loudness vs Energy

# In[14]:


sample_df = df_tracks.sample(int(0.004*len(df_tracks)))


# In[15]:


print(len(sample_df))  # 0.4% of the data set is 2346 rows


# In[16]:


# Regression map1 line between loudness and Energy

plt.figure(figsize=(10,6))
sns.regplot(data = sample_df, y = "loudness", x = "energy", color = "c").set(title = "Loudness Vs Energy Correleation")


# # Rgression model for Popularity Vs Acousticness 

# In[17]:


plt.figure(figsize=(10,6))
sns.regplot(data = sample_df, y = "popularity", x = "acousticness", color = "b").set(title = "Popularity Vs Acousticness Correleation")


# # Histograph for number of songs released per year

# In[18]:


df_tracks['dates']=df_tracks.index.get_level_values('release_date')
df_tracks.dates=pd.to_datetime(df_tracks.dates)
years=df_tracks.dates.dt.year


# In[19]:


#pip install --user seaborn==0.11.0


# In[20]:


sns.displot(years,discrete=True,aspect=2,height=5 ,kind="hist").set(title="Number of songs per year")


# # Barplot for duration of songs in diffrent years

# In[21]:


total_dr = df_tracks.duration
fig_dims = (18,7)
fig, ax = plt.subplots(figsize = fig_dims)
fig = sns.barplot(x = years, y = total_dr, ax = ax, errwidth = False).set(title="Year vs Duration")
plt.xticks(rotation=90)

# Downside is the list of 101 Text xticklabel objects


# # Lineplot for average duration of songs

# In[22]:


total_dr=df_tracks.duration
sns.set_style(style="whitegrid")
fig_dims = (10, 5)
fig, ax = plt.subplots(figsize=fig_dims)
fig=sns.lineplot(x=years, y=total_dr, ax=ax).set(title="Year vs Duration")
plt.xticks(rotation = 60)


# # Part2 of the Dataset

# In[23]:


df_genre=pd.read_csv("D:/Datasets/SpotifyFeatures.csv")


# In[24]:


df_genre.head()


# # Barplot for duration of songs in diffrent Genres

# In[25]:


plt.title("Duration of the Songs in Different Genres")
sns.color_palette("rocket", as_cmap= True)
sns.barplot(y='genre', x='duration_ms', data=df_genre)
plt.xlabel("Duration in milli seconds")
plt.ylabel("Genres")


# # Top 5 Genres by Popularity

# In[26]:


sns.set_style(style = "darkgrid")
plt.figure(figsize=(10,5))
famous = df_genre.sort_values("popularity", ascending = False).head(10)
sns.barplot(y='genre', x='popularity', data = famous).set(title= "Top 5 Genres by Populartiy")


# In[ ]:




