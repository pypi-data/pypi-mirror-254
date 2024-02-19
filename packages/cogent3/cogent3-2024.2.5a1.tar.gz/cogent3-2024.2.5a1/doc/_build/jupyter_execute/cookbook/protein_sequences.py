#!/usr/bin/env python
# coding: utf-8

# In[1]:


import set_working_directory


# In[2]:


from cogent3 import make_seq

p = make_seq("THISISAPRQTEIN", "myProtein", moltype="protein")
type(p)


# In[3]:


p


# In[4]:


from cogent3 import get_code

standard_code = get_code(1)
standard_code.translate("TTTGCAAAC")


# In[5]:


from cogent3 import make_seq

nuc = make_seq("TTTGCAAAC", moltype="dna")
pep = nuc.get_translation()
pep


# In[6]:


from cogent3 import load_aligned_seqs

seq = load_aligned_seqs("data/abglobin_aa.phylip", moltype="protein")

