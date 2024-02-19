#!/usr/bin/env python
# coding: utf-8

# In[1]:


import set_working_directory


# In[2]:


from cogent3 import get_app

loader = get_app("load_aligned", format="fasta", moltype="dna")
aln = loader("data/primate_brca1.fasta")

tree = "data/primate_brca1.tree"

null = get_app("model", "GTR", tree=tree, optimise_motif_probs=True)
alt = get_app("model", "GN", tree=tree, optimise_motif_probs=True)
hyp = get_app("hypothesis", null, alt)
result = hyp(aln)
type(result)


# In[3]:


result


# In[4]:


result.LR, result.df, result.pvalue


# In[5]:


result.null


# In[6]:


result.null.lf


# In[7]:


result.alt.lf

