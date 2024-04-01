rule all:
    input:
        "logs/asr_complete.txt"

#Step 1: Prepare Sequences
rule seq_prep:
  input:
    "protein_sequences.fasta"
  output:
    "logs/seq_prep_complete.txt"
  shell:
    """
    python scripts/seq_prep.py
    touch {output}
    """

#Step 2: Generate MSA
rule msa:
  input:
    "logs/seq_prep_complete.txt"
  output: 
    "logs/msa_complete.txt"
  shell:
    """
    python scripts/msa.py
    touch {output}
    """
#Step 3: Replace Undertermined Characters
rule msa_prep:
  input:
    "logs/msa_complete.txt"
  output:
    "logs/msa_prep_complete.txt"
  shell:
    """
    python scripts/msa_prep.py
    touch {output}
    """

#Step 4: Phylogenetic Tree Inference w/IQ-TREE
rule iqtree:
  input:
    "logs/msa_prep_complete.txt"
  output:
    "iqtree/IQ-TREE_output.treefile"
  shell:
    "iqtree -s alignments/aligned_protein_sequences.fasta -m LG+G+F -bb 1000 -nt AUTO -pre iqtree/IQ-TREE_output"

#Step 5: Converting to Newick
rule convert_to_nwk:
  input:
    "iqtree/IQ-TREE_output.treefile"
  output:
    "iqtree/IQ-TREE_output.nwk"
  shell:
    "mv {input} {output}"

#Step 6: Run Autophy
rule autophy:
  input:
    "iqtree/IQ-TREE_output.nwk"
  output:
    "logs/autophy_success.txt"
  shell:
    """
    echo "Running Autophy..."
    autophy -t {input} -id autophy -d monophyletic -o clustered
    touch {output} # Create the success file upon completion
    """

#Step 7: Autophy Tree Renamer
rule rename_tree_file:
  input:
    "logs/autophy_success.txt"
  output:
    "output/autophy_tree.nwk"
  conda:
    "autophy"
  shell:
    "python scripts/rename_tree_file.py"

# Step 8: Subtree Newick and Fasta Extractor
rule subtree_extractor:
  input:
    "output/autophy_tree.nwk"
  output:
    "logs/extraction_success.txt"
  shell:
    """
    python scripts/subtree_extractor.py
    touch {output}
    """

# Step 9: Subtree Sequence Preparation
rule subtree_seq_prep:
  input:
    "logs/extraction_success.txt"
  output:
    "logs/subtree_seq_prep_success.txt"
  shell:
    """
    python scripts/subtree_seq_prep.py
    touch {output}
    """

#Step 10: Subtree MSA
rule subtree_msa:
  input:
    "logs/subtree_seq_prep_success.txt"
  output: 
    "logs/aligned_autophy_subtree_sequences_success.txt"
  shell:
    """
    python scripts/mafft_msa.py
    touch {output}
    """

#Step 11: Header standardizer
rule header_standardizer:
  input:
    "logs/aligned_autophy_subtree_sequences_success.txt"
  output:
    "logs/completed_aligned_autophy_subtree_sequences_success.txt"
  shell:
    """
    python scripts/header_standardizer.py
    touch {output}
    """

#Step 12: Ancestral Sequence Reconstruction
rule asr:
  input:
    "logs/completed_aligned_autophy_subtree_sequences_success.txt"
  output:
    "logs/asr_complete.txt"
  shell:
    """
    python scripts/asr.py
    touch {output}
    """