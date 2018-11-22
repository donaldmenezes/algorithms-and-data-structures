def reverse_string(string):
    """
    Assumes that string is str
    
    Returns the reverse of the string.
    
    >>> reverse_string("abc def")
    fed cba
    """
    
    if len(string) == 1:
        return string[0]
    else:
        return reverse_string(string[1:]) + string[0]
