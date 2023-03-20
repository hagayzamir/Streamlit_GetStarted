#!/usr/bin/env python
# coding: utf-8

# # <span style='color:#065087'>Default start page</span>

# In[1]:


import streamlit as st
import pandas as pd
import numpy as np


# In[2]:


map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)


# In[ ]:





# In[3]:


df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df


# <h1> Hola </h>

# In[4]:


dataframe = np.random.randn(10, 20)
st.dataframe(dataframe)


# In[5]:


dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(dataframe.style.highlight_max(axis=0))


# In[6]:


chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)


# In[ ]:





# In[ ]:




