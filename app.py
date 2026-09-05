from geneweaver.pipeline import analyze_fasta

def main():
    results = analyze_fasta("data/sample.fasta")
    print("GENEWEAVER")
    print("=" * 60)
    print(f"Reference: {results['reference_id']}")
    print(f"Sequences processed: {results['sequence_count']}")
    for r in results["results"]:
        print(f"Target: {r['target_id']}")
        print(f"  Mismatches: {r['mismatches']}")
        print(f"  Alignment score: {r['alignment_score']}")
        print(f"  Similarity score: {r['score']}")
        print(f"  Severity: {r['severity']}")
        print(f"  Mismatch positions: {r['mismatch_positions']}")
        print()

if __name__ == "__main__":
    main()
