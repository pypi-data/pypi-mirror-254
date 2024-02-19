#!/usr/bin/env python
# coding: utf-8

# In[1]:


from cogent3 import make_aligned_seqs

data = {
    "s1": "GCTCATGCCAGCTCTTTACAGCATGAGAACA--AGT",
    "s2": "ACTCATGCCAACTCATTACAGCATGAGAACAGCAGT",
    "s3": "ACTCATGCCAGCTCATTACAGCATGAGAACAGCAGT",
    "s4": "ACTCATGCCAGCTCATTACAGCATGAGAACAGCAGT",
    "s5": "ACTCATGCCAGCTCAGTACAGCATGAGAACAGCAGT",
}

nt_seqs = make_aligned_seqs(data=data, moltype="dna")
nt_seqs


# In[2]:


nt_seqs.get_translation(gc=1, incomplete_ok=True)


# In[3]:


from cogent3 import get_code

standard_code = get_code(1)
standard_code.translate("TTTGCAAAC")


# In[4]:


from cogent3 import get_code, make_seq

standard_code = get_code(1)
seq = make_seq("ATGCTAACATAAA", moltype="dna")
translations = standard_code.sixframes(seq)
print(translations)


# In[5]:


from cogent3 import get_code, make_seq

standard_code = get_code(1)
seq = make_seq("ATGCTAACATAAA", moltype="dna")
stops_frame1 = standard_code.get_stop_indices(seq, start=0)
stops_frame1


# In[6]:


stop_index = stops_frame1[0]
seq[stop_index : stop_index + 3]


# In[7]:


from cogent3 import get_code, make_seq

standard_code = get_code(1)
standard_code["TTT"]


# In[8]:


standard_code["A"]


# In[9]:


from cogent3 import get_code

standard_code = get_code(1)
standard_code["TTT"]


# In[10]:


from cogent3 import get_code

standard_code = get_code(1)
standard_code["A"]


# In[11]:


targets = ["A", "C"]
codons = [standard_code[aa] for aa in targets]
codons


# In[12]:


flat_list = sum(codons, [])
flat_list


# In[13]:


from cogent3 import get_code

gc = get_code(1)
alphabet = gc.get_alphabet()
print(alphabet)


# In[14]:


from cogent3 import make_seq

my_seq = make_seq("ATGCACTGGTAA", name="my_gene", moltype="dna")
codons = my_seq.get_in_motif_size(3)
codons


# In[15]:


pep = my_seq.get_translation()
pep


# In[16]:


from cogent3.core.alphabet import AlphabetError


# In[17]:


from cogent3 import make_seq

seq = make_seq("ATGTGATGGTAA", name="s1", moltype="dna")


# In[18]:


pep = seq.get_translation()


# In[19]:


pep = seq.get_translation(include_stop=True)
pep

