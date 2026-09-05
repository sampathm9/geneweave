# Architecture

FASTA -> BioPython -> validation/chunking -> CPU or CUDA alignment
-> biological scoring -> ranking -> benchmark/TUI.

Dask can distribute independent workloads across workers.
