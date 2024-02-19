#!/usr/bin/env python
# coding: utf-8

# In[1]:


from cogent3.util.union_dict import UnionDict

data = UnionDict(a=2, b={"c": 24, "d": [25]})
data.a


# In[2]:


data["a"]


# In[3]:


data.b.d


# In[4]:


from cogent3.util.union_dict import UnionDict

data = UnionDict(a=2, b={"c": 24, "d": [25]})
data.b |= {"d": 25}
data.b


# In[5]:


data.b.union({"d": [25]})


# In[6]:


data.b
{"c": 24, "d": [25]}


# In[7]:


from cogent3.util.union_dict import UnionDict

data = UnionDict(a=2, b={"c": 24, "d": [25]})
data["k"]


# In[8]:


data.k

