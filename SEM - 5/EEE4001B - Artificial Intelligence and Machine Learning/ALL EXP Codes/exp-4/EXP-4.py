#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
import sklearn.datasets


# In[4]:


iris = sklearn.datasets.load_iris()
iris_data = pd.DataFrame(iris.data, columns=iris.feature_names)
iris_data['class'] = iris.target
iris_data.head()


# In[5]:


iris_data.describe()


# In[6]:


iris_data.info()


# In[7]:


iris_data.isnull().sum()


# In[8]:


iris_data.corr()


# In[9]:


X = iris_data.drop('class',axis = 1)
Y = iris_data['class']
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test = train_test_split(X,Y, test_size=0.30)


# In[10]:


from sklearn.linear_model import LogisticRegression
model = LogisticRegression()


# In[11]:


model.fit(X_train, Y_train) #model training


# In[19]:


#print metric to get performance
print('Acuracy:', model.score(X_test, Y_test)*100)

