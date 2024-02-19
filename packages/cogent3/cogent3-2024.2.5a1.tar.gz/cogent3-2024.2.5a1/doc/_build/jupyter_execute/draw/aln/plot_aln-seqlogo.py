#!/usr/bin/env python
# coding: utf-8

# In[1]:


import set_working_directory


# In[2]:


from cogent3 import load_aligned_seqs
from cogent3.parse import jaspar

_, pwm = jaspar.read("data/tbp.jaspar")
freqarr = pwm.to_freq_array()
freqarr[:5]  # illustrating the contents of the MotifFreqsArray


# In[3]:


logo = freqarr.logo()
logo.show(height=250, width=500)


# In[4]:


outpath = set_working_directory.get_thumbnail_dir() / "plot_aln-seqlogo.png"

logo.write(outpath)


# In[5]:


aln = load_aligned_seqs("data/brca1-bats.fasta", moltype="dna")
l = aln[:311].seqlogo(height=300, width=500, wrap=60, vspace=0.05)
l.show()


# In[6]:


aa = aln.get_translation(incomplete_ok=True)[:120]
logo = aa.seqlogo(width=500, height=300, wrap=50, vspace=0.1)
logo.show()

