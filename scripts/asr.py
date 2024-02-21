import os
import subprocess

def run_shell_command(input_aln, input_nwk):
    """
    Run the shell command "java -jar bnkit.jar --aln {input_aln} --nwk {input_nwk}".

    Args:
        input_aln (str): Path to the input alignment file (.aln).
        input_nwk (str): Path to the input Newick tree file (.nwk).
    """
    command = ["java", "-jar", "bnkit.jar", "--aln", input_aln, "--nwk", input_nwk]
    subprocess.run(command)

def main():
    """
    Main function to process files in a directory.
    """
    directory = "subtrees"

    for filename in os.listdir(directory):
        if filename.endswith(".nwk"):
            nwk_file = os.path.join(directory, filename)
            fasta_file = os.path.join(directory, filename.replace(".nwk", ".fasta"))

            if os.path.exists(fasta_file):
                run_shell_command(fasta_file, nwk_file)
                print(f"Command executed for pair: {fasta_file}, {nwk_file}")
            else:
                print(f"Warning: Corresponding FASTA file not found for '{nwk_file}'. Skipping.")

if __name__ == "__main__":
    main()
