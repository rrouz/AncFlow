import os

def perform_mafft_alignment(input_file, output_file):
    os.system(f"mafft --auto {input_file} > {output_file}")
    print(f"MAFFT alignment completed. Aligned sequences saved to {output_file}")

if __name__ == "__main__":
    input_file = "alignments/modified_protein_sequences.fasta"
    output_file = "alignments/aligned_protein_sequences.fasta"
    perform_mafft_alignment(input_file, output_file)
