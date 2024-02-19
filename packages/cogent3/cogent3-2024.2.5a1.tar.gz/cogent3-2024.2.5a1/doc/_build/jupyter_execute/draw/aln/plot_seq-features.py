#!/usr/bin/env python
# coding: utf-8

# In[1]:


import set_working_directory


# In[2]:


from cogent3 import load_seq

seq = load_seq("data/C-elegans-chromosome-I.gb", moltype="dna")
seq


# In[3]:


seq = seq[25000:35000]


# In[4]:


fig = seq.get_drawable()
fig.show(height=400, width=700)


# In[5]:


fig = seq.get_drawable(biotype=("gene", "CDS", "mRNA"))
fig.show(height=300, width=650)


# In[6]:


outpath = set_working_directory.get_thumbnail_dir() / "plot_seq-features.png"

fig.write(outpath)

