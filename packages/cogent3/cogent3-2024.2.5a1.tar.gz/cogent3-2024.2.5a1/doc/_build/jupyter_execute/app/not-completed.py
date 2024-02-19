#!/usr/bin/env python
# coding: utf-8

# In[1]:


import set_working_directory


# In[2]:


from cogent3 import get_app

reader = get_app("load_aligned", format="fasta")
select_seqs = get_app("take_named_seqs", "Mouse", "Human")
aln = reader("data/primate_brca1.fasta")
result = select_seqs(aln)
assert result == False
result


# In[3]:


result.source


# In[4]:


result.origin


# In[5]:


result.message


# In[6]:


result = reader("primate_brca1.fasta")
result


# In[7]:


app = reader + select_seqs
result = app("data/primate_brca1.fasta")
result


# In[8]:


result = app("primate_brca1.fasta")
result

