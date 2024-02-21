# AncFlow
AncFlow is a comprehensive snakemake driven pipeline designed to perform ancestral sequence reconstruction upon the immediate parent nodes of AutoPhy clustered phylogenetic trees. AncFlow is fed protein sequence data which undergo multiple sequence alignment via MAFFT. A phylogenetic tree is then inferred using IQ-TREE. Afterwhich, monophyletic clustering of the previously inferred phylogenetic tree is achieved through the use of Autophy. Size defined cladistic subtrees are then extracted utilized to achieve ancestral sequence reconstruction of immediate parent nodes. To execute this pipeline, users need to install and have proficiency with Snakemake, MAFFT, IQ-TREE, Conda, and Autophy.

## Dependencies
Before running the pipeline, ensure you have the following software installed:

- [MAFFT](https://mafft.cbrc.jp/alignment/software/) - Multiple sequence alignment tool.
- [IQ-TREE](http://www.iqtree.org/) - Phylogenetic tree inference software.
- [Conda](https://conda.io/projects/conda/en/latest/index.html) - Package and environment management system.
- [AutoPhy](https://github.com/aortizsax/autophy) - Ancestral sequence reconstruction tool.
