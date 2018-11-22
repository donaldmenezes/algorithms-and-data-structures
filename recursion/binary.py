def to_str(n, base):
    """
    Assumes n and base are integers and non-negative. Also assumes that base is between 2 and 16.
    
    Converts an integer to a string in any base.
    Return the string representation of the integer entered.
    """
    
    convert_string = "0123456789ABCDEF"
    if n < base:
        return convert_string[n]
    else:
        return to_str(n // base, base) + convert_string[n % base]
