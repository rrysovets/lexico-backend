def int_to_bool_status_converter(seq) :
    """Converts the first element of a tuples to boolean, preserving the second element. return iterator"""
    for tup in seq:
        yield (bool(tup[0]), tup[1])
