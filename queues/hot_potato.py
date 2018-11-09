import Queue #as defined in Queue DT

def hot_potato(name_list, num):
    """
    """
    
    sim_queue = Queue()
    
    #Adding elements from name_list to the queue data structure
    for name in name_list:
        sim_queue.enqueue(name)
        
    # assuming that the potato is at the end of the line, remove that end element and place it at position 0, 
    # at the end of num, remove the element from the queue
    # continue this process until only element remains in the list
    while sim_queue.size() > 1:
        for i in range (num):
            sim_queue.enqueue(sim_queue.dequeue())
            
        sim_queue.dequeue()
    
    #return the last remaining element
    return sim_queue.dequeue()
    
    
print(hot_potato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7))
