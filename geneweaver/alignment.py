def count_mismatches(sequence_a: str, sequence_b: str) -> int:
    """
    Count the number of different nucleotides
    between two DNA sequences.
    """

    if len(sequence_a) != len(sequence_b):
        raise ValueError("Sequences must have the same length")

    sequence_a = sequence_a.upper()
    sequence_b = sequence_b.upper()

    mismatch_count = 0

    for base_a, base_b in zip(sequence_a, sequence_b):
        if base_a != base_b:
            mismatch_count += 1

    return mismatch_count