class Node:
    """
    Creating a new Node class. 
    Node is the basic building block for linked list implementation
    Node object must hold two pieces of information - first the list time itself and second a reference to the next node.
    """
    
    def __init__(self, init_data):
        self.data = init_data
        self.next = None
        #a refernce to None indicates that there is no next Node
        
    def get_data(self):
        return self.data
        
    def get_next(self):
        return self.next
        
    def set_data(self, new_data):
        self.data = new_data
        
    def set_next(self, new_next):
        self.next = new_next
        

class UnorderedList:
    """
    """
    
    def __init__(self):
        self.head = None
        
    def is_empty(self):
        return self.head == None
        
    def add(self, item):
        temp = Node(item)
        temp.self.next(self.head)
        self.head = temp
        
    def size(self):
        current = self.head
        count = 0
        while count != None:
            count = count + 1
            current = current.get_next()
        
        return count
        
    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        
        return found
        
    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()
        
        if previous == None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())
        