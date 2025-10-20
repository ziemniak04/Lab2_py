def divisible(numbers, divisor):
    """
    Returns a list of numbers from the given list that are divisible by the specified divisor.

    Parameters:
        numbers (list of int): A list of integers to check.
        divisor (int): The integer divisor to test divisibility against.

    Returns:
        list of int: A new list containing only those numbers from 'numbers'
                     that are evenly divisible by 'divisor' (i.e., number % divisor == 0).

    Raises:
        TypeError: If 'numbers' is not a list or if 'divisor' is not an integer.
        ZeroDivisionError: If 'divisor' is zero.

    Outsource:
    - docstrings
    """
    if not isinstance(numbers, list):
        raise TypeError("Input 'numbers' must be a list.")
    if not all(isinstance(n, int) for n in numbers):
        raise TypeError("All elements in 'numbers' must be integers.")
    if not isinstance(divisor, int):
        raise TypeError("Input 'divisor' must be an integer.")
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be zero.")

    result = []
    for number in numbers:
        if number % divisor == 0:
            result.append(number)
    return result
