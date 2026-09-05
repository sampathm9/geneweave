import pytest
from geneweaver.alignment import count_mismatches, mismatch_positions, needleman_wunsch

def test_perfect_match():
    assert count_mismatches("ACGT", "ACGT") == 0

def test_mismatch():
    assert count_mismatches("ACGT", "ACGA") == 1

def test_lowercase():
    assert count_mismatches("acgt", "acga") == 1

def test_positions():
    assert mismatch_positions("ACGT", "ACGA") == [3]

def test_different_lengths():
    with pytest.raises(ValueError):
        count_mismatches("ACGT", "ACG")

def test_alignment():
    result = needleman_wunsch("ACGT", "ACG")
    assert len(result.aligned_a) == len(result.aligned_b)
