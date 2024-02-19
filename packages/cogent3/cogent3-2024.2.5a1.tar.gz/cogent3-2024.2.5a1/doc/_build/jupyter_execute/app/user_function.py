#!/usr/bin/env python
# coding: utf-8

# In[1]:


from cogent3.app.typing import defined_types

defined_types()


# In[2]:


from cogent3.app.composable import define_app
from cogent3.app.typing import AlignedSeqsType

@define_app
def up_to(val: AlignedSeqsType, index=2) -> AlignedSeqsType:
    return val[:index]


# In[3]:


first4 = up_to(index=4)
first4


# In[4]:


from cogent3 import make_aligned_seqs

aln = make_aligned_seqs(
    data=dict(a="GCAAGCGTTTAT", b="GCTTTTGTCAAT"), array_align=False, moltype="dna"
)
result = first4(aln)
result


# In[5]:


from typing import Union

from cogent3.app.composable import define_app
from cogent3.app.typing import SeqsCollectionType, SerialisableType

T = Union[SeqsCollectionType, SerialisableType]

@define_app
def rename_seqs(seqs: SeqsCollectionType) -> T:
    """upper case names"""
    return seqs.rename_seqs(lambda x: x.upper())

renamer = rename_seqs()
result = renamer(aln)
result


# In[6]:


from cogent3.app.composable import define_app
from cogent3.app.typing import AlignedSeqsType, PairwiseDistanceType

@define_app
def get_dists(aln: AlignedSeqsType, calc="hamming") -> PairwiseDistanceType:
    return aln.distance_matrix(calc=calc, show_progress=False)

percent_dist = get_dists(calc="pdist")
result = percent_dist(aln)
result

