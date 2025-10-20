import ex1

"""
Test the divisible function from ex1 module.
Outsource:
- Grok"""

def test_divisible():
    # Test case 1: Normal case
    numbers = [1, 2, 3, 4, 5, 6]
    divisor = 2
    result = ex1.divisible(numbers, divisor)
    print(f"Test 1: divisible({numbers}, {divisor}) = {result}")
    assert result == [2, 4, 6], f"Expected [2, 4, 6], got {result}"

    # Test case 2: No divisible numbers
    numbers = [1, 3, 5]
    divisor = 2
    result = ex1.divisible(numbers, divisor)
    print(f"Test 2: divisible({numbers}, {divisor}) = {result}")
    assert result == [], f"Expected [], got {result}"

    # Test case 3: All divisible
    numbers = [2, 4, 6]
    divisor = 2
    result = ex1.divisible(numbers, divisor)
    print(f"Test 3: divisible({numbers}, {divisor}) = {result}")
    assert result == [2, 4, 6], f"Expected [2, 4, 6], got {result}"

    # Test case 4: Empty list
    numbers = []
    divisor = 3
    result = ex1.divisible(numbers, divisor)
    print(f"Test 4: divisible({numbers}, {divisor}) = {result}")
    assert result == [], f"Expected [], got {result}"

    # Test case 5: Divisor 1 (all divisible)
    numbers = [1, 2, 3]
    divisor = 1
    result = ex1.divisible(numbers, divisor)
    print(f"Test 5: divisible({numbers}, {divisor}) = {result}")
    assert result == [1, 2, 3], f"Expected [1, 2, 3], got {result}"

    # Test case 6: Negative numbers
    numbers = [-6, -3, 0, 3, 6]
    divisor = 3
    result = ex1.divisible(numbers, divisor)
    print(f"Test 6: divisible({numbers}, {divisor}) = {result}")
    assert result == [-6, -3, 0, 3, 6], f"Expected [-6, -3, 0, 3, 6], got {result}"

    # Test case 7: Negative divisor
    numbers = [6, 3, 0, -3, -6]
    divisor = -3
    result = ex1.divisible(numbers, divisor)
    print(f"Test 7: divisible({numbers}, {divisor}) = {result}")
    assert result == [6, 3, 0, -3, -6], f"Expected [6, 3, 0, -3, -6], got {result}"

    # Unacceptable inputs - currently no validation, so these will fail with TypeError or ZeroDivisionError

    # Test case 8: Divisor 0 (should raise ZeroDivisionError)
    try:
        ex1.divisible([1, 2, 3], 0)
        assert False, "Should have raised ZeroDivisionError for divisor 0"
    except ZeroDivisionError:
        print("Test 8: Correctly raised ZeroDivisionError for divisor 0")

    # Test case 9: Non-list numbers
    try:
        ex1.divisible("not a list", 2)
        assert False, "Should have raised TypeError for non-list numbers"
    except TypeError:
        print("Test 9: Correctly raised TypeError for non-list numbers")

    # Test case 10: Non-int divisor
    try:
        ex1.divisible([1, 2, 3], "not an int")
        assert False, "Should have raised TypeError for non-int divisor"
    except TypeError:
        print("Test 10: Correctly raised TypeError for non-int divisor")

    # Test case 11: List with non-int elements
    try:
        ex1.divisible([1, 2, "three"], 2)
        assert False, "Should have raised TypeError for non-int in list"
    except TypeError:
        print("Test 11: Correctly raised TypeError for non-int in list")

    print("All tests passed!")

if __name__ == "__main__":
    test_divisible()