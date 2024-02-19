#!/usr/bin/env python
# coding: utf-8

# In[1]:


import set_working_directory


# In[2]:


from cogent3 import load_aligned_seqs, get_app

seqs = load_aligned_seqs("data/brca1.fasta", moltype="dna").degap()
seqs = seqs.take_seqs(
    ["LeafNose", "FalseVamp", "RoundEare", "Sloth", "Anteater", "HairyArma"]
)


# In[3]:


aligner = get_app("progressive_align", "nucleotide", indel_rate=1e-2, indel_length=1e-9)
aln = aligner(seqs)
dp = aln[2200:2500].dotplot("HairyArma", "RoundEare")
dp.show()


# In[4]:


outpath = set_working_directory.get_thumbnail_dir() / "plot_aln-dotplot-3.png"

dp.write(outpath)


# In[5]:


aln[2300:2500]


# In[6]:


aligner = get_app("progressive_align", "nucleotide")
aln = aligner(seqs)
aln[2200:2500].dotplot("HairyArma", "RoundEare").show()


# In[7]:


aln[2300:2500]

