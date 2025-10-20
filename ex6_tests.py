from ex6 import find_genes, main, dna_complement

"""
Test the find_genes function.

Outsource:
- Grok
"""

def test_find_genes():
    # Test 1: Simple single gene
    seq1 = "ATGAAATAG"
    assert find_genes(seq1) == ["ATGAAATAG"], "Test 1 failed"

    # Test 3: Lowercase input
    seq3 = "atgaaatag"
    assert find_genes(seq3) == ["ATGAAATAG"], "Test 3 failed"

    # Test 4: Complementary sequence
    seq4 = "ATGAAATAG"
    comp = dna_complement(seq4)
    genes_comp = find_genes(comp)
    assert genes_comp == ["ATTTTCAT"], "Test 4 failed (complement)"

    # Test 5: Invalid character
    try:
        find_genes("CXGC")
    except ValueError:
        print("Test 5 passed (invalid character detected)")
    else:
        print("Test 5 failed (no error detected)")

    print("All basic gene tests passed ")


if __name__ == "__main__":
    test_find_genes()