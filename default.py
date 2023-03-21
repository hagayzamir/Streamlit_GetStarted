#!/usr/bin/env python
# coding: utf-8

# In[14]:


import streamlit as st
import pandas as pd
pd.set_option('display.max_colwidth', None)
import numpy as np


# In[22]:


experiences_df = pd.DataFrame({
  'subject': ['Birth', 'Childhood', 'Love', 'Loss', 'Joy', 'Pain', \
              'Fear', 'Learning', 'Change', 'Death'],
  'description': ['All human beings have experienced being born and entering the world.', \
                  'Everyone has experienced a period of childhood, characterized by growth, learning, and exploration.', \
                  'Most people have experienced the feeling of love or being loved by others, whether it be romantic or platonic.', \
                  'All people experience loss, such as the loss of a loved one or a significant change in life circumstances.', \
                 'Everyone has experienced moments of joy and happiness, such as achieving a personal goal or celebrating a special occasion.', \
                 'Most people have experienced physical or emotional pain at some point in their lives.', \
                 'Everyone has experienced fear in some form, whether it be a specific phobia or a general sense of anxiety.', \
                 'All human beings have the ability to learn and grow, whether it be through formal education or life experiences.', \
                 'Everyone experiences change throughout their lives, whether it be changes in their physical bodies, relationships, or surroundings.', \
                 'All people will experience the inevitability of death, either personally or through the loss of others.' \
                 ],
    'Selected': [False, False, False, False, False, False, False, False, False, False]
})
#styled_df = experiences_df.style.set_properties(**{'text-align': 'left'}, subset=['description'])
#display(styled_df)


# In[28]:


st.header('Shared experiences')
st.subheader('Select 4 of the 10 options below that you mostley identify with:')


# In[29]:


for index, row in experiences_df.iterrows():
    the_label = row['subject'] + ": " + row['description']
    selected = st.checkbox(label=the_label)
    experiences_df.loc[index, 'Selected'] = selected
    the_label = "";

# Display the updated DataFrame
#st.write(experiences_df)


# In[ ]:





# In[ ]:




