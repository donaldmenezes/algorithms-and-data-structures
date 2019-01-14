def binary_search(alist, item):
    
    first = 0
    last = len(alist) - 1
    found = False
    
    while first <= last and not found:
        midpoint = (last+first) // 2
        if alist[midpoint] == item:
            found = True
        else:
            if alist[midpoint] > item:
                last = midpoint - 1
            else:
                first = midpoint + 1
    
    return found
    
testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(binary_search(testlist, 3))
print(binary_search(testlist, 30))
