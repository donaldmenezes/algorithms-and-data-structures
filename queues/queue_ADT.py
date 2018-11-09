class Queue:
    """
    Defining a Queue Class, First in First Out system
    """
    
    def __init__ (self):
        """ Using List collection to represent queue data structure """
        
        self.items = []
        
    def is_empty(self):
        """ 
        Returns if the queue is empty 
        
        >>> q.is_empty()
        True
        """
        
        return self.items == []
        
    def enqueue(self, item):
        """ 
        Adds an item at position 0 of the queue. 
        That is, adding item at the rear of the queue.
        Returns the mutated the list.
        
        >>> q.enqueue('4')
        ['4']
        """
        
        return self.items.insert(0, item)
        
    def dequeue(self):
        """ 
        Removes the last item of the queue, 
        That is removing item from the front of the queue
        Returns the remved item
        
        >>> q.pop()
        '4'
        """
        
        return self.items.pop()
    
    def size(self):
        """
        Returns the length of the queue
        
        >>> q.size
        0
        """
        
        return len(self.items)
