#!/usr/bin/env python
# coding: utf-8

# In[1]:


import set_working_directory


# In[2]:


from cogent3 import get_app

loader = get_app("load_aligned", format="fasta", moltype="dna")
aln = loader("data/primate_brca1.fasta")

hc_differ = get_app("natsel_timehet",
    "GNC",
    tree="data/primate_brca1.tree",
    optimise_motif_probs=False,
    tip1="Human",
    tip2="Chimpanzee",
)
result = hc_differ(aln)
result


# In[3]:


result.alt.lf

