import os
import glob
import shutil

def perform_msa(input_file):
    """Performs MSA on the input file and overwrites it with the aligned result.

    Args:
        input_file (str): Path to the input FASTA file.

    Raises:
        Exception: If an error occurs during MSA execution.
    """

    try:
        temp_output_file = input_file + "_temp"
        os.system(f"mafft --auto {input_file} > {temp_output_file}")
        shutil.move(temp_output_file, input_file)
        print(f"Processed file: {input_file}")
    except Exception as e:
        print(f"Error processing file {input_file}: {e}")

def main():
    """Searches for FASTA files in 'subtrees', performs MSA, and overwrites them."""
    directory = 'subtrees'
    fasta_files = glob.glob(os.path.join(directory, '**/*.fasta'), recursive=True)
    fasta_files.extend(glob.glob(os.path.join(directory, '**/*.fa'), recursive=True))
    for fasta_file in fasta_files:
        perform_msa(fasta_file)

if __name__ == "__main__":
    main()
