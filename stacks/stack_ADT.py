class Stack:
    def__init__(self):
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
        

# a program to use stack to reverse the characters of a string

def reversestr(string):
    """ 
    assumes string is a str
    returns reverse of a string
    
    >>> reversestr(football)
    llabtoof
    """
    
    s = Stack()
    
    # convert string to a stack
    for char in string:
        s.push(char)
        
    reversestrlist = []
    
    # pluck out the last element of the stack and append it as the first element of an empty list
    while not s.is_empty():
        reversestrlist.append(s.pop())
        
    return "".join(reversestrlist)
    

test_string = "I am a legend. No you're not!!"
print(reversestr(test_string))

#!!ton er'uoy oN .dnegel a ma I
