import numpy as np

try:
    from numba import cuda
    CUDA_AVAILABLE = cuda.is_available()
except Exception:
    cuda = None
    CUDA_AVAILABLE = False

if cuda is not None:
    @cuda.jit
    def mismatch_kernel(a, b, output):
        i = cuda.grid(1)
        if i < a.size:
            output[i] = 1 if a[i] != b[i] else 0

def cuda_count_mismatches(sequence_a, sequence_b):
    if not CUDA_AVAILABLE:
        raise RuntimeError("CUDA is not available. Use a supported NVIDIA CUDA system.")
    if len(sequence_a) != len(sequence_b):
        raise ValueError("Sequences must have the same length")
    a = np.frombuffer(sequence_a.upper().encode("ascii"), dtype=np.uint8)
    b = np.frombuffer(sequence_b.upper().encode("ascii"), dtype=np.uint8)
    da, db = cuda.to_device(a), cuda.to_device(b)
    out = cuda.device_array(a.size, dtype=np.uint8)
    threads = 256
    blocks = (a.size + threads - 1) // threads
    mismatch_kernel[blocks, threads](da, db, out)
    cuda.synchronize()
    return int(out.copy_to_host().sum())
