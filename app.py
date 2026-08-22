from geneweaver.fasta import read_fasta
from geneweaver.alignment import align_sequences


def main():
    sequences = read_fasta("data/sample.fasta")

    print(f"Loaded {len(sequences)} sequences")

    for sequence_id, sequence in sequences:
        print(f"{sequence_id}: {sequence}")


if __name__ == "__main__":
    main()