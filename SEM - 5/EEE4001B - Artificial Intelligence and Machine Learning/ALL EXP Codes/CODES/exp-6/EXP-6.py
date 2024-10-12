#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


# Data Preparation
x = np.array(([2, 9], [1, 5], [3, 6]), dtype=float)
y = np.array(([92], [86], [89]), dtype=float)

# Scale Units
x = x / np.amax(x, axis=0)
# Maximum test score = 100
y = y / 100

print(x)
print(y)


# In[3]:


# neural Network Class
class NeuralNetwork(object):
    def __init__(self):  # Fix the double underscores here
        # Parameters
        self.inputSize = 2
        self.outputSize = 1
        self.hiddenSize = 3
        # Weights
        self.W1 = np.random.randn(self.inputSize, self.hiddenSize)
        self.W2 = np.random.randn(self.hiddenSize, self.outputSize)

    def feedForward(self, X):
        self.z = np.dot(X, self.W1)
        self.z2 = self.sigmoid(self.z)

        self.z3 = np.dot(self.z2, self.W2)
        output = self.sigmoid(self.z3)
        return output

    def sigmoid(self, s, deriv=False):
        if deriv:
            return s * (1 - s)
        return 1 / (1 + np.exp(-s))

    def backward(self, X, y, output):
        self.output_error = y - output
        self.output_delta = self.output_error * self.sigmoid(output, deriv=True)
        self.z2_error = self.output_delta.dot(self.W2.T)
        self.z2_delta = self.z2_error * self.sigmoid(self.z2, deriv=True)

        # Update weights
        self.W2 += self.z2.T.dot(self.output_delta)
        self.W1 += X.T.dot(self.z2_delta)

    def train(self, X, y):
        output = self.feedForward(X)  # Fix the typo here
        self.backward(X, y, output)


# In[4]:


NN = NeuralNetwork()
for i in range(1000):  # trains the NN 1000 times
    if i % 100 == 0:
        print("Loss" + str(np.mean(np.square(y - NN.feedForward(x)))))  # Fix the typo here
    NN.train(x, y)


# In[5]:


## Final RESULT
print("Input: " + str(x))
print("Actual Output: " + str(y))
print("Loss: " + str(np.mean(np.square(y - NN.feedForward(x)))))
print("\n")
print("Predicted Output: " + str(NN.feedForward(x)))


# In[ ]:




