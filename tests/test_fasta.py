import pytest
from geneweaver.fasta import validate_sequence

def test_uppercase():
    assert validate_sequence("acgt") == "ACGT"

def test_invalid():
    with pytest.raises(ValueError):
        validate_sequence("ACGX")

def test_empty():
    with pytest.raises(ValueError):
        validate_sequence("")
