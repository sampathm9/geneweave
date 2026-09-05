import time
from .alignment import count_mismatches

def benchmark(sequence_length=10000, repetitions=100):
    a = ("ACGT" * ((sequence_length + 3)//4))[:sequence_length]
    b = ("ACGA" * ((sequence_length + 3)//4))[:sequence_length]
    start = time.perf_counter()
    result = 0
    for _ in range(repetitions):
        result = count_mismatches(a, b)
    elapsed = time.perf_counter() - start
    total = sequence_length * repetitions
    return {"sequence_length": sequence_length, "repetitions": repetitions,
            "mismatches": result, "elapsed_seconds": elapsed,
            "comparisons_per_second": total / elapsed}

if __name__ == "__main__":
    for k, v in benchmark().items():
        print(f"{k}: {v}")
