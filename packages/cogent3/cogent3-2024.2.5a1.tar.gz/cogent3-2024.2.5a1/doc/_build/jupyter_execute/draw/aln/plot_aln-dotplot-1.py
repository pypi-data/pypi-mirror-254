#!/usr/bin/env python
# coding: utf-8

# In[1]:


import set_working_directory


# In[2]:


from cogent3 import load_unaligned_seqs

seqs = load_unaligned_seqs("data/SCA1-cds.fasta", moltype="dna")
draw = seqs.dotplot()
draw.show()


# In[3]:


outpath = set_working_directory.get_thumbnail_dir() / "plot_aln-dotplot-1.png"

draw.write(outpath)


# In[4]:


draw = seqs.dotplot(name1="Human", name2="Mouse", window=8, threshold=8)
draw.show()


# In[5]:


draw = seqs.dotplot(name1="Human", name2="Mouse", rc=True)
draw.show()


# In[6]:


draw = seqs.dotplot(name1="Human", name2="Mouse", rc=True, title="SCA1", width=400)
draw.show()

