from geneweaver.scoring import score_off_target

def test_high_similarity():
    assert score_off_target(0, 20).severity == "HIGH"

def test_range():
    result = score_off_target(5, 20)
    assert 0 <= result.score <= 1
