#!/usr/bin/env python
# coding: utf-8

# In[1]:


import set_working_directory


# In[2]:


from cogent3 import get_app

loader = get_app("load_aligned", format="fasta", moltype="dna")
aln = loader("data/primate_brca1.fasta")
aln.names


# In[3]:


from cogent3 import load_tree
from cogent3 import get_app

tree = load_tree("data/primate_brca1.tree")
gn = get_app("model", "GN", tree=tree)
gn


# In[4]:


gn = get_app("model", "GN", tree="data/primate_brca1.tree")
gn


# In[5]:


fitted = gn(aln)
fitted


# In[6]:


fitted.lf

