import os
import glob

def convert_header(header):
    """
    Convert a header from FASTA format to UniProt format.

    Args:
        header (str): The header line from a FASTA file.

    Returns:
        str: The header line converted to UniProt format.
    """
    accession = header.split('.')[0]
    uniprot_header = f">tr|{accession}"
    return uniprot_header

def process_fasta_file(input_file, output_file):
    """
    Process a single FASTA file by converting headers to UniProt format and rewriting the file.

    Args:
        input_file (str): Path to the input FASTA file.
        output_file (str): Path to the output file with converted headers.
    """
    try:
        with open(output_file, "w") as outfile:
            with open(input_file, "r") as infile:
                header = ""
                sequence = ""
                for line in infile:
                    if line.startswith(">"):
                        if header:
                            uniprot_header = convert_header(header)
                            outfile.write(f"{uniprot_header}\n{sequence}\n")
                        header = line[1:].strip()
                        sequence = ""
                    else:
                        sequence += line.strip()

                if header:
                    uniprot_header = convert_header(header)
                    outfile.write(f"{uniprot_header}\n{sequence}\n")
        print(f"Processed file: {input_file}")

        os.rename(output_file, input_file)
    except Exception as e:
        print(f"Error processing file {input_file}: {e}")

directory = 'subtrees'

fasta_files = glob.glob(os.path.join(directory, '**/*.fasta'), recursive=True)
fasta_files.extend(glob.glob(os.path.join(directory, '**/*.fa'), recursive=True))

for fasta_file in fasta_files:
    process_fasta_file(fasta_file, f"{fasta_file}.temp")

print("Processing completed.")