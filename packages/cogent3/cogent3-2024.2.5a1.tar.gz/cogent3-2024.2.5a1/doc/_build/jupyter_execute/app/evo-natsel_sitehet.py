#!/usr/bin/env python
# coding: utf-8

# In[1]:


import set_working_directory


# In[2]:


from cogent3 import get_app

loader = get_app("load_aligned", format="fasta", moltype="dna")
aln = loader("data/primate_brca1.fasta")

sites_differ = get_app("natsel_sitehet",
    "GNC", tree="data/primate_brca1.tree", optimise_motif_probs=False
)

result = sites_differ(aln)
result


# In[3]:


result.alt.lf


# In[4]:


bprobs = result.alt.lf.get_bin_probs()
bprobs[:, :20]

