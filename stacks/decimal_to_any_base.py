import Stack #from stack ADT

def base_converter(dec_number, base):
    """ 
    assumes dec_number is a potive integer and the base entered is between 2 to 16
    returns a representation of the number in that base.
    """
    
    digits = '0123456789ABCDEF'
    rem_stack = Stack()
    
    while dec_number > 0:
        rem = dec_number % base
        rem_stack.push(rem)
        dec_number = dec_number // base
        
    new_string = ""
    while not rem_stack.is_empty():
        new_string += digits(rem_stack.pop())
        
    return new_string
    

print(base_converter(25,2))
print(base_converter(25,10))
