#!/usr/bin/env python
# coding: utf-8

# In[1]:


import set_working_directory


# In[2]:


from cogent3.app import io

reader = io.load_json()

ens_tree = reader("data/GN-tree.json")
fig = ens_tree.get_figure(width=600, height=600)
fig.scale_bar = "top right"
fig.show()


# In[3]:


outpath = set_working_directory.get_thumbnail_dir() / "plot_tree-square.png"

fig.write(outpath)


# In[4]:


fig.style_edges(
    "AfricanEl",
    tip2="Manatee",
    legendgroup="Afrotheria",
    line=dict(color="magenta"),
)
fig.show()


# In[5]:


fig.contemporaneous = True
fig.show()

