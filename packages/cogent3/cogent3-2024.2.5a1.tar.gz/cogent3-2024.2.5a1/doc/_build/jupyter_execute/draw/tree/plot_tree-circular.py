#!/usr/bin/env python
# coding: utf-8

# In[1]:


import set_working_directory


# In[2]:


from cogent3.app import io

reader = io.load_json()

ens_tree = reader("data/GN-tree.json")
fig = ens_tree.get_figure("circular", width=600, height=600)
fig.scale_bar = "top right"
fig.label_pad = 0.1
fig.show()


# In[3]:


fig.style_edges(
    "AfricanEl",
    tip2="Manatee",
    legendgroup="Afrotheria",
    line=dict(color="magenta", width=2),
)
fig.show(width=650, height=600)


# In[4]:


fig.contemporaneous = True
fig.label_pad = 0.3
fig.show(width=650, height=600)


# In[5]:


outpath = set_working_directory.get_thumbnail_dir() / "plot_tree-circular.png"

fig.write(outpath)

