# AncFlow
AncFlow is a comprehensive snakemake driven pipeline designed to perform ancestral sequence reconstruction upon the immediate parent nodes of AutoPhy clustered phylogenetic trees. AncFlow is fed protein sequence data which undergo multiple sequence alignment via MAFFT. A phylogenetic tree is then inferred using IQ-TREE. Afterwhich, monophyletic clustering of the previously inferred phylogenetic tree is achieved through the use of AutoPhy. Size defined cladistic subtrees are all extracted and utilized to create the respective ancestral sequence reconstruction of immediate parent nodes.

## Installation
1. Clone repository

2. Create conda environment:
```bash
conda env create -f environment.yml
```

3. Activate conda environment:
```bash
conda activate ancflow
```

4. Preform dry run:
```bash
snakemake -n
```

5. Navigate to directory containing Snakefile:
```bash
snakemake asr -j1
```


