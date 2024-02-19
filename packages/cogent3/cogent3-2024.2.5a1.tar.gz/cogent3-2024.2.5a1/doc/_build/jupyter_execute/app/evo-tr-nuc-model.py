#!/usr/bin/env python
# coding: utf-8

# In[1]:


import set_working_directory


# In[2]:


from cogent3 import available_models

available_models("nucleotide")


# In[3]:


from cogent3 import get_app

loader = get_app("load_aligned", format="fasta", moltype="dna")
aln = loader("data/primate_brca1.fasta")
model = get_app("model",
    "GTR", tree="data/primate_brca1.tree", optimise_motif_probs=True
)
result = model(aln)
result


# In[4]:


result.lf

