#!/usr/bin/env python
# coding: utf-8

# In[1]:


import set_working_directory


# In[2]:


from cogent3 import make_aligned_seqs, make_unaligned_seqs

dna = {"seq1": "ATGACC", "seq2": "ATCGCC"}
seqs = make_aligned_seqs(data=dna, moltype="dna")
type(seqs)


# In[3]:


seqs = make_unaligned_seqs(dna, moltype="dna")
type(seqs)


# In[4]:


from cogent3 import make_aligned_seqs

dna = {"seq1": "ATGACC", "seq2": "ATCGCC"}
seqs = make_aligned_seqs(data=dna, moltype="dna", array_align=True)
print(type(seqs))
seqs


# In[5]:


from cogent3 import load_unaligned_seqs

seqs = load_unaligned_seqs("data/test.paml")
seqs


# In[6]:


from cogent3 import make_aligned_seqs

aln = make_aligned_seqs(
    [("seq1", "ATGAA------"), ("seq2", "ATG-AGTGATG"), ("seq3", "AT--AG-GATG")],
    moltype="dna",
)
aln


# In[7]:


new_seqs = make_aligned_seqs(
    [("seq0", "ATG-AGT-AGG"), ("seq4", "ATGCC------")], moltype="dna"
)
new_aln = aln.add_seqs(new_seqs)
new_aln


# In[8]:


new_aln = aln.add_seqs(new_seqs, before_name="seq2")
new_aln


# In[9]:


new_aln = aln.add_seqs(new_seqs, after_name="seq2")
new_aln


# In[10]:


from cogent3 import make_aligned_seqs

aln = make_aligned_seqs(
    [("seq1", "ATGAA------"), ("seq2", "ATG-AGTGATG"), ("seq3", "AT--AG-GATG")],
    moltype="dna",
)
ref_aln = make_aligned_seqs(
    [("seq3", "ATAGGATG"), ("seq0", "ATG-AGCG"), ("seq4", "ATGCTGGG")],
    moltype="dna",
)
new_aln = aln.add_from_ref_aln(ref_aln)
new_aln


# In[11]:


from cogent3 import make_aligned_seqs

aln = make_aligned_seqs(
    [("seq1", "ATGAA---TG-"), ("seq2", "ATG-AGTGATG"), ("seq3", "AT--AG-GATG")],
    moltype="dna",
)
new_aln = aln.get_degapped_relative_to("seq1")
new_aln


# In[12]:


from cogent3 import make_aligned_seqs

aln = make_aligned_seqs(
    [("seq1", "ATGAA------"), ("seq2", "ATG-AGTGATG"), ("seq3", "AT--AG-GATG")],
    moltype="dna",
    array_align=False,
)
seq = aln.get_seq("seq1")
seq.name
type(seq)
seq.is_gapped()


# In[13]:


seq = aln.get_gapped_seq("seq1")
seq.is_gapped()
seq


# In[14]:


aln.names


# In[15]:


from cogent3 import load_aligned_seqs, load_unaligned_seqs

fn = "data/long_testseqs.fasta"
seqs = load_unaligned_seqs(fn, moltype="dna")
my_seq = seqs.seqs[0]
my_seq[:24]


# In[16]:


type(my_seq)


# In[17]:


aln = load_aligned_seqs(fn, moltype="dna")
aln.seqs[0][:24]


# In[18]:


from cogent3 import load_aligned_seqs

aln = load_aligned_seqs("data/test.paml", moltype="dna")
aln.names


# In[19]:


new = aln.take_seqs(["Human", "HowlerMon"])
new.names


# In[20]:


from cogent3 import load_unaligned_seqs
from cogent3.core.alignment import Alignment

seq = load_unaligned_seqs("data/test.paml", moltype="dna")
seq


# In[21]:


aln = Alignment(seq)
aln


# In[22]:


from cogent3 import make_aligned_seqs

data = [("a", "ACG---"), ("b", "CCTGGG")]
aln = make_aligned_seqs(data=data)
dna = aln.to_dna()
dna


# In[23]:


aln.to_moltype("dna")


# In[24]:


from cogent3 import make_aligned_seqs

data = [("a", "ACG---"), ("b", "CCUGGG")]
aln = make_aligned_seqs(data=data)
rna = aln.to_rna()
rna


# In[25]:


from cogent3 import make_aligned_seqs

data = [("x", "TYV"), ("y", "TE-")]
aln = make_aligned_seqs(data=data)
prot = aln.to_protein()
prot


# In[26]:


from cogent3 import load_aligned_seqs

aln = load_aligned_seqs("data/primate_cdx2_promoter.fasta")
degapped = aln.degap()
print(type(degapped))


# In[27]:


from cogent3 import make_aligned_seqs

dna = {"seq1": "ATGACC", "seq2": "ATCGCC"}
aln = make_aligned_seqs(data=dna, moltype="dna")
aln.write("sample.fasta")


# In[28]:


aln.write("sample", format="fasta")


# In[29]:


from cogent3.util.io import remove_files

remove_files(["sample", "sample.fasta"], error_on_missing=False)


# In[30]:


from cogent3 import load_aligned_seqs
from cogent3.core.alignment import Alignment

seq = load_aligned_seqs("data/long_testseqs.fasta")
aln = Alignment(seq)
fasta_align = aln


# In[31]:


from cogent3 import load_aligned_seqs
from cogent3.core.alignment import Alignment

seq = load_aligned_seqs("data/test.paml")
aln = Alignment(seq)
got = aln.to_phylip()
print(got)


# In[32]:


from cogent3 import load_aligned_seqs
from cogent3.core.alignment import Alignment

seq = load_aligned_seqs("data/test.paml")
aln = Alignment(seq)
string_list = aln.to_dict().values()


# In[33]:


from cogent3 import load_aligned_seqs

fn = "data/long_testseqs.fasta"
aln = load_aligned_seqs(fn, moltype="dna")
aln[:24]


# In[34]:


from cogent3 import load_unaligned_seqs

fn = "data/long_testseqs.fasta"
seqs = load_unaligned_seqs(fn)
seqs[:24]


# In[35]:


from cogent3 import load_aligned_seqs

seq = load_aligned_seqs("data/test.paml")
column_four = aln[3]


# In[36]:


from cogent3 import load_aligned_seqs

aln = load_aligned_seqs("data/long_testseqs.fasta")
region = aln[50:70]


# In[37]:


from cogent3 import load_aligned_seqs

aln = load_aligned_seqs("data/primate_cdx2_promoter.fasta")
col = aln[113:115].iter_positions()
type(col)
list(col)


# In[38]:


from cogent3 import make_aligned_seqs

aln = make_aligned_seqs(
    data={"seq1": "ATGATGATG---", "seq2": "ATGATGATGATG"}, array_align=False
)
list(range(len(aln))[2::3])
indices = [(i, i + 1) for i in range(len(aln))[2::3]]
indices


# In[39]:


pos3 = aln.add_feature(biotype="pos3", name="pos3", spans=indices)
pos3 = pos3.get_slice()
pos3


# In[40]:


from cogent3 import make_aligned_seqs

aln = make_aligned_seqs(
    data={"seq1": "ATGATGATG---", "seq2": "ATGATGATGATG"}, array_align=True
)
pos3 = aln[2::3]
pos3


# In[41]:


from cogent3 import make_aligned_seqs

aln = make_aligned_seqs(
    data={"seq1": "ACGTAA---", "seq2": "ACGACA---", "seq3": "ACGCAATGA"},
    moltype="dna",
)
new = aln.trim_stop_codons()
new


# In[42]:


aln = make_aligned_seqs(
    data={
        "seq1": "ACGTAA---",
        "seq2": "ACGAC----",  # terminal codon incomplete
        "seq3": "ACGCAATGA",
    },
    moltype="dna",
)
new = aln.trim_stop_codons(strict=True)


# In[43]:


from cogent3 import make_aligned_seqs

aln = make_aligned_seqs(
    data=[
        ("seq1", "ATGAAGGTG---"),
        ("seq2", "ATGAAGGTGATG"),
        ("seq3", "ATGAAGGNGATG"),
    ],
    moltype="dna",
)


# In[44]:


nucs = aln.no_degenerates()
nucs


# In[45]:


trinucs = aln.no_degenerates(motif_length=3)
trinucs


# In[46]:


from cogent3 import load_aligned_seqs

aln = load_aligned_seqs("data/long_testseqs.fasta")
pos = aln.variable_positions()
just_variable_aln = aln.take_positions(pos)
just_variable_aln[:10]


# In[47]:


from cogent3 import load_aligned_seqs

aln = load_aligned_seqs("data/long_testseqs.fasta")
pos = aln.variable_positions()
just_constant_aln = aln.take_positions(pos, negate=True)
just_constant_aln[:10]


# In[48]:


from cogent3 import load_aligned_seqs

aln = load_aligned_seqs("data/long_testseqs.fasta")
variable_codons = aln.filtered(
    lambda x: len(set(map(tuple, x))) > 1, motif_length=3
)
just_variable_aln[:9]


# In[49]:


aln = aln.to_type(array_align=False)
variable_codons = aln.filtered(lambda x: len(set("".join(x))) > 1, motif_length=3)
just_variable_aln[:9]


# In[50]:


from cogent3 import load_aligned_seqs

aln = load_aligned_seqs("data/long_testseqs.fasta")
aln.take_seqs(["Human", "Mouse"])


# In[51]:


aln.take_seqs(["Human", "Mouse"], negate=True)


# In[52]:


from cogent3 import make_aligned_seqs

aln = make_aligned_seqs(
    data=[
        ("seq1", "ATGAAGGTG---"),
        ("seq2", "ATGAAGGTGATG"),
        ("seq3", "ATGAAGGNGATG"),
    ],
    moltype="dna",
)

def no_N_chars(s):
    return "N" not in s

aln.take_seqs_if(no_N_chars)


# In[53]:


aln.take_seqs_if(no_N_chars, negate=True)


# In[54]:


from cogent3 import make_aligned_seqs

aln = make_aligned_seqs(
    data=[
        ("seq1", "ATGAAGGTG---"),
        ("seq2", "ATGAAGGTGATG"),
        ("seq3", "ATGAAGGNGATG"),
    ],
    moltype="dna",
)
counts = aln.counts()
counts


# In[55]:


counts = aln.counts(motif_length=3)
counts


# In[56]:


counts = aln.counts(include_ambiguity=True)
counts


# In[57]:


from cogent3 import load_aligned_seqs

aln = load_aligned_seqs("data/primate_cdx2_promoter.fasta", moltype="dna")
motif_probs = aln.get_motif_probs()
motif_probs


# In[58]:


from cogent3 import DNA, load_aligned_seqs

trinuc_alphabet = DNA.alphabet.get_word_alphabet(3)
aln = load_aligned_seqs("data/primate_cdx2_promoter.fasta", moltype="dna")
motif_probs = aln.get_motif_probs(alphabet=trinuc_alphabet)
for m in sorted(motif_probs, key=lambda x: motif_probs[x], reverse=True):
    print("%s  %.3f" % (m, motif_probs[m]))


# In[59]:


aln = make_aligned_seqs(data=[("a", "AACAAC"), ("b", "AAGAAG")], moltype="dna")
motif_probs = aln.get_motif_probs()
assert motif_probs["T"] == 0.0
motif_probs = aln.get_motif_probs(pseudocount=1e-6)
assert 0 < motif_probs["T"] <= 1e-6


# In[60]:


seqs = [("a", "AACGTAAG"), ("b", "AACGTAAG")]
aln = make_aligned_seqs(data=seqs, moltype="dna")
dinuc_alphabet = DNA.alphabet.get_word_alphabet(2)
motif_probs = aln.get_motif_probs(alphabet=dinuc_alphabet)
assert motif_probs["AA"] == 0.25


# In[61]:


seqs = [("my_seq", "AAAGTAAG")]
aln = make_aligned_seqs(data=seqs, moltype="dna")
my_seq = aln.get_seq("my_seq")
my_seq.count("AA")
"AAA".count("AA")
"AAAA".count("AA")


# In[62]:


from cogent3 import make_seq

seq = make_seq(moltype="dna", seq="AAAGTAAG")
seq
di_nucs = [seq[i : i + 2] for i in range(len(seq) - 1)]
sum([nn == "AA" for nn in di_nucs])


# In[63]:


from cogent3 import load_aligned_seqs

aln = load_aligned_seqs("data/primate_cdx2_promoter.fasta")
col = aln[113:115].iter_positions()
c1, c2 = list(col)
c1, c2
list(filter(lambda x: x == "-", c1))
list(filter(lambda x: x == "-", c2))


# In[64]:


from cogent3 import load_aligned_seqs

aln = load_aligned_seqs("data/primate_cdx2_promoter.fasta")
for column in aln[113:150].iter_positions():
    ungapped = list(filter(lambda x: x == "-", column))
    gap_fraction = len(ungapped) * 1.0 / len(column)
    print(gap_fraction)


# In[65]:


from cogent3 import make_aligned_seqs

aln = make_aligned_seqs(
    data=[
        ("seq1", "ATGAAGG-TG--"),
        ("seq2", "ATG-AGGTGATG"),
        ("seq3", "ATGAAG--GATG"),
    ],
    moltype="dna",
)
seq_to_aln_map = aln.get_gapped_seq("seq1").gap_maps()[0]


# In[66]:


seq_to_aln_map[3]
seq_to_aln_map[8]


# In[67]:


aln_to_seq_map = aln.get_gapped_seq("seq1").gap_maps()[1]
aln_to_seq_map[3]
aln_to_seq_map[8]


# In[68]:


seq_pos = aln_to_seq_map[7]


# In[69]:


aln = make_aligned_seqs(
    data=[
        ("seq1", "ATGAA---TG-"),
        ("seq2", "ATG-AGTGATG"),
        ("seq3", "AT--AG-GATG"),
    ],
    moltype="dna",
)
aln.omit_gap_runs(2)


# In[70]:


aln = make_aligned_seqs(
    data=[
        ("seq1", "ATGAA---TG-"),
        ("seq2", "ATG-AGTGATG"),
        ("seq3", "AT--AG-GATG"),
    ],
    moltype="dna",
)
aln.omit_gap_pos(0.40)


# In[71]:


aln = make_aligned_seqs(
    data=[
        ("seq1", "ATGAA------"),
        ("seq2", "ATG-AGTGATG"),
        ("seq3", "AT--AG-GATG"),
    ],
    moltype="dna",
)
filtered_aln = aln.omit_gap_seqs(0.50)
filtered_aln


# In[72]:


filtered_aln.omit_gap_pos()

