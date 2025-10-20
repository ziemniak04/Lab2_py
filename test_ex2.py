import ex2

"""
Test the common function from ex2 module.
Outsource:
- Grok"""

def test_common():
    # Test case 1: Normal lists with common elements
    x = [1, 2, 2, 3]
    y = [2, 2, 4]
    result = ex2.common(x, y)
    print(f"Test 1: common({x}, {y}) = {result}")
    assert result == [2, 2], f"Expected [2, 2], got {result}"

    # Test case 2: No common elements
    x = [1, 3, 5]
    y = [2, 4, 6]
    result = ex2.common(x, y)
    print(f"Test 2: common({x}, {y}) = {result}")
    assert result == [], f"Expected [], got {result}"

    # Test case 3: Empty lists
    x = []
    y = [1, 2]
    result = ex2.common(x, y)
    print(f"Test 3: common({x}, {y}) = {result}")
    assert result == [], f"Expected [], got {result}"

    # Test case 4: Identical lists
    x = [1, 2, 3]
    y = [1, 2, 3]
    result = ex2.common(x, y)
    print(f"Test 4: common({x}, {y}) = {result}")
    assert result == [1, 2, 3], f"Expected [1, 2, 3], got {result}"

    # Test case 5: Strings
    x = ['a', 'b', 'c']
    y = ['b', 'c', 'd']
    result = ex2.common(x, y)
    print(f"Test 5: common({x}, {y}) = {result}")
    assert result == ['b', 'c'], f"Expected ['b', 'c'], got {result}"

    # Test case 6: Invalid input - not lists
    try:
        ex2.common("not a list", [1, 2])
        print("Test 6 failed: Should have raised ValueError")
        assert False, "Should have raised ValueError"
    except ValueError as e:
        print(f"Test 6: Correctly raised ValueError: {e}")

    # Test case 7: Invalid input - second not list
    try:
        ex2.common([1, 2], "not a list")
        print("Test 7 failed: Should have raised ValueError")
        assert False, "Should have raised ValueError"
    except ValueError as e:
        print(f"Test 7: Correctly raised ValueError: {e}")

    print("All tests passed!")

if __name__ == "__main__":
    test_common()