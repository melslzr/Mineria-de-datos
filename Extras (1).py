#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import json


# In[3]:


# Csv de asilos anuales
an = pd.read_csv("C:/Users/maria/Downloads/archive/asylum_seekers.csv")


# In[19]:


an.rename(columns = {'decisions_recognized':'dr'})


# In[18]:



an.rename(columns = {'Applied during year':'ap'})


# In[20]:


data_frame.year.astype("float")
data_frame.ap.astype("float")
data_frame.dr.astype("float")


# In[9]:


an[an['year'] < 2020].sample(100).plot.scatter(x='Applied during year', y='decisions_recognized')


# In[ ]:




