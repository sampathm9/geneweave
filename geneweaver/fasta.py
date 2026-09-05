from pathlib import Path
from Bio import SeqIO

DNA_ALPHABET = set("ACGTN")

def read_fasta(path):
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(path)
    records = [(r.id, str(r.seq).upper().strip()) for r in SeqIO.parse(str(path), "fasta")]
    if not records:
        raise ValueError("FASTA file contains no sequences")
    return records

def validate_sequence(sequence):
    sequence = sequence.upper().strip()
    if not sequence:
        raise ValueError("DNA sequence cannot be empty")
    invalid = set(sequence) - DNA_ALPHABET
    if invalid:
        raise ValueError(f"Invalid DNA characters: {''.join(sorted(invalid))}")
    return sequence

def validate_records(records):
    return [(record_id, validate_sequence(sequence)) for record_id, sequence in records]

def chunk_sequence(sequence, chunk_size):
    if chunk_size <= 0:
        raise ValueError("chunk_size must be positive")
    return [sequence[i:i+chunk_size] for i in range(0, len(sequence), chunk_size)]
