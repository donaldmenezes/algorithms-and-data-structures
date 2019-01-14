def binary_search_recursive(alist, item, first=0, last=None):
    if last is None:
        last = len(alist) - 1
    if first > last:
        return False

    midpoint = (first + last) // 2
    if item == alist[midpoint]:
        return True
    if item < alist[midpoint]:
        return binary_search_recursive(alist, item, first, midpoint-1)
    # item > alist[midpoint]
    return binary_search_recursive(alist, item, midpoint+1, last)
                

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(binary_search_recursive(testlist, 3))
print(binary_search_recursive(testlist, 30))
