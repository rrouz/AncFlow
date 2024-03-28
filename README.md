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

* Create a FASTA file containing at least 50 intentionally curated protein sequences. We recommend using sequences from protein families found in Pfam (https://pubmed.ncbi.nlm.nih.gov/26673716/) or UniProt (https://www.uniprot.org/) databases for optimal results.
* Using custom sequences is possible, however you may encounter parsing errors requiring manual correction.

## AncFlow And Protein Structure Prediction
AncFlow output ancestral sequences reconstructions are inteded for use by protein model prediction tools, like AlphaFold2, resolving the tertiary  structures of target nodes by their respective ancestral sequences.

![Predicted Ancestral Structures](https://jmp.sh/HarZWYGt)



