from pathlib import Path

from Bio import SeqIO


def read_fasta(file_path: str | Path) -> list[tuple[str, str]]:
    """
    Read DNA sequences from a FASTA file.

    Returns:
        A list containing (sequence_id, sequence) tuples.
    """
    file_path = Path(file_path)

    if not file_path.exists():
        raise FileNotFoundError(f"FASTA file not found: {file_path}")

    sequences = []

    for record in SeqIO.parse(file_path, "fasta"):
        sequence = str(record.seq).upper()
        sequences.append((record.id, sequence))

    return sequences