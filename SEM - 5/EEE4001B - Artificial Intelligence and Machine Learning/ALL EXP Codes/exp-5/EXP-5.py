#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install scikit-learn


# In[2]:


import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split  # Add this import
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt


# In[3]:


data= pd.read_excel('C:/Users/SHREERANG/Desktop/AIML/CODES/Expt-5 DataSheet.xlsx')


# In[4]:


data.describe()


# In[5]:


data.head()


# In[6]:


x = data.drop(['PE'], axis=1).values
y = data['PE'].values

# Display the features and target variable
print("Features (x):")
print(x)
print("Target variable (y):")
print(y)

# Split the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.30, random_state=0)

# Create a Linear Regression model
ml = LinearRegression()

# Fit the model on the training data
ml.fit(x_train, y_train)

# Make predictions on the test data
y_pred = ml.predict(x_test)
print("Predictions on the test data:")
print(y_pred)

# Make a prediction for a specific input
specific_input = [[14.96, 41.7, 1024.07, 73.17]]
prediction = ml.predict(specific_input)
print("Prediction for specific input:")
print(prediction)

# Evaluate the model using R-squared (R2) score
r2 = r2_score(y_test, y_pred)
print("R-squared (R2) score:")
print(r2)

# Create a scatter plot to visualize the model's predictions
plt.figure(figsize=(15, 10))
plt.scatter(y_test, y_pred)
plt.xlabel('Actual')
plt.ylabel('Predicted')
plt.title('Actual Vs Predicted')

# Create a DataFrame to display the actual values, predicted values, and the difference
pred_y_df = pd.DataFrame({'Actual Value': y_test, 'Predicted Value': y_pred, 'Difference': y_test - y_pred})
print("Sample of actual vs. predicted values:")
print(pred_y_df.head(15))


# In[ ]:




