#!/usr/bin/env python
# coding: utf-8

# In[1]:


import set_working_directory


# In[2]:


from cogent3.app import io

reader = io.load_json()

tree = reader("data/tree-with-support.json")
fig = tree.get_figure(show_support=True, threshold=0.8)
fig.scale_bar = None
fig.show(width=500, height=400)


# In[3]:


fig.support_xshift = 15
fig.support_yshift = 0
fig.show(width=500, height=400)


# In[4]:


outpath = set_working_directory.get_thumbnail_dir() / "plot_tree-support.png"

fig.write(outpath)

