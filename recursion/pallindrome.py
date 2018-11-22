def pallindrome(string):
    """
    Assumes string is a str
    
    Returns True if the string is a pallindrome
    """
    
    if len(string) == 1:
        return True
    elif len(string) == 2:
        return string[0] == string[1]
    else:
        if string[0] == string[-1]:
            return pallindrome(string[1:-1])
        else:
            return False
