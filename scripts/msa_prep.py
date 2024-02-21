def replace_x_with_dash(fasta_file):
    """Replaces "X" characters with "-" in sequences within a FASTA file and overwrites the original file."""

    with open(fasta_file, "r+") as file:
        contents = file.readlines()
        file.seek(0)
        file.truncate()  # Clear existing content

        in_header = True
        sequence_index = 0

        for line in contents:
            if line.startswith(">"):
                # Header line: write as is
                file.write(line)
                in_header = True
                sequence_index += 1
            else:
                # Sequence line: replace "X" with "-"
                new_line = line.replace("X", "-")
                if new_line != line:
                    print(f"Replaced 'X' with '-' at position {line.index('X') + 1} in sequence {sequence_index}")
                file.write(new_line)
                in_header = False

if __name__ == "__main__":
    fasta_file = "alignments/aligned_protein_sequences.fasta"
    replace_x_with_dash(fasta_file)
    print(f"Replacement completed and saved to {fasta_file}")
