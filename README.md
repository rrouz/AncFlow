# AncFlow
AncFlow is a comprehensive snakemake driven pipeline designed to perform ancestral sequence reconstruction upon the immediate parent nodes of AutoPhy clustered phylogenetic trees. AncFlow is fed protein sequence data which undergo multiple sequence alignment via [MAFFT](https://github.com/GSLBiotech/mafft), phylogenetic tree inferrence via [IQ-TREE](https://github.com/iqtree/iqtree2), and monophyletic clustering via [AutoPhy](https://github.com/aortizsax/autophy). Size defined cladistic subtrees of immediate parent nodes are extracted from the clustered phylogenetic tree to resolve ancestral sequence reconstructions via [bnkit](https://github.com/bodenlab/bnkit).

## Installation for Mac/Linux
1. Clone repository
```bash
git clone https://github.com/rrouz/AncFlow.git
```

2. Enter directory
```bash
cd AncFlow
```

3. Create conda environment:
```bash
conda env create -f environment.yml
```

4. Activate conda environment:
```bash
conda activate ancflow
```

5. Perform dry run:
```bash
snakemake asr -n
```

6. Run pipeline, where -j(number of cores 1-4):
```bash
snakemake asr -j2
```

## Installation for Windows
For Windows users, it is recommended to utilize Windows Subsystem for Linux (WSL) along with Miniconda. 


1. Install WSL by following the official Microsoft documentation: [Install WSL](https://docs.microsoft.com/en-us/windows/wsl/install)

2. Install Miniconda within your WSL environment: [Install Miniconda](https://conda.io/projects/conda/en/latest/user-guide/install/windows.html)

3. Follow the installation steps for Mac/Linux


## Installation Troubleshooting
If you encounter difficulties, or error messages in pipeline setup we recommend using miniconda, with a conda version of 24.1.2 or newer. Additionally, when doing so completely remove your existing AncFlow conda environment and re-create a fresh environment after instllation of the newer conda version. 

# Basic Usage

**Getting Started:**

Create a FASTA file containing at least 50 intentionally curated protein sequences. We recommend using sequences from protein families found in the [Pfam](https://pubmed.ncbi.nlm.nih.gov/26673716/) or [UniProt](https://www.uniprot.org/) databases for optimal results.
* Using custom sequences is possible, however you may encounter parsing errors requiring manual correction.
For example:
```bash
>sp|P45996.1|OMP53_HAEIF RecName: Full=Outer membrane protein P5; Short=OMP P5; AltName: Full=Fimbrin; AltName: Full=Outer membrane porin A; AltName: Full=Outer membrane protein A; Flags: Precursor
MKKTAIALVVAGLAAASVA
>sp|P02935.1|OMPA_SHIDY RecName: Full=Outer membrane protein A; AltName: Full=Outer membrane porin A; Flags: Precursor
MKKTAIAITVALAGFATVA
>sp|O31101.1|SRPC_PSEPU RecName: Full=Solvent efflux pump outer membrane protein SrpC; Flags: Precursor
MKFKSLPMFALLMLGGCSL
>sp|O84879.1|PMPG_CHLTR RecName: Full=Probable outer membrane protein PmpG; AltName: Full=Polymorphic membrane protein G; Flags: Precursor
MQTSFHKFFLSMILAYSCC
>sp|P59570.1|OMPK_VIBPA RecName: Full=Outer membrane protein OmpK; Flags: Precursor
MRKSLLALSLLAATSAPVL

and so on
```

**Interpretting Autophy:**

After IQ-TREE has inferred the phylogeny of your sequences, AutoPhy will attempt to cluster and resolve novel subfamilies. Upon successful completion AutoPhy will create an output directory with the monophyletically clustered trees. At this point we recommend analyzing the autophy outputs for clades of interest and to take note of their clade sizes as you will be prompted for the minimum retained clade size (this is a number typically larger than 2) for downstream subtree extraction.  

Example Acyltransferace family tree: 
![Acyltransferace Sample Tree](https://github.com/rrouz/AncFlow/blob/grasp-based-asr/sample_runs/acyltransferaces/output/2024-02-16_3_EMClust_monophyleticautophy_precomputed_coloredtree.svg)

For my purposes clades 11.0, and 31 are of particular interest for downstream ancestral sequence reconstruction therefore I set the minimum prompted clade size to 5.

For Example:
![Retaining Clade Size](https://i.imgur.com/nOqLOMT.jpeg)

**Ancestral Sequence Reconstruction:**

EXPLAIN WHAT BNKIT IS DOING HOW ITS DOING IT AND WHAT CAN BE DONE WITH THE ASRS


## AncFlow And Protein Structure Prediction
AncFlow output ancestral sequences reconstructions are inteded for use by protein model prediction tools, like AlphaFold2, resolving the tertiary  structures of target nodes by their respective ancestral sequences.
![Predicted Ancestral Structures](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNzQ1dnlhNGlwaWRnZ2EzajR0c2cwNnEwN3JsYmc0MTU5dTV2eDUzaSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/LFf30BXqYICQtcy9DX/giphy-downsized-large.gif)



