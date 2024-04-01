"""
    Remove gap characters in ancestral sequence reconstructions. Useful for protein structural prediction tools.

    Args:
        input_file (str): Path to the input FASTA file.
        output_file (str): Path to the de-gapped FASTA file.
    """
def read_fasta(filename):
    sequences = {}
    current_sequence = ""
    with open(filename, 'r') as file:
        for line in file:
            if line.startswith('>'):
                sequence_name = line.strip()[1:]
                sequences[sequence_name] = ""
                current_sequence = sequence_name
            else:
                sequences[current_sequence] += line.strip()
    return sequences

def remove_gaps(sequences):
    sequences_no_gaps = {}
    for name, sequence in sequences.items():
        sequence_no_gaps = sequence.replace('-', '')
        sequences_no_gaps[name] = sequence_no_gaps
    return sequences_no_gaps

def write_fasta(sequences, output_file):
    with open(output_file, 'w') as file:
        for name, sequence in sequences.items():
            file.write('>' + name + '\n')
            file.write(sequence + '\n')

def main(input_file, output_file):
    sequences = read_fasta(input_file)
    sequences_no_gaps = remove_gaps(sequences)
    write_fasta(sequences_no_gaps, output_file)

if __name__ == "__main__":
    input_file = ""  #Change to your input file name
    output_file = ""  #Change to your desired output file name
    main(input_file, output_file)
