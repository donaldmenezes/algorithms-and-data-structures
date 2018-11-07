class Stack:
    def __init__(self):
        """ Using list data structure to implement a stack """
        self.items = []
    
    def is_empty(self):
        """ returns if the stack is empty """
        return self.items == []
        
    def push(self, item):
        """ adds a item to the end of the list """
        return self.items.append(item)
        
    def pop(self, item):
        """ removes the last element from list """
        return self.items.pop()
        
    def peek(self):
        """ returns the top element of the stack/list """
        return self.items[len(items)-1]
        
    def size(self):
        """ returns the length of the stack """
        return len(self.items)

def matches(open, close):
    """ checks if the '([{' match equally to ')]}' """
    opens = '([{'
    closes = ')]}'
    return opens.index(open) == closes.index(close)
    
def par_checker(symbol_string):
    """
    Returns a boolean if a set of opening and closing symbols are properly balanced and nested
    
    >>> par_checker('({([])})')
    True
    >>> par_checker('{[})')
    False
    """
    
    s = Stack()
    balanced = True     # assume that the set of symbols are equally balanced
    index = 0
    
    while index < len(symbol_string) and balanced:
        symbol = symbol_string[index]
        if symbol in '([{':         #check for opening symbols and push them to the stack
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
            else:
                top = s.pop()       #removes the last element of the stack
                if not matches(top, symbol):    #matching the opening and closing element, if not matched, balanced = False
                    balanced = False
        index += 1
        
    if balanced and s.is_empty():   #check if the string is balanced and the stack is empty 
        return True
    else:
        return False
        
print(par_checker('{{([][])}()}'))
print(par_checker('[{()]'))
