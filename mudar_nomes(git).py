import os
from Bio import SeqIO
import re

def rename_sequences(input_file, output_file):
    sequences = SeqIO.parse(input_file, "fasta")
    new_sequences = []
    
    for seq_record in sequences:
        match = re.search(r"\[organism=([^\]]+)\]", seq_record.description)
        if match:
            organism_name = match.group(1)
            seq_record.id = organism_name.replace(" ", "_")
            seq_record.description = ""
        new_sequences.append(seq_record)
    
    SeqIO.write(new_sequences, output_file, "fasta")
    print(f"Sequências renomeadas e salvas em {output_file}")

def process_directory(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for filename in os.listdir(input_dir):
        if filename.endswith(".aln"):
            input_file = os.path.join(input_dir, filename)
            output_file = os.path.join(output_dir, filename)
            rename_sequences(input_file, output_file)

# Exemplo de uso
input_directory = r"C:\Users\IQ-TREE-trial\Alinhamentos com gaps"
output_directory = r"C:\Users\IQ-TREE-trial\Alinhamentos com gaps\renomeados"

process_directory(input_directory, output_directory)
