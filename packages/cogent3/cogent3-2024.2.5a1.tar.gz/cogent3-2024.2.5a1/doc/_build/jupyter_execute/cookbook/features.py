#!/usr/bin/env python
# coding: utf-8

# In[1]:


import set_working_directory


# In[2]:


from cogent3 import make_seq

# create an example sequence
seq = make_seq(
    "GCCTAATACTAAGCCTAAGCCTAAGACTAAGCCTAATACTAAGCCTAAGCCTAAGACTAA",
    name="seq1",
    moltype="dna",
)

# Add a feature
seq.add_feature(biotype="gene", name="a_gene", spans=[(12, 48)], seqid="seq1")


# In[3]:


# Add a feature as a series
seq.add_feature(
    biotype="cpgsite",
    name="a_cpgsite",
    spans=[(12, 18), (21, 29), (35, 48)],
    seqid="seq1",
)


# In[4]:


from cogent3 import make_aligned_seqs

# make demo alignment
aln1 = make_aligned_seqs(
    data=[["seq1", "-AAACCCCCA"], ["seq2", "TTTT--TTTT"]], array_align=False
)
# add feature to seq1
aln1.add_feature(
    seqid="seq1", biotype="exon", name="A", spans=[(3, 8)], on_alignment=False
)


# In[5]:


from cogent3 import make_aligned_seqs

# make demo alignment
aln1 = make_aligned_seqs(
    data=[["seq1", "-AAACCCCCA"], ["seq2", "TTTT--TTTT"]], array_align=False
)

aln1.add_feature(
    biotype="exon",
    name="aligned_exon",
    spans=[(0, 8)],
    on_alignment=True,
)


# In[6]:


from cogent3 import make_seq
from cogent3.core.annotation_db import BasicAnnotationDb

# init empty db and add feature
db = BasicAnnotationDb()
db.add_feature(seqid="seq1", biotype="exon", name="C", spans=[(45, 48)])

# make demo seq
s1 = make_seq(
    "AAGAAGAAGACCCCCAAAAAAAAAATTTTTTTTTTAAAAAGGGAACCCT", name="seq1", moltype="dna"
)

# assign db to sequence
s1.annotation_db = db
s1.annotation_db


# In[7]:


from cogent3 import load_seq

get_ipython().run_line_magic('timeit', 'load_seq("data/C-elegans-chromosome-I.gb", moltype="dna")')


# In[8]:


seq = load_seq("data/C-elegans-chromosome-I.gb", moltype="dna")


# In[9]:


seq.annotation_db


# In[10]:


from cogent3 import load_seq

seq = load_seq(
    filename="data/C-elegans-chromosome-I.fa",
    annotation_path="data/C-elegans-chromosome-I.gff",
    moltype="dna",
)
seq.annotation_db


# In[11]:


from cogent3 import load_seq

seq = load_seq(
    "data/C-elegans-chromosome-I.fa",
    annotation_path="data/C-elegans-chromosome-I.gff",
    label_to_name=lambda x: x.split()[0],
    moltype="dna",
)
seq.annotation_db


# In[12]:


from cogent3 import load_seq

loaded_seq = load_seq(
    "data/C-elegans-chromosome-I.fa",
    label_to_name=lambda x: x.split()[0],
    moltype="dna",
)


# In[13]:


# loaded_seq = < loaded / created the seq>
loaded_seq.annotate_from_gff("data/C-elegans-chromosome-I.gff")
loaded_seq.annotation_db


# In[14]:


from cogent3 import make_seq

sub_seq = make_seq(
    "GCCTAATACTAAGCCTAAGCCTAAGACTAAGCCTAATACTAAGCCTAAGCCTAAGACTAAGCCTAAGACTAAGCCTAAGA",
    name="I",
    moltype="dna",
)


# In[15]:


# sub_seq = <genomic region starting at the 600th nt>
sub_seq.annotate_from_gff("data/C-elegans-chromosome-I.gff", offset=600)
sub_seq.annotation_db


# In[16]:


from cogent3 import load_aligned_seqs

brca1_aln = load_aligned_seqs(
    "data/primate_brca1.fasta", array_align=False, moltype="dna"
)
brca1_aln


# In[17]:


brca1_aln.annotate_from_gff("data/brca1_hsa_shortened.gff", seq_ids=["Human"])
brca1_aln.annotation_db


# In[18]:


brca1_aln.get_seq("Human").annotation_db


# In[19]:


from cogent3 import load_seq

seq = load_seq("data/C-elegans-chromosome-I.gb", moltype="dna")

# note we wrap `get_features` in `list` as generator is returned
gene = list(seq.get_features(name="WBGene00021661", biotype="gene"))
gene


# In[20]:


from cogent3 import load_seq

seq = load_seq("data/C-elegans-chromosome-I.gb", moltype="dna")
cds = list(seq.get_features(biotype="CDS"))
cds[:3]


# In[21]:


cds = list(seq.get_features(biotype="CDS", name="WBGene00021661"))
cds


# In[22]:


from cogent3 import load_seq

seq = load_seq("data/C-elegans-chromosome-I.gb", moltype="dna")
region_features = list(seq.get_features(start=10148, stop=26732))
region_features[:3]


# In[23]:


mRNA = list(seq.get_features(start=10148, stop=29322, biotype="mRNA"))[0]
mRNA


# In[24]:


from cogent3 import load_aligned_seqs

# first load alignment and annotate the human seq
aln = load_aligned_seqs(
    "data/primate_brca1.fasta", array_align=False, moltype="dna"
)
aln.annotate_from_gff("data/brca1_hsa_shortened.gff", seq_ids=["Human"])

# query alignment providing seqid of interest
human_exons = list(aln.get_features(biotype="exon", seqid="Human"))
human_exons


# In[25]:


from cogent3 import make_aligned_seqs

# add a feature to the alignment we created above on difference sequence
aln.add_feature(biotype="gene", name="gene:101", spans=[(40, 387)], seqid="Rhesus")

any_feature = list(aln.get_features(on_alignment=False))
any_feature


# In[26]:


from cogent3 import make_aligned_seqs

# first we add the feature to the alignment
aln.add_feature(
    biotype="pseudogene", name="pseudogene1", spans=[(420, 666)], on_alignment=True
)

# query for features on the alignment
aln_features = list(aln.get_features(on_alignment=True))
aln_features


# In[27]:


from cogent3 import make_aligned_seqs

aln3 = make_aligned_seqs(
    data=[["x", "C-CCCAAAAA"], ["y", "-T----TTTT"]],
    array_align=False,
    moltype="dna",
)
exon = aln3.add_feature(
    seqid="x", biotype="exon", name="ex1", spans=[(0, 4)], on_alignment=False
)
exon.get_slice()


# In[28]:


aln_exons = list(aln3.get_features(seqid="x", biotype="exon"))[0]
aln_exons


# In[29]:


exon.get_slice(allow_gaps=True)


# In[30]:


from cogent3 import load_seq

seq = load_seq(
    "data/C-elegans-chromosome-I.fa",
    annotation_path="data/C-elegans-chromosome-I.gff",
    label_to_name=lambda x: x.split()[0],
    moltype="dna",
)
pseudogene = list(seq.get_features(start=10148, stop=26732, biotype="pseudogene"))[0]
seq[pseudogene]


# In[31]:


pseudogene.get_slice()


# In[32]:


from cogent3 import load_seq

seq = load_seq("data/C-elegans-chromosome-I.gb", moltype="dna")
subseq = seq[25000:35000]
fig = subseq.get_drawable(biotype=("gene", "mRNA", "CDS", "misc_RNA"))
fig.show()


# In[33]:


pseudogene.get_coordinates()


# In[34]:


from cogent3 import load_seq

seq = load_seq("data/C-elegans-chromosome-I.gb", moltype="dna")
cds = list(seq.get_features(biotype="CDS"))[0]
exon_coords = cds.get_coordinates()

exon_coords


# In[35]:


intron_coords = []

for i in range(len(exon_coords) - 1):
    intron_coords.append((exon_coords[i][1], exon_coords[i + 1][0]))

intron_coords


# In[36]:


intron = seq.add_feature(
    biotype="intron", name="intron:Y74C9A.3.1", seqid="I", spans=intron_coords
)
intron


# In[37]:


from cogent3 import load_seq

seq = load_seq("data/C-elegans-chromosome-I.gb", moltype="dna")
cds = list(seq.get_features(biotype="CDS"))
union_cds = cds[0].union(cds[1:])


# In[38]:


from cogent3 import load_seq

seq = load_seq("data/C-elegans-chromosome-I.gb", moltype="dna")
genes = list(seq.get_features(biotype="gene"))
genes = genes[0].union(genes[1:])
genes


# In[39]:


intergenic = genes.shadow()
intergenic


# In[40]:


intergenic.get_slice()


# In[41]:


from cogent3 import load_seq

seq = load_seq("data/C-elegans-chromosome-I.gb", moltype="dna")
no_cds = seq.with_masked_annotations("CDS")
no_cds[2575800:2575900]


# In[42]:


from cogent3 import make_aligned_seqs

aln = make_aligned_seqs(
    data=[["x", "C-CCCAAAAAGGGAA"], ["y", "-T----TTTTG-GTT"]],
    moltype="dna",
    array_align=False,
)
exon = aln.add_feature(
    seqid="x",
    biotype="exon",
    name="exon-be-gone",
    spans=[(0, 4)],
    on_alignment=False,
)
aln.with_masked_annotations("exon", mask_char="?")


# In[43]:


rc = aln.rc()
rc


# In[44]:


rc.with_masked_annotations("exon", mask_char="?")


# In[45]:


from cogent3 import load_seq

seq = load_seq(
    "data/C-elegans-chromosome-I.fa",
    annotation_path="data/C-elegans-chromosome-I.gff",
    label_to_name=lambda x: x.split()[0],
    moltype="dna",
)
gene = list(seq.get_features(name="gene:WBGene00022276", biotype="gene"))[0]
children = list(gene.get_children())
children


# In[46]:


child = list(seq.get_features(name="transcript:Y74C9A.2a.3", biotype="mRNA"))[0]
parent = list(child.get_parent())
parent


# In[47]:


aln2 = make_aligned_seqs(
    data=[["x", "-AAAAAAAAA"], ["y", "TTTT--TTTT"]],
    array_align=False,
    moltype="dna",
)
x, y = aln2.get_seq("x"), aln2.get_seq("y")
x.annotation_db is y.annotation_db is aln2.annotation_db


# In[48]:


seq = make_seq("CCCCCCCCCCCCCCCCCCCC", name="x", moltype="dna")
match_exon = seq.add_feature(biotype="exon", name="A", spans=[(3, 8)])
aln2.copy_annotations(seq.annotation_db)
aln2.annotation_db


# In[49]:


copied = list(aln2.get_features(seqid="x", biotype="exon"))
copied


# In[50]:


unified = aln_exons.as_one_span()
aln3[unified]


# In[51]:


plus = make_seq("CCCCCAAAAAAAAAATTTTTTTTTTAAAGG", moltype="dna")
plus_rpt = plus.add_feature(biotype="blah", name="a", spans=[(5, 15), (25, 28)])
plus[plus_rpt]


# In[52]:


minus = plus.rc()
minus


# In[53]:


minus_rpt = list(minus.get_features(biotype="blah"))[0]
minus[minus_rpt]

