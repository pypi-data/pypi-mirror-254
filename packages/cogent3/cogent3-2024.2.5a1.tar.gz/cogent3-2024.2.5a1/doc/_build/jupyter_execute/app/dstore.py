#!/usr/bin/env python
# coding: utf-8

# In[1]:


import set_working_directory


# In[2]:


from cogent3 import open_data_store

dstore = open_data_store("data/raw.zip", suffix="fa", mode="r")
print(dstore)


# In[3]:


dstore.describe


# In[4]:


m = dstore[0]
m


# In[5]:


for m in dstore[:5]:
    print(m)


# In[6]:


m.read()[:20] # truncating


# In[7]:


dstore = open_data_store("data/demo-locked.sqlitedb")
dstore.describe


# In[8]:


dstore.unlock(force=True)


# In[9]:


dstore.summary_logs


# In[10]:


dstore.logs


# In[11]:


print(dstore.logs[0].read()[:225]) # truncated for clarity


# In[12]:


from cogent3 import open_data_store

in_dstore = open_data_store("data/raw.zip", suffix="fa")


# In[13]:


out_dstore = open_data_store("translated.sqlitedb", mode="w")


# In[14]:


from cogent3 import get_app

load = get_app("load_unaligned", moltype="dna")
translate = get_app("translate_seqs")
write = get_app("write_db", data_store=out_dstore)
app = load + translate + write
app


# In[15]:


out_dstore = app.apply_to(in_dstore)


# In[16]:


out_dstore.describe


# In[17]:


out_dstore.validate()


# In[18]:


out_dstore.summary_not_completed


# In[19]:


len(out_dstore.not_completed)


# In[20]:


out_dstore.not_completed[:2]


# In[21]:


import pathlib

fn = pathlib.Path("translated.sqlitedb")
fn.unlink()

