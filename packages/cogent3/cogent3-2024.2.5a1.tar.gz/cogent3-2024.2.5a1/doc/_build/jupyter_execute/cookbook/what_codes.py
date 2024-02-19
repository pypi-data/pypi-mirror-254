#!/usr/bin/env python
# coding: utf-8

# In[1]:


import set_working_directory


# In[2]:


from cogent3 import available_codes

available_codes()


# In[3]:


from cogent3 import get_code

gc = get_code(4)
gc

