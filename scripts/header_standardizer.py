import os
import re

def replace_fasta_headers_with_newick_samples(newick_file_path, fasta_file_path):
    """
    Replaces FASTA sample names in header lines with corresponding sample names from a Newick tree file,
    using accession numbers for matching and the specified extraction logic for sample names.

    Args:
        newick_file_path (str): Path to the Newick tree file.
        fasta_file_path (str): Path to the FASTA file.
    """

    newick_samples_by_accession = {}
    with open(newick_file_path, "r") as newick_file:
        for line in newick_file:
            for sample in line.split(","):
                sample_name = re.search(r"s(.*?):", sample).group(1)
                parts = sample_name.split("_")
                if "." in parts[1]:
                    accession = parts[1].split(".")[0]
                else:
                    accession = parts[1]
                newick_samples_by_accession[accession] = ">s" + sample_name


    temp_output_file_path = fasta_file_path + ".temp"
    with open(fasta_file_path, "r") as fasta_file, open(temp_output_file_path, "w") as output_file:
        for line in fasta_file:
            if line.startswith(">"):
                original_sample = line.strip()[1:]
                accession = original_sample.split("|")[1]
                if accession in newick_samples_by_accession:
                    output_file.write(f"{newick_samples_by_accession[accession]}\n")
                else:
                    print(f"Warning: Accession '{accession}' not found in Newick tree.")
                    output_file.write(line)
            else:
                output_file.write(line)

    os.replace(temp_output_file_path, fasta_file_path)
    print(f"FASTA headers replaced successfully in {fasta_file_path}!")

def main():
    input_directory = "subtrees"

    for filename in os.listdir(input_directory):
        if filename.endswith(".nwk"):
            newick_file_path = os.path.join(input_directory, filename)
            fasta_filename = filename.replace(".nwk", ".fasta")
            fasta_file_path = os.path.join(input_directory, fasta_filename)
            
            if os.path.exists(fasta_file_path):
                replace_fasta_headers_with_newick_samples(newick_file_path, fasta_file_path)
                print(f"Processing {filename} completed.")
            else:
                print(f"Warning: Corresponding FASTA file '{fasta_filename}' not found for '{filename}'. Skipping.")

if __name__ == "__main__":
    main()
