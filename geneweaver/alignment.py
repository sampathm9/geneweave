from dataclasses import dataclass

@dataclass
class AlignmentResult:
    aligned_a: str
    aligned_b: str
    score: int

def count_mismatches(sequence_a, sequence_b):
    if len(sequence_a) != len(sequence_b):
        raise ValueError("Sequences must have the same length")
    return sum(a != b for a, b in zip(sequence_a.upper(), sequence_b.upper()))

def mismatch_positions(sequence_a, sequence_b):
    if len(sequence_a) != len(sequence_b):
        raise ValueError("Sequences must have the same length")
    return [i for i, (a, b) in enumerate(zip(sequence_a.upper(), sequence_b.upper())) if a != b]

def needleman_wunsch(sequence_a, sequence_b, match=1, mismatch=-1, gap=-2):
    a, b = sequence_a.upper(), sequence_b.upper()
    n, m = len(a), len(b)
    dp = [[0]*(m+1) for _ in range(n+1)]
    for i in range(1, n+1):
        dp[i][0] = i * gap
    for j in range(1, m+1):
        dp[0][j] = j * gap
    for i in range(1, n+1):
        for j in range(1, m+1):
            diagonal = dp[i-1][j-1] + (match if a[i-1] == b[j-1] else mismatch)
            dp[i][j] = max(diagonal, dp[i-1][j] + gap, dp[i][j-1] + gap)
    aa, bb = [], []
    i, j = n, m
    while i or j:
        if i and j:
            diagonal = dp[i-1][j-1] + (match if a[i-1] == b[j-1] else mismatch)
            if dp[i][j] == diagonal:
                aa.append(a[i-1]); bb.append(b[j-1]); i -= 1; j -= 1
                continue
        if i and dp[i][j] == dp[i-1][j] + gap:
            aa.append(a[i-1]); bb.append("-"); i -= 1
        else:
            aa.append("-"); bb.append(b[j-1]); j -= 1
    return AlignmentResult("".join(reversed(aa)), "".join(reversed(bb)), dp[n][m])
