#!/usr/bin/env python
# coding: utf-8

# In[1]:


import set_working_directory


# In[2]:


from pathlib import Path
from tempfile import TemporaryDirectory

tmpdir = TemporaryDirectory(dir=".")
path_to_dir = tmpdir.name


# In[3]:


from cogent3 import get_app, open_data_store

out_dstore = open_data_store(path_to_dir, suffix="fa", mode="w")

loader = get_app("load_aligned", format="fasta", moltype="dna")
cpos3 = get_app("take_codon_positions", 3)
writer = get_app("write_seqs", out_dstore, format="fasta")


# In[4]:


data = loader("data/primate_brca1.fasta")
just3rd = cpos3(data)
m = writer(just3rd)


# In[5]:


process = loader + cpos3 + writer
m = process("data/primate_brca1.fasta")


# In[6]:


dstore = open_data_store("data", suffix="fasta", mode="r")
result = process.apply_to(dstore)


# In[7]:


out_dstore.summary_logs


# In[8]:


out_dstore.describe


# In[9]:


out_dstore.summary_not_completed


# In[10]:


result = process.apply_to(dstore, show_progress=True)


# In[11]:


import shutil

shutil.rmtree(path_to_dir, ignore_errors=True)

