#!/usr/bin/env python
# coding: utf-8

# In[27]:


import random
class Environment(object):
    def __init__(self): 
        self.locationcondition={'A' : '1' , 'B' :'1'}
        self.locationcondition['A']=random.randint(0,1) 
        self.locationcondition['B']=random.randint(0,1)


# In[28]:


class Sreflexagent(Environment):
    def __init__(self,Environment):
        #place vacuum at random location
        print(Environment.locationcondition) 
        vacuumlocation=random.randint(0,1)
        
        if vacuumlocation==0:
            print("vacuum is randomly placed at locationn A") 
            #and if location A is dirty
            if Environment.locationcondition['A']==1: 
                print("Location A is dirty")
                #suck the dirt and mark it clean
                Environment.locationcondition['A']=0 
                print("Location A has been cleaned") 
                vacuumlocation=1
                
        else:
            print("Location A is clean") #move to B
            print("moving to location B") 
            vacuumlocation=1
            if Environment.locationcondition['B']==1:
                #suck the dirt and mark it clean 
                Environment.locationcondition['B']=0 
                print("Location B has been cleaned")
            
            elif vacuumlocation==1:
                print("vacuum is randomly placed at locationn B")
                #and if location B is dirty
            else:
                print("Location B is clean") 
                #and if location B is dirty
                
                
            if Environment.locationcondition['B']==1: 
                print("Location B is dirty")
                #suck the dirt and mark it clean Environment.
                Environment.locationcondition['B']=0; 
                print("Location B has been cleaned")
                print("moving to location A")
                vacuumlocation=0
            else:
                print("Location B is Clean") 
                #Move to A
                print("moving to location A") 
                vacuumlocation=0
                
                
            if vacuumlocation==0:
                if Environment.locationcondition['A']==1: 
                    print("Location A is dirty")
                    #suck the dirt and mark it clean 
                    Environment.locationcondition['A']=0; 
                    print("Location A has been cleaned")
            else:
                print("Location A is Clean")
        
                


# In[29]:


obj= Environment()


# In[30]:


agent=Sreflexagent(obj)


# In[34]:


agent=Sreflexagent(obj)


# In[43]:


agent=Sreflexagent(obj)


# In[ ]:




