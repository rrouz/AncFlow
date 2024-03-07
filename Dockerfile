# Use an official Python runtime as a parent image
FROM continuumio/miniconda3 AS python_base

# Set the working directory in the container
WORKDIR /app

# Copy the Snakefile and any other necessary files into the container
COPY Snakefile /app/
COPY scripts/ /app/scripts/
COPY sample_runs/ /app/sample_runs/
COPY bnkit.jar /app/
COPY protein_sequences.fasta /app/protein_sequences.fasta

# Install Snakemake and Biopython using Conda
RUN conda create -n autophy python==3.8.18

# Install Snakemake and other dependencies using Conda from Bioconda and Conda Forge channels
RUN conda install --yes -c bioconda -c conda-forge snakemake biopython mafft iqtree

# Activate the Conda environment
SHELL ["conda", "run", "-n", "autophy", "/bin/bash", "-c"]

# Install Autophy from GitHub using pip
RUN pip install 'autophy @ git+https://github.com/aortizsax/autophy@main'

# Switch to a new stage
FROM openjdk:11-jre-slim AS java_base

# Create the /app directory
RUN mkdir -p /app

# Create a bash script to run bnkit.jar
RUN echo '#!/bin/sh\njava -jar -Xmx16g /app/bnkit.jar $@' > /app/grasp \
    && chmod 755 /app/grasp

# Add the script to the system path
ENV PATH="/app:${PATH}"

# Define the entry point for running the pipeline
ENTRYPOINT ["snakemake", "--cores", "4"]
