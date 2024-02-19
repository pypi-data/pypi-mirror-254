#!/usr/bin/env python
# coding: utf-8

# In[1]:


import set_working_directory


# In[2]:


from cogent3 import get_app

loader = get_app("load_aligned", format="fasta", moltype="dna")
aln = loader("data/primate_brca1.fasta")

omega_eq_1 = get_app("natsel_neutral",
    "GNC", tree="data/primate_brca1.tree", optimise_motif_probs=False
)
result = omega_eq_1(aln)
type(result)


# In[3]:


result


# In[4]:


result.alt.lf

