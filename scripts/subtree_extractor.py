"""
Script for extracting and formatting subtrees from a Newick tree file.

This script extracts subtrees from a Newick tree file based on a specified clade size threshold,
fetches sequences for each clade from NCBI GenBank, and saves the sequences and corresponding
subtrees in separate files.

Functions:
    - extract_and_format_subtree(tree_string, clade_number): Extracts and formats a subtree from
      the Newick tree string for a given clade number.
    - subtree_parse(selected_subtree): Parses the selected subtree to ensure correct formatting.

Paths:
    - newick_tree_file_path (str): Path to the Newick tree file.
    - output_folder (str): Path to the folder where output files will be saved.

Usage:
    1. Ensure that the 'newick_tree_file_path' variable points to the correct Newick tree file.
    2. Set the 'output_folder' variable to the desired folder where output files will be saved.
    3. Run the script. It will prompt you to enter the minimum clade size to extract.
    4. The script will process each clade, fetch sequences from NCBI GenBank, and save the sequences
       and corresponding subtrees in separate files.

Example:
    python extract_subtrees.py
"""

import re
import os
from Bio import Entrez, SeqIO

def extract_and_format_subtree(tree_string, clade_number):
    taxon_pattern = r"([^,;()]*\|{}:[^,;()]+)".format(clade_number)
    matches = re.findall(taxon_pattern, tree_string)

    if matches:
        formatted_subtree = ""
        first_occurrence_index = tree_string.find(matches[0])

        if first_occurrence_index >= 0:
            while first_occurrence_index > 0:
                if tree_string[first_occurrence_index] == ',':
                    break
                first_occurrence_index -= 1

            open_parentheses_count = 0
            subtree = ""
            comma_encountered = False

            for char in tree_string[first_occurrence_index:]:
                if comma_encountered:
                    if char == '(':
                        open_parentheses_count += 1
                    elif char == ')':
                        if open_parentheses_count == 0:
                            break
                        else:
                            open_parentheses_count -= 1
                    subtree += char
                if char == ',':
                    comma_encountered = True

            formatted_subtree = subtree

            return formatted_subtree

    return None

def subtree_parse(selected_subtree):
    if selected_subtree:
        pieces = selected_subtree.split('|')[1:]
        numbers = []

        for piece in pieces:
            number = ""
            for char in piece:
                if char == ":":
                    break
                number += char
            numbers.append(number)

        count = 0
        number_we_care_about = numbers[0]

        for num in numbers:
            if num != number_we_care_about:
                break
            count += 1

        result = ""
        b = None

        for i, char in enumerate(selected_subtree):
            if char == '(':
                continue
            else:
                b = i
                break

        new_string = selected_subtree[b:]

        for char in new_string:
            if char == ',':
                count -= 1
            if count == 0:
                break
            result += char

        closer_p = 0
        open_p = 0

        for char in result:
            if char == ')':
                closer_p += 1
            if char == '(':
                open_p += 1

        total_p = closer_p - open_p

        while total_p != 0:
            result = '(' + result
            total_p -= 1
    return result

newick_tree_file_path = "output/autophy_tree.nwk"
output_folder = "subtrees"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

with open(newick_tree_file_path, "r") as file:
    newick_tree_string = file.read()

minimum_clade_size = int(input("Enter the minimum clade size to extract: "))

taxon_pattern = r"sp_([^|]+)\|([\d.]+):"
matches = re.findall(taxon_pattern, newick_tree_string)

if not matches:
    print("No clades found in the tree.")
    exit()

for match in matches:
    clade_number = match[1]
    clade_size = len([accession for accession in matches if accession[1] == clade_number])

    if clade_size < minimum_clade_size:
        print(f"Skipping clade {clade_number} as it has only {clade_size} member(s).")
        continue

    accession_numbers = [accession[0].split('_')[0] for accession in matches if accession[1] == clade_number]

    Entrez.email = ""
    db = "protein"
    sequences = []

    for accession in accession_numbers:
        try:
            handle = Entrez.efetch(db=db, id=accession, rettype="gb", retmode="text")
            record = SeqIO.read(handle, "genbank")
            sequences.append(record)
        except Exception as e:
            print(f"Failed to retrieve sequence for {accession}: {e}")

    fasta_filename = os.path.join(output_folder, f"clade_{clade_number}_subtree.fasta")
    with open(fasta_filename, "w") as fasta_file:
        SeqIO.write(sequences, fasta_file, "fasta")

    print(f"Sequences for clade {clade_number} saved in '{fasta_filename}'")
    selected_subtree = extract_and_format_subtree(newick_tree_string, clade_number)
    final_subtree = subtree_parse(selected_subtree)
    if final_subtree is not None:
        new_newick_tree_file_path = os.path.join(output_folder, f"clade_{clade_number}_subtree.nwk")
        with open(new_newick_tree_file_path, "w") as newick_file:
            newick_file.write(final_subtree + ";")

        print(f"Subtree for clade {clade_number} saved in '{new_newick_tree_file_path}'")

print("All viable subtrees processed successfully.")
