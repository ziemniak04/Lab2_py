from ex3 import subsets

"""
Test the subsets function.

Outsource:
- Grok
"""

def test_subsets():
    # Test 1: Two-element set
    x = {'a', 'b'}
    result = subsets(x)
    expected = [set(), {'a'}, {'b'}, {'a', 'b'}]
    assert len(result) == 4, f"Test 1 failed: expected 4 subsets, got {len(result)}"
    assert all(subset in result for subset in expected), "Test 1 failed: missing expected subsets"
    print("Test 1 passed (two-element set)")

    # Test 2: Single-element set
    x = {'x'}
    result = subsets(x)
    expected = [set(), {'x'}]
    assert len(result) == 2, f"Test 2 failed: expected 2 subsets, got {len(result)}"
    assert all(subset in result for subset in expected), "Test 2 failed: missing expected subsets"
    print("Test 2 passed (single-element set)")

    # Test 3: Three-element set
    x = {1, 2, 3}
    result = subsets(x)
    assert len(result) == 8, f"Test 3 failed: expected 8 subsets, got {len(result)}"
    assert set() in result, "Test 3 failed: empty set not in result"
    assert {1, 2, 3} in result, "Test 3 failed: full set not in result"
    print("Test 3 passed (three-element set)")

    # Test 4: Empty set
    x = set()
    result = subsets(x)
    assert len(result) == 1, f"Test 4 failed: expected 1 subset, got {len(result)}"
    assert set() in result, "Test 4 failed: empty set not in result"
    print("Test 4 passed (empty set)")

    # Test 5: Four-element set (verify count)
    x = {'a', 'b', 'c', 'd'}
    result = subsets(x)
    assert len(result) == 16, f"Test 5 failed: expected 16 subsets, got {len(result)}"
    print("Test 5 passed (four-element set)")

    # Test 6: All results are sets
    x = {1, 2}
    result = subsets(x)
    assert all(isinstance(subset, set) for subset in result), "Test 6 failed: not all results are sets"
    print("Test 6 passed (all results are sets)")

    print("\nAll tests passed!")


if __name__ == "__main__":
    test_subsets()