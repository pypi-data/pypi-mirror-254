#!/usr/bin/env python
# coding: utf-8

# In[1]:


import set_working_directory


# In[2]:


from cogent3.app import io

reader = io.load_json()

ens_tree = reader("data/GN-tree.json")
fig = ens_tree.get_figure(style="angular", width=600, height=600)
fig.show()


# In[3]:


fig.contemporaneous = True
fig.show()


# In[4]:


outpath = set_working_directory.get_thumbnail_dir() / "plot_tree-angular.png"

fig.write(outpath)

