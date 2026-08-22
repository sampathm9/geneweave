import time

from .scoring import calculate_alignment_score


def benchmark_alignment(seq1, seq2):
    start_time = time.perf_counter()

    score = calculate_alignment_score(seq1, seq2)

    end_time = time.perf_counter()

    elapsed_time = end_time - start_time

    return {
        "score": score,
        "time": elapsed_time,
    }