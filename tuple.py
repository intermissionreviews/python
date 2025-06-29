def concat_tuples(tuple1, tuple2):
    """
    Concatenates two tuples of any lengths into a single tuple.

    Args:
    tuple1 (tuple): The first input tuple.
    tuple2 (tuple): The second input tuple.

    Returns:
    tuple: A new tuple containing all elements from both input tuples.
    """
    return tuple1 + tuple2

# Example usage:
tuple_a = (4, 5, 6)
tuple_b = ('e', 'f', 'g', 'h')
result = concat_tuples(tuple_a, tuple_b)
print(result) # Output: (4, 5, 6, 'e', 'f', 'g', 'h')