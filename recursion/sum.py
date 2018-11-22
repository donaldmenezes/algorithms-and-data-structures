def sum_list(lst):
    """
    Assumes lst is a list of numbers
    Returns the sum of all the numbers in the list
    Uses a recursive algorithm
    """
    
    if len(lst) == 1:
        return lst[0]
    else :
        return lst[0] + sum_list(lst[1:])
        
        
print(sum_list([1, 3, 5, 7, 9]))
