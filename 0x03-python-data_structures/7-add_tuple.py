#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """
    Adds two tuples

    Args:
        tuple_a: First tuple
        tuple_b: Second tuple

    Return:
        New tuple, with addition of former
    """
    if len(tuple_a) < 3:
        tuple_a += (0,) if (len(tuple_a) == 1) else (0, 0,)
    if len(tuple_b) < 3:
        tuple_b += (0,) if (len(tuple_b) == 1) else (0, 0,)

    list_a = [a_index for a_index in tuple_a]
    list_b = [b_index for b_index in tuple_b]
    result = tuple([list_a[i] + list_b[i] for i in range(2)])
    return(result)
