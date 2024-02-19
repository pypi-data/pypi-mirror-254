#!/usr/bin/env python
# coding: utf-8

# In[1]:


from cogent3 import make_seq

my_seq = make_seq("AGTACACTGGT")
my_seq.moltype.label


# In[2]:


my_seq


# In[3]:


my_seq = make_seq("AGTACACTGGT", moltype="bytes")
my_seq.moltype.label


# In[4]:


my_seq


# In[5]:


from cogent3 import make_seq

my_seq = make_seq("AGTACACTGGT", moltype="dna")
my_seq


# In[6]:


from cogent3 import make_seq

rnaseq = make_seq("ACGUACGUACGUACGU", moltype="rna")


# In[7]:


from cogent3 import make_seq

my_seq = make_seq("AGTACACTGGT", moltype="dna")
my_seq


# In[8]:


from cogent3 import make_seq

rnaseq = make_seq("ACGUACGUACGUACGU", moltype="rna")
rnaseq


# In[9]:


from cogent3 import make_seq

my_seq = make_seq("AGTACACTGGT", "my_gene", moltype="dna")
my_seq
type(my_seq)


# In[10]:


from cogent3 import make_seq

my_seq = make_seq("AGTACACTGGT", moltype="dna")
my_seq.name = "my_gene"
my_seq


# In[11]:


from cogent3 import make_seq

my_seq = make_seq("AGTACACTGGT", moltype="dna")
my_seq.complement()


# In[12]:


my_seq.rc()


# In[13]:


from cogent3 import make_seq

my_seq = make_seq("GCTTGGGAAAGTCAAATGGAA", name="s1", moltype="dna")
pep = my_seq.get_translation()
type(pep)


# In[14]:


pep


# In[15]:


from cogent3 import make_seq

my_seq = make_seq("ACGTACGTACGTACGT", moltype="dna")
rnaseq = my_seq.to_rna()
rnaseq


# In[16]:


from cogent3 import make_seq

rnaseq = make_seq("ACGUACGUACGUACGU", moltype="rna")
dnaseq = rnaseq.to_dna()
dnaseq


# In[17]:


from cogent3 import make_seq

a = make_seq("AGTACACTGGT", moltype="dna")
a.can_pair(a.complement())


# In[18]:


a.can_pair(a.rc())


# In[19]:


from cogent3 import make_seq

my_seq = make_seq("AGTACACTGGT", moltype="dna")
extra_seq = make_seq("CTGAC", moltype="dna")
long_seq = my_seq + extra_seq
long_seq


# In[20]:


my_seq[1:6]


# In[21]:


from cogent3 import make_seq

seq = make_seq("ATGATGATGATG", moltype="dna")
pos3 = seq[2::3]
assert str(pos3) == "GGGG"


# In[22]:


from cogent3 import make_seq

seq = make_seq("ATGATGATGATG", moltype="dna")
indices = [(i, i + 2) for i in range(len(seq))[::3]]
pos12 = seq.add_feature(biotype="pos12", name="pos12", spans=indices)
pos12 = pos12.get_slice()
assert str(pos12) == "ATATATAT"


# In[23]:


rnaseq.shuffle()


# In[24]:


from cogent3 import make_seq

s = make_seq("--AUUAUGCUAU-UAu--", moltype="rna")
s.degap()

