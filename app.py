from geneweaver.fasta import read_fasta
from geneweaver.alignment import count_mismatches


def main():
    sequences = read_fasta("data/sample.fasta")

    print(f"Loaded {len(sequences)} sequences")
    print()

    target_id, target_sequence = sequences[0]

    print(f"Reference: {target_id}")
    print(f"Sequence:  {target_sequence}")
    print()

    for sequence_id, sequence in sequences[1:]:
        mismatches = count_mismatches(target_sequence, sequence)

        print(f"Comparing: {sequence_id}")
        print(f"Mismatches: {mismatches}")
        print()


if __name__ == "__main__":
    main()