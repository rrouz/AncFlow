#Snakefile for Protein Sequence Reconstruction Pipeline
#rule all:
#    input:
#        "IQ-TREE_output.nwk"

#Step 1: Prepare Sequences
rule seq_prep:
    input:
        "protein_sequences.fasta"
    output:
        modified="modified_protein_sequences.fasta"
    run:
        with open(input[0], "r") as infile, open(output.modified, "w") as outfile:
            header = ""
            sequence = ""
            for line in infile:
                if line.startswith(">"):
                    if header:
                        processed_header = header.split("|")[0] + "|" + header.split("|")[1] + "|" + ".".join(header.split("|")[2].split(".")[:2])
                        outfile.write(f">{processed_header}\n{sequence}\n")
                    header = line[1:].replace("_", ".").replace(" ", ".").replace(":", "-").replace("/", ".").replace('"', ".").replace("-", ".")
                    sequence = ""
                else:
                    sequence += line.strip()

#Step 2: Generate MSA
rule msa:
    input:
        "modified_protein_sequences.fasta"
    output: 
        "aligned_protein_sequences.fasta"
    shell:
        "mafft --auto {input} > {output}"

#ARTIFACT // Step 2: Phylogenetic Tree Inference w/MrBayes
#rule run_mrbayes:
#    input:
#        "aligned_protein_sequences.fasta"  # Replace with your input file
#    output:
#        "mrbayes_output.nex"  # Replace with your desired output file
#    shell:
#        "mb {input} > {output}"


#ARTIFACT // Step 2: Phylogenetic Tree Inference w/RAxML
#rule infer_protein_tree:
#    input:
#        "aligned_protein_sequences.fasta"
#    output:
#        "RAxML_bestTree.AUTO"
#    shell:
#        "raxmlHPC -f a -x 12345 -p 12345 -m PROTGAMMAAUTO -N 250 -n RAxML_bestTree -s {input}" #"raxmlHPC -p 12345 -m PROTGAMMAAUTO -s {input} -n AUTO"

#Step 3: Phylogenetic Tree Inference w/IQ-TREE
rule iqtree:
    input:
        "aligned_protein_sequences.fasta"
    output:
        "IQ-TREE_output.treefile"
    shell:
        "iqtree -s {input} -m LG+G+F -bb 1000 -nt AUTO -pre IQ-TREE_output"

#Step 4: Converting to Newick
rule convert_to_nwk:
    input:
        "IQ-TREE_output.treefile"
    output:
        "IQ-TREE_output.nwk"
    shell:
        "mv {input} {output}"

#ARTIFACT // Step 3: Setup AutoPhy (installation of Autophy)
#rule setup_autophy:
#    input:
#        "IQ-TREE_output.nwk"
#    output:
#        "autophy_env_created.txt"
#    shell:
#        """
#        conda create -y -n autophy python=3.8
#        source activate autophy
#        pip install 'autophy @ git+https://github.com/aortizsax/autophy@main'
#        """

#Step 3a: Activate Autophy
rule activate_autophy:
    input:
        "IQ-TREE_output.nwk"
    shell:
        """
        echo "Running Autophy..."
        conda run -n autophy /bin/bash -c 'autophy -t IQ-TREE_output.nwk -id autophy -d monophyletic  -o clustered'
        """

#Step 5: Autophy Tree Renamer
rule rename_tree_file:
    output:
        "output/autophy_tree.nwk"
    shell:
        """
        python - <<EOF
import os

def rename_tree_file(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".tree"):
            new_name = "autophy_tree.nwk"
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))
            break  #Stop after renaming the first .tree file found

directory = "output/"

rename_tree_file(directory)
EOF
        """

rule subtree_extractor:
    input:
        "output/autophy_tree.nwk",
    output:
        "subtree_sequences.fasta",
    shell:
        """
        python scripts/subtree_extractor.py
        """

rule subtree_seq_prep:
    input:
        "subtree_sequences.fasta"
    output:
       modified="modified_subtree_sequences.fasta"
    script:
        "scripts/subtree_seq_prep.py"

rule subtree_msa:
    input:
        "modified_subtree_sequences.fasta"
    output: 
        "aligned_subtree_sequences.fasta"
    shell:
        "mafft --auto {input} > {output}"

#rule subtree_iqtree:
#    input:
#        "aligned_subtree_sequences.fasta"
#    output:
#        "IQ-TREE_subtree_output.treefile"
#    shell:
#        "iqtree -s {input} -m LG+G+F -bb 1000 -nt AUTO -pre IQ-TREE_subtree_output"
#
#rule subtree_convert_to_nwk:
#    input:
#        "IQ-TREE_subtree_output.treefile"
#    output:
#        "IQ-TREE_subtree_output.nwk"
#    shell:
#        "mv {input} {output}"
#
#rule activate_autophy_subtree:
#    input:
#        "IQ-TREE_subtree_output.nwk"
#    shell:
#        """
#        echo "Running Autophy..."
#        conda run -n autophy /bin/bash -c 'autophy -t IQ-TREE_subtree_output.nwk -id autophy -d monophyletic  -o clustered'
#        """
#
#rule rename_subtree_file:
#    output:
#        "output/autophy_subtree.nwk"
#    shell:
#        """
#        python - <<EOF
#import os
#
#def rename_tree_file(directory):
#    for filename in os.listdir(directory):
#        if filename.endswith(".tree"):
#            new_name = "autophy_subtree.nwk"
#            os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))
#            break  #Stop after renaming the first .tree file found
#
#directory = "output/"
#
#rename_tree_file(directory)
#EOF
#        """

#Step 6: Re-label MSA taxon
#rule autophy_msa:
#    input:
#        tree_file="output/autophy_tree.nwk",
#        msa_file="aligned_protein_sequences.fasta"
#    output:
#        output_msa="autophy_msa.fasta"
#    shell:
#        """
#        python scripts/autophy_msa_script.py {input.tree_file} {input.msa_file} {output.output_msa}
#        """

#Step 7: IQ-TREE Ancestral Sequence Reconstruction
#rule iqtree_asr:
#    input:
#        tree_file="output/autophy_tree.nwk",
#        protein_alignment="autophy_msa.fasta"
#    output:
#        "autophy_msa.fasta.state"
#    shell:
#        """
#        iqtree -s {input.protein_alignment} -st AA -nt AUTO -te {input.tree_file} -m MFP+MERGE -asr
#        """

#Step 8: Re-format Ancestral Sequences Into Fasta
#rule anc_fasta:
#    input:
#        tsv_file="autophy_msa.fasta.state"
#    output:
#        fasta_file="ancestral_node_sequences.fasta"
#    shell:
#        "python scripts/tsv_fasta.py {input.tsv_file} {output.fasta_file}"

#ARTIFACT // Sequence Combination and MSA   
#rule anc_msa:
#    input:
#        ancestral_fasta="ancestral_node_sequences.fasta",
#        protein_fasta="modified_protein_sequences.fasta"
#    output:
#        combined_fasta="combined_sequences.fasta"
#    params:
#        mafft_output="combined_msa.fasta"
#    shell:
#        """
#        cat {input.ancestral_fasta} {input.protein_fasta} > {output.combined_fasta}
#        mafft {output.combined_fasta} > {params.mafft_output}
#        """

#ARTIFACT // rule anc_iqtree:
#    input:
#        "combined_msa.fasta"
#    output:
#        "IQ-TREE_anc.treefile"
#    shell:
#        "iqtree -s {input} -m LG+G+F -bb 1000 -nt AUTO -pre IQ-TREE_anc"

#ARTIFACT // Step 4: Ancestral Reconstruction w/ARPIP
#include link to how to install ARPIP
#rule arpip:
#    shell:
#        """
#        ./../bpp-arpip/ARPIP params="conf.txt"
#        """

