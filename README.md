# AncFlow
AncFlow is a comprehensive snakemake driven pipeline designed to perform ancestral sequence reconstruction upon the immediate parent nodes of AutoPhy clustered phylogenetic trees. AncFlow is fed protein sequence data which undergo multiple sequence alignment via MAFFT, phylogenetic tree inferrence via IQ-TREE, and monophyletic clustering via AutoPhy. Size defined cladistic subtrees of immediate parent nodes are extracted from the clustered phylogenetic tree to resolve ancestral sequence reconstructions via bnkit.

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

6. Navigate to directory containing Snakefile:
```bash
snakemake asr -j1
```

## Installation for Windows
For Windows users, it's recommended to utilize Windows Subsystem for Linux (WSL) along with Miniconda. 


1. Install WSL by following the official Microsoft documentation: [Install WSL](https://docs.microsoft.com/en-us/windows/wsl/install)

2. Install Miniconda within your WSL environment: [Install Miniconda](https://conda.io/projects/conda/en/latest/user-guide/install/windows.html)

3. Follow the installation steps for Mac/Linux


## Troubleshooting
If you encounter difficulties we recommend using miniconda, with a conda version of 24.1.2 or newer.

