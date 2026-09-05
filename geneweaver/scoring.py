from dataclasses import dataclass

@dataclass
class ScoreResult:
    score: float
    severity: str

def score_off_target(mismatches, length, pam_proximity=0.0):
    if length <= 0:
        raise ValueError("length must be positive")
    identity = max(0.0, 1.0 - mismatches / length)
    proximity = max(0.0, min(1.0, pam_proximity))
    score = round(0.8 * identity + 0.2 * proximity, 4)
    severity = "HIGH" if score >= 0.80 else "MEDIUM" if score >= 0.50 else "LOW"
    return ScoreResult(score, severity)
