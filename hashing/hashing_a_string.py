def hashstring(astring, tablesize):
    """
    Assumes that astring is a string, and tablesize is a prime number.
    Returns the hash value of the string in the range of 0 to tablesize-1
    """
    
    sum = 0
    for pos in range(len(astring)):
        # to account for anagrams, we give weightage to positions of the letters to give different hash values
        sum = sum + ord(astring[pos]) * (pos + 1)
    
    return sum % tablesize
    
    
print(hashstring('cat', 11))
print(hashstring('listen', 11))
print(hashstring('silent', 11))
print(hashstring('binary', 11))
print(hashstring('brainy', 11))

## 3
## 4
## 0
## 1
## 3
