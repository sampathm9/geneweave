def calculate_alignment_score(seq1, seq2):
    # your logic here
    if len(seq1) != len(seq2):
        raise ValueError("Sequences must have the same length")

    score = 0

    for nucleotide1, nucleotide2 in zip(seq1, seq2):
        if nucleotide1 == nucleotide2:
            score += 1
        else:
            score -= 1

    return score
