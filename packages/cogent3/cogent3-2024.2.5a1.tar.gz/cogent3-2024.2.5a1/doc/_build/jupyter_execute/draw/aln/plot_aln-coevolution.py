#!/usr/bin/env python
# coding: utf-8

# In[1]:


import set_working_directory


# In[2]:


from cogent3 import load_aligned_seqs

aln = load_aligned_seqs("data/brca1.fasta", moltype="dna")
aln = aln.no_degenerates(motif_length=3)
aln = aln.get_translation()
aln = aln[:100]  # for compute speed in testing the documentation
coevo = aln.coevolution(show_progress=False, drawable="heatmap")
coevo.drawable.show()


# In[3]:


outpath = set_working_directory.get_thumbnail_dir() / "plot_aln-coevolution.png"

coevo.drawable.write(outpath)


# In[4]:


coevo = aln.coevolution(show_progress=False, drawable="violin")
coevo.drawable.show(width=300)


# In[5]:


coevo = aln.coevolution(show_progress=False, drawable="box")
coevo.drawable.show(width=300)

