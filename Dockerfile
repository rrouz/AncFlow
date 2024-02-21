# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Snakefile and any other necessary files into the container
COPY Snakefile /app/
COPY scripts/ /app/scripts/

# Install Snakemake and any other dependencies
RUN pip install --no-cache-dir snakemake

# Define the entry point for running the pipeline
ENTRYPOINT ["snakemake", "--cores", "4"]  # Adjust the number of cores as needed

# Optionally, you can specify default targets for the pipeline
# CMD ["all"]
