from .fasta import read_fasta, validate_records
from .alignment import count_mismatches, mismatch_positions, needleman_wunsch
from .scoring import score_off_target

def analyze_fasta(path):
    records = validate_records(read_fasta(path))
    reference_id, reference = records[0]
    results = []
    for target_id, target in records[1:]:
        if len(reference) == len(target):
            mismatches = count_mismatches(reference, target)
            positions = mismatch_positions(reference, target)
        else:
            alignment = needleman_wunsch(reference, target)
            mismatches = sum(a != b for a, b in zip(alignment.aligned_a, alignment.aligned_b) if a != "-" and b != "-")
            positions = []
        alignment_score = needleman_wunsch(reference, target).score
        s = score_off_target(mismatches, max(len(reference), len(target)))
        results.append({"target_id": target_id, "mismatches": mismatches,
                        "mismatch_positions": positions, "alignment_score": alignment_score,
                        "score": s.score, "severity": s.severity})
    return {"reference_id": reference_id, "sequence_count": len(records), "results": results}
