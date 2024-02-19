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

codon_aligner = get_app("progressive_align", "codon")
aligned = codon_aligner(seqs)
aligned


# In[4]:


nt_aligner = get_app("progressive_align", "codon", distance="paralinear")
aligned = nt_aligner(seqs)
aligned


# In[5]:


tree = "((Chimp:0.001,Human:0.001):0.0076,Macaque:0.01,((Rat:0.01,Mouse:0.01):0.02,Mouse_Lemur:0.02):0.01)"
codon_aligner = get_app("progressive_align", "codon", guide_tree=tree)
aligned = codon_aligner(seqs)
aligned


# In[6]:


codon_aligner = get_app("progressive_align",
    "codon", guide_tree=tree, indel_rate=0.001, indel_length=0.01
)
aligned = codon_aligner(seqs)
aligned


# In[7]:


codon_aligner = get_app("progressive_align",
    "CNFHKY", guide_tree=tree, param_vals=dict(omega=0.1, kappa=3)
)
aligned = codon_aligner(seqs)
aligned


# In[8]:


aligned.info

