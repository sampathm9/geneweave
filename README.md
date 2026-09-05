# GeneWeaver

GPU-accelerated CRISPR/DNA sequence analysis engine.

Pipeline:
FASTA -> BioPython -> validation -> chunking -> CPU/CUDA alignment
-> scoring -> ranking -> benchmarking -> Textual TUI

## Run
python app.py

## Test
pytest -q

## Benchmark
python -m geneweaver.benchmark

CUDA requires a supported NVIDIA GPU and compatible CUDA/Numba environment.
