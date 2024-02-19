#!/usr/bin/env python
# coding: utf-8

# In[1]:


import set_working_directory


# In[2]:


from cogent3 import get_app

loader = get_app("load_json")
seqs = loader("data/tp53.json")
dp = seqs.dotplot(name1="Macaque", name2="Marmoset", width=600)
dp.show()


# In[3]:


outpath = set_working_directory.get_thumbnail_dir() / "plot_aln-dotplot-2.png"

dp.write(outpath)


# In[4]:


help(dp.remove_track)


# In[5]:


dp.remove_track(left_track=True)
dp.show()

