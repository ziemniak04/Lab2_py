def common(x, y):
    """
    Returns the intersection of two lists treated as multisets.

    This function compares two lists (x and y) and returns a new list 
    containing the elements that appear in both. Each element in the result 
    appears as many times as it appears in both lists (i.e., the minimum count 
    between the two).

    Parameters:
        x (list): The first list (multiset).
        y (list): The second list (multiset).

    Returns:
        list: A new list containing elements that are common to both x and y.

    Raises:
        ValueError: If either x or y is not a list.

    Outsource:
    - docstrings

    """
    if not isinstance(x, list) or not isinstance(y, list):
        raise ValueError("Both x and y must be lists")

    result = []
    y_copy = list(y)
    for element in x:
        if element in y_copy:
            result.append(element)
            y_copy.remove(element)  
    return result
