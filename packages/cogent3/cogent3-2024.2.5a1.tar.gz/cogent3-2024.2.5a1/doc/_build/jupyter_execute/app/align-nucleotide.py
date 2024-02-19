#!/usr/bin/env python
# coding: utf-8

# In[1]:


import set_working_directory


# In[2]:


from cogent3 import get_app

loader = get_app("load_unaligned", format="fasta")
seqs = loader("data/SCA1-cds.fasta")


# In[3]:


from cogent3 import get_app

nt_aligner = get_app("progressive_align", "nucleotide")
aligned = nt_aligner(seqs)
aligned


# In[4]:


nt_aligner = get_app("progressive_align", "nucleotide", distance="TN93")
aligned = nt_aligner(seqs)
aligned


# In[5]:


tree = "((Chimp:0.001,Human:0.001):0.0076,Macaque:0.01,((Rat:0.01,Mouse:0.01):0.02,Mouse_Lemur:0.02):0.01)"
nt_aligner = get_app("progressive_align", "nucleotide", guide_tree=tree)
aligned = nt_aligner(seqs)
aligned


# In[6]:


tree = "((Chimp:0.001,Human:0.001):0.0076,Macaque:0.01,((Rat:0.01,Mouse:0.01):0.02,Mouse_Lemur:0.02):0.01)"
nt_aligner = get_app("progressive_align", "F81", guide_tree=tree)
aligned = nt_aligner(seqs)
aligned


# In[7]:


aligned.info

