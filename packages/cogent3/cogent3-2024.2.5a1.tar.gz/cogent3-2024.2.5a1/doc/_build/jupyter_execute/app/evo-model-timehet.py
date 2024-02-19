#!/usr/bin/env python
# coding: utf-8

# In[1]:


import set_working_directory


# In[2]:


from cogent3 import load_tree
from cogent3 import get_app

tree = load_tree("data/primate_brca1.tree")
fig = tree.get_figure(contemporaneous=True)
fig.style_edges(
    "Human", tip2="Orangutan", outgroup="Galago", line=dict(color="red")
)
fig.show(width=500, height=500)


# In[3]:


time_het = get_app("model",
    "GN",
    tree=tree,
    time_het=[dict(tip_names=["Human", "Orangutan"], outgroup_name="Galago")],
)


# In[4]:


loader = get_app("load_aligned", format="fasta")
aln = loader("data/primate_brca1.fasta")
result = time_het(aln)


# In[5]:


result.lf

