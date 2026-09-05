def dask_process(reference, targets):
    from dask import delayed, compute
    from .cuda_alignment import cuda_count_mismatches
    tasks = [delayed(cuda_count_mismatches)(reference, target) for target in targets]
    return list(compute(*tasks))

def start_local_client():
    from dask.distributed import Client
    return Client()
