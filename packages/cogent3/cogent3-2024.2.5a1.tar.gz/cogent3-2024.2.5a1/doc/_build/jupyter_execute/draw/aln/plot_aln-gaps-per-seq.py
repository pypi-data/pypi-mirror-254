#!/usr/bin/env python
# coding: utf-8

# In[1]:


import set_working_directory


# In[2]:


from cogent3 import load_aligned_seqs

aln = load_aligned_seqs("data/brca1.fasta", moltype="dna")

counts = aln.count_gaps_per_seq(unique=True)
counts[10: 20] # limiting the width of the displayed output


# In[3]:


counts = aln.count_gaps_per_seq(unique=True, drawable="bar")
counts.drawable.show(width=500)


# In[4]:


outpath = set_working_directory.get_thumbnail_dir() / "plot_aln-gaps-per-seq.png"

counts.drawable.write(outpath)


# In[5]:


counts = aln.count_gaps_per_seq(unique=True, drawable="violin")
counts.drawable.show(width=300, height=500)


# In[6]:


counts = aln.count_gaps_per_seq(unique=True, drawable="box")
counts.drawable.show(width=300, height=500)

