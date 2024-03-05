# AncFlow
AncFlow is a comprehensive snakemake driven pipeline designed to perform ancestral sequence reconstruction upon the immediate parent nodes of AutoPhy clustered phylogenetic trees. AncFlow is fed protein sequence data which undergo multiple sequence alignment via MAFFT. A phylogenetic tree is then inferred using IQ-TREE. Afterwhich, monophyletic clustering of the previously inferred phylogenetic tree is achieved through the use of AutoPhy. Size defined cladistic subtrees are all extracted and utilized to create the respective ancestral sequence reconstruction of immediate parent nodes.

## Docker Installation

Coming Soon.

## Manual Installation

### Dependencies
Before running the pipeline, ensure you have the following software,tools, and libraries installed in order:

- [AutoPhy](https://github.com/aortizsax/autophy) - Monophyletic clustering tool.
- [Snakemake](https://snakemake.readthedocs.io/en/stable/getting_started/installation.html) - Workflow management system.
- [MAFFT](https://mafft.cbrc.jp/alignment/software/) - Multiple sequence alignment tool.
- [IQ-TREE](http://www.iqtree.org/) - Phylogenetic tree inference software.
- [GRASP](https://github.com/bodenlab/GRASP) - Ancestral sequence reconstruction software.

### First Run
Upon the proper installation of all dependencies, execute the following command to run the pipeline.
```bash
snakemake asr -c4
```



