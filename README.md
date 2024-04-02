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
snakemake -n
```

6. Run pipeline, where -j(number of cores 1-4):
```bash
snakemake -j2
```

## Installation for Windows
For Windows users, it is recommended to utilize Windows Subsystem for Linux (WSL) along with Miniconda. 


1. Install WSL by following the official Microsoft documentation: [Install WSL](https://docs.microsoft.com/en-us/windows/wsl/install)

2. Install Miniconda within your WSL environment: [Install Miniconda](https://conda.io/projects/conda/en/latest/user-guide/install/windows.html)

3. Follow the installation steps for Mac/Linux


## Installation Troubleshooting
If you encounter difficulties, or error messages in pipeline setup we recommend using miniconda, with a conda version of 24.1.2 or newer. Additionally, when doing so completely remove your existing AncFlow conda environment and re-create a fresh environment after instllation of the newer conda version. 

# Basic Usage
![Workflow](https://i.imgur.com/Pp7OdYk.jpg)

**Getting Started:**

Create a FASTA file containing at least 50 intentionally curated protein sequences. For a seamless run use Swiss-Prot sequences of protein families found in the [Pfam](https://pubmed.ncbi.nlm.nih.gov/26673716/) or [UniProt](https://www.uniprot.org/) databases that follow the following header format: 
* Using custom sequences is possible, however you may encounter parsing errors requiring manual correction of the sequence headers.
```bash
>sp|P45996.1|OMP53_HAEIF RecName: Full=Outer membrane protein P5; Short=OMP P5; AltName: Full=Fimbrin; AltName: Full=Outer membrane porin A; AltName: Full=Outer membrane protein A; Flags: Precursor

Database Source: Swiss-Prot (sp)
Accession Number: Sequence identifier (P45996.1)
Identifier: Often the protein name or shorthand (OMP53_HAEIF)

It is critical that the sequence headers follow pipe delimited structure above.
```

**Interpretting Autophy:**

After IQ-TREE has inferred the phylogeny of your sequences, AutoPhy will attempt to cluster and resolve novel subfamilies. Upon successful completion AutoPhy will create an output directory with the monophyletically clustered trees. At this point we recommend analyzing the autophy outputs for clades of interest and to take note of their clade sizes as you will be prompted for the minimum retained clade size (this is a number typically larger than 2) for downstream subtree extraction.  

Acyltransferace family tree colored and clustered by AutoPhy: 
![Acyltransferace Sample Tree](https://github.com/rrouz/AncFlow/blob/main/sample_runs/acyltransferaces/output/2024-02-16_3_EMClust_monophyleticautophy_precomputed_coloredtree.svg)

For example, clades 11.0 and 31 are of particular interest for downstream ancestral sequence reconstruction. Therefore, to capture them, the minimum prompted clade size should be set to a value less than or equal to 5. The colored nodes depict the ancestral sequences of these target clades, whose sequences were later derived from the pipeline and used to predict the superimposed structures below.
![Target Clade](https://i.imgur.com/lMhZzpf.jpeg)
![Predicted Ancestral Structures](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNzQ1dnlhNGlwaWRnZ2EzajR0c2cwNnEwN3JsYmc0MTU5dTV2eDUzaSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/LFf30BXqYICQtcy9DX/giphy-downsized-large.gif)

**Ancestral Sequence Reconstruction:**

The extracted subtree and respective MSA are used as input for GRASP via BNKIT. GRASP employs statistical models and maximum likelihood approaches to infer the most likely ancestral sequences at internal nodes of the subtree.


## AncFlow and Protein Structure Prediction
Ancestral sequences reconstructions can be use by protein model prediction tools, like AlphaFold2, to approximate the tertiary structures of target nodes by their derived sequences.



