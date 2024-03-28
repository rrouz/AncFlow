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

**Get Started:**

* Create a FASTA file containing at least 50 intentionally curated protein sequences. We recommend using sequences from protein families found in Pfam (https://pubmed.ncbi.nlm.nih.gov/26673716/) or UniProt (https://www.uniprot.org/) databases for optimal results.
* Using custom sequences is possible, however you may encounter parsing errors requiring manual correction.

## AncFlow And Protein Structure Prediction
AncFlow output ancestral sequences reconstructions are inteded for use by protein model prediction tools, like AlphaFold2, resolving the tertiary  structures of target nodes by their respective ancestral sequences.

![Predicted Ancestral Structures](https://previews.dropbox.com/p/thumb/ACNo3FJEo04EDbVirA7hNwYPVw_bRTQiyhVfqO74IBzn-YrpJbAS1ZTaM54RNWYKQ-uBXEMRCkKdYvOW35xjs9GN_xxbcCj4FTlvNx7ZJGkqQw4omEeAR91PhV0u9NLBig08LPTIV99LyyN383-Fa8_wmhlT0fY72rD-5fretunxV4IJpMooVZEbSSBhYmvzEZnvME9Mu58eGgv1awmPcPkR_bveU0ULb6WuTyLlqnXQ8kss0qBPgLif5I3U0u1icnTsd1ECGyB_oJGRtRpCK_zv7XWfintnSTu_fWp2FB-udaN3i50DqmN64D_zjURFWkMDMH7Pz0rjMxAtaea1Pz4ZYlpt5BkXGmjP1ZG779t4fLQvS2Ue5P9LsKM5qzV6pPk1BykHqUoWf7VBTA5bgVVXObVTMCylYzv9UZfzazZYZKR9WAeIU-ZACTClBe-IPdoNUdenCALInEdGsJaW7o20WtPx0HiPX5FU6a_pY2DituaQcqV2qA_pNf8FDQSWA-CE-PP0taYizHieA7dU0IPDOAjy2v_Jzlm9yCGCD3lFNaKJZFUvKPXjqcYrWzQDRY-GOyjTQ5GiKUImhHWku49rf8JE3E7fUFiKj5Ur-_9mXKras8REuOxFxf-hKFrE9gpbgBhBAiaaaDwrsLDx8NrtuEclJxqvjc2iw6m6BeidgcxwxJa2DQ1NnrGTNYRxvrlw5LVU5jwGYuhq-ZjFM6MQaNHt6AdyXAkMmIzp4LF6JiIKCJCMTHmtEXABxKkMqyMeMzJuKVKZohMc5WCym-nVBDfZQOYSNKxAFIK4FunJvvWcHzw9LFxLAdyQg3hQKFHW6UIi1APgysoY9gTihp4qY74icb8C3zHEBJgxReNvpErYrXoxn5gXQLrSyn_gMWZ9RIxn3-ufaQFJtrn8nRaP9qz5HurdtXTX5Xof4k3trDB5JIdC89bBT4iFbgpB-cdLOw69DUdeAq-E-5fUKbVss66oGgDXNU7rzlm53-tHM65wHPcix01P8ABhMri6rBBdGllpQvjq77YUSzNlQK_RhmLlkIHgqf9TMhAIHKa2Lg/p.gif)



