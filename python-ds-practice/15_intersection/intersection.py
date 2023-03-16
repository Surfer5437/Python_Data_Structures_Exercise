def intersection(l1, l2):
    x=[]
    for num1 in l1:
        for num2 in l2:
            if num1 == num2:
                x.append(num1)
                l2.pop(l2.index(num2))
    return x
        

    # return set(l1 + l2)
"""Return intersection of two lists as a new list::
    
        >>> intersection([1, 2, 3], [2, 3, 4])
        [2, 3]
        
        >>> intersection([1, 2, 3], [1, 2, 3, 4])
        [1, 2, 3]
        
        >>> intersection([1, 2, 3], [3, 4])
        [3]
        
        >>> intersection([1, 2, 3], [4, 5, 6])
        []
"""