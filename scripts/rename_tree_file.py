import os

def rename_tree_file(directory):
    """
    Renames a tree file within the specified directory.

    Args:
        directory (str): Path to the directory containing the tree file.
    """
    for filename in os.listdir(directory):
        if filename.endswith(".tree"):
            new_name = "autophy_tree.nwk"
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))
            break
    else:
        print("No .tree files found in the specified directory.")

directory = 'output'
rename_tree_file(directory)
