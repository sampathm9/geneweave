from geneweaver.pipeline import analyze_fasta

def test_pipeline():
    result = analyze_fasta("data/sample.fasta")
    assert result["sequence_count"] == 3
    assert result["reference_id"] == "target_001"
    assert len(result["results"]) == 2
