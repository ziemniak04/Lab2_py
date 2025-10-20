from ex5 import dna_complement

"""
Test the dna_complement function.

Outsource:
- Grok 
"""

def test_dna_complement():
    # Test 1: Simple case
    assert dna_complement("ATCG") == "TAGC", "Test 1 failed"

    # Test 2: Lowercase input
    assert dna_complement("gattaca") == "CTAATGT", "Test 2 failed"

    # Test 3: Mixed case input
    assert dna_complement("aTcG") == "TAGC", "Test 3 failed"

    # Test 4: Empty string
    assert dna_complement("") == "", "Test 4 failed"

    # Test 5: Invalid character
    try:
        dna_complement("ATXG")
    except ValueError:
        print("Test 5 passed (caught ValueError)")
    else:
        print("Test 5 failed (no ValueError raised)")

    print("All basic DNA complement tests passed")

test_dna_complement()