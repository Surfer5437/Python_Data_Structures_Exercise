def find_factors(num):
    arr=[]
    x = range(num+1)
    for i in x:
        if i!=0:
            if x.count(num / i)>0:
                arr.append(i)
    return arr
    """Find factors of num, in increasing order.

    >>> find_factors(10)
    [1, 2, 5, 10]

    >>> find_factors(11)
    [1, 11]

    >>> find_factors(111)
    [1, 3, 37, 111]

    >>> find_factors(321421)
    [1, 293, 1097, 321421]
    """
