#!/usr/bin/env python
# coding: utf-8

# In[1]:


import set_working_directory


# In[2]:


from cogent3 import get_app

loader = get_app("load_aligned", format="fasta", moltype="dna")
aln = loader("data/primate_brca1.fasta")
model = get_app("model", "GN", tree="data/primate_brca1.tree")
result = model(aln)


# In[3]:


tabulator = get_app("tabulate_stats")
tabulated = tabulator(result)
tabulated


# In[4]:


tabulated["edge params"]


# In[5]:


tabulated["global params"]


# In[6]:


tabulated["motif params"]

