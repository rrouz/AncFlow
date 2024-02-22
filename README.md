# AncFlow
AncFlow is a comprehensive snakemake driven pipeline designed to perform ancestral sequence reconstruction upon the immediate parent nodes of AutoPhy clustered phylogenetic trees. AncFlow is fed protein sequence data which undergo multiple sequence alignment via MAFFT. A phylogenetic tree is then inferred using IQ-TREE. Afterwhich, monophyletic clustering of the previously inferred phylogenetic tree is achieved through the use of Autophy. Size defined cladistic subtrees are then extracted utilized to achieve ancestral sequence reconstruction of immediate parent nodes. To execute this pipeline, users need to install and have proficiency with Snakemake, MAFFT, IQ-TREE, Conda, and Autophy.

## Docker Installation

Coming Soon.

## Manual Installation

### Dependencies
Before running the pipeline, ensure you have the following software,tools, and libraries installed:

- [Snakemake](https://snakemake.readthedocs.io/en/stable/getting_started/installation.html) - Workflow management system.
- [MAFFT](https://mafft.cbrc.jp/alignment/software/) - Multiple sequence alignment tool.
- [IQ-TREE](http://www.iqtree.org/) - Phylogenetic tree inference software.
- [AutoPhy](https://github.com/aortizsax/autophy) - Monophyletic clustering tool.
- [GRASP](https://github.com/bodenlab/GRASP) - Ancestral sequence reconstruction software.

BioPython - install via pip:

```bash
pip install biopython
```



