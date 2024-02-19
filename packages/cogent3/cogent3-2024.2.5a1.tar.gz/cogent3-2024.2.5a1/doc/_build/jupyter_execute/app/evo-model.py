#!/usr/bin/env python
# coding: utf-8

# In[1]:


import set_working_directory


# In[2]:


from cogent3 import get_app

loader = get_app("load_aligned", format="fasta", moltype="dna")
select_seqs = get_app("take_named_seqs", "Human", "Rhesus", "Galago")
process = loader + select_seqs
aln = process("data/primate_brca1.fasta")
aln.names


# In[3]:


gn = get_app("model", "GN")
gn


# In[4]:


fitted = gn(aln)
type(fitted)


# In[5]:


fitted


# In[6]:


fitted.lf


# In[7]:


fitted.lnL, fitted.nfp


# In[8]:


fitted.source


# In[9]:


fitted.tree, fitted.alignment


# In[10]:


fitted.total_length(length_as="paralinear")


# In[11]:


gn = get_app("model", "GN", split_codons=True)

fitted = gn(aln)
fitted


# In[12]:


fitted[3]

