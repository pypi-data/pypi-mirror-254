#!/usr/bin/env python
# coding: utf-8

# In[1]:


from cogent3 import make_aligned_seqs, make_unaligned_seqs


# In[2]:


seqs = {
    "hum": "AAGCAGATCCAGGAAAGCAGCGAGAATGGCAGCCTGGCCGCGCGCCAGGAGAGGCAGGCCCAGGTCAACCTCACT",
    "mus": "AAGCAGATCCAGGAGAGCGGCGAGAGCGGCAGCCTGGCCGCGCGGCAGGAGAGGCAGGCCCAAGTCAACCTCACG",
    "rat": "CTGAACAAGCAGCCACTTTCAAACAAGAAA",
}
unaligned_DNA = make_unaligned_seqs(seqs, moltype="dna")
unaligned_DNA


# In[3]:


unaligned_aa = unaligned_DNA.get_translation()
unaligned_aa


# In[4]:


aligned_aa_seqs = {
    "hum": "KQIQESSENGSLAARQERQAQVNLT",
    "mus": "KQIQESGESGSLAARQERQAQVNLT",
    "rat": "LNKQ------PLS---------NKK",
}
aligned_aa = make_aligned_seqs(aligned_aa_seqs, moltype="protein")
aligned_DNA = aligned_aa.replace_seqs(unaligned_DNA)
aligned_DNA

