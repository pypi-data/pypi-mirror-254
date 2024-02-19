#!/usr/bin/env python
# coding: utf-8

# In[1]:


import set_working_directory


# In[2]:


from cogent3 import get_app

loader = get_app("load_unaligned", format="fasta")
to_aa = get_app("translate_seqs")
process = loader + to_aa
seqs = process("data/SCA1-cds.fasta")


# In[3]:


from cogent3 import get_app

aa_aligner = get_app("progressive_align", "protein")
aligned = aa_aligner(seqs)
aligned


# In[4]:


aa_aligner = get_app("progressive_align", "protein", distance="paralinear")
aligned = aa_aligner(seqs)
aligned


# In[5]:


aligned.info

