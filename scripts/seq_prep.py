import os

os.makedirs("logs", exist_ok=True)
os.makedirs("alignments", exist_ok=True)

input_file = "protein_sequences.fasta"
output_file = "alignments/modified_protein_sequences.fasta"

with open(input_file, "r") as infile, open(output_file, "w") as outfile:
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
                    