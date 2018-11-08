import Stack #from stack ADT

def divide_by_2(dec_number):
    """ 
    assumes dec_number is a potive integer
    returns a binary of the number.
    """
    
    rem_stack = Stack()
    
    while dec_number > 0:
        rem = dec_number % 2
        rem_stack.push(rem)
        dec_number = dec_number // 2
        
    bin_string = ""
    while not rem_stack.is_empty():
        bin_string += str(rem_stack.pop())
        
    return bin_string
    
print(divide_by_2(42))
