#!/usr/bin/env python
# coding: utf-8

# In[1]:


import set_working_directory


# In[2]:


from cogent3.core.annotation_db import BasicAnnotationDb

anno_db = BasicAnnotationDb()
anno_db


# In[3]:


from cogent3 import load_annotations

gff_db = load_annotations(path="data/mycoplasma-genitalium.gff")
gff_db


# In[4]:


from cogent3 import load_annotations

gb_db = load_annotations(path="data/mycoplasma-genitalium.gb")
gb_db


# In[5]:


summary = gff_db.describe
summary


# In[6]:


anno_db.add_feature(
    seqid="NC_000908",
    biotype="gene",
    name="interesting_gene",
    spans=[(1, 4)],
    strand="+",
)
anno_db.describe


# In[7]:


gff_db.add_feature(
    seqid="seq1",
    biotype="gene",
    name="interesting_gene",
    spans=[(1, 4)],
    strand="+",
)
gff_db.describe[-2:, :]  # showing just last two rows


# In[8]:


mg_16s = list(
    gb_db.get_features_matching(
        name="MG_RS00775", biotype="gene", seqid="NC_000908"
    )
)
mg_16s


# In[9]:


pseudogenes = list(gff_db.get_features_matching(biotype="pseudogene"))
pseudogenes[:2]  # showing just the first two


# In[10]:


operon_cds = list(
    gff_db.get_features_matching(start=220600, end=229067, biotype="CDS")
)
operon_cds


# In[11]:


replication_records = list(
    gff_db.get_records_matching(attributes="replication", biotype="CDS")
)
replication_records[0]  # showing just the first match


# In[12]:


gb_db.num_matches(biotype="gene")


# In[13]:


total_genes = gb_db.count_distinct(biotype="gene", name=True)
single_copy = total_genes[total_genes.columns["count"] == 1, :]
len(single_copy)


# In[14]:


total_genes = gff_db.num_matches(biotype="gene")
print("total genes: ", total_genes)
genes = gff_db.count_distinct(biotype="gene", name=True)
single_copy = genes[genes.columns["count"] == 1, :]
print("single copy genes: ", len(single_copy))


# In[15]:


children = list(gff_db.get_feature_children(name="gene-MG_RS00035"))
children


# In[16]:


parents = list(gff_db.get_feature_parent(name="cds-WP_009885556.1"))
parents


# In[17]:


gff_db.compatible(anno_db)


# In[18]:


gff_db.compatible(gb_db)


# In[19]:


union_db = gb_db.union(anno_db)
union_db.describe[-2:, :]


# In[20]:


gff_db.update(anno_db)
gff_db.describe[-2:, :]


# In[21]:


from cogent3.core.annotation_db import GenbankAnnotationDb

new_gb_db = GenbankAnnotationDb(source="m-genitalium-database.gbdb", db=anno_db)
new_gb_db


# In[22]:


from cogent3 import load_annotations

gff_db = load_annotations(path="data/mycoplasma-genitalium.gff")
just_cds = gff_db.subset(biotype="CDS")
just_cds.describe


# In[23]:


from cogent3 import make_seq

seq1 = make_seq(
    "AAGAAGAAGACCCCCAAAAAAAAAATTTTTTTTTTAAAAAGGGAACCCT",
    name="NC_000908",
    moltype="dna",
)

seq1.annotation_db = anno_db
seq1.annotation_db


# In[24]:


from cogent3 import load_seq

gb_seq = load_seq("data/mycoplasma-genitalium.gb")
gb_seq.annotation_db


# In[25]:


gff_seq = load_seq(
    "data/mycoplasma-genitalium.fa",
    annotation_path="data/mycoplasma-genitalium.gff",
)
gff_seq.annotation_db


# In[26]:


seq = load_seq(
    "data/mycoplasma-genitalium.fa",
    annotation_path="data/mycoplasma-genitalium.gff",
    label_to_name=lambda x: x.split()[0],
)
seq.annotation_db


# In[27]:


import pathlib

# clean up files

path = pathlib.Path("m-genitalium-database.gbdb")
path.unlink()

