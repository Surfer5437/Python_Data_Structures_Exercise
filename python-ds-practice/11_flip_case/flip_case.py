def flip_case(phrase, to_swap):
    swapped=[]
    for x in phrase:
        if x.lower() == to_swap.lower():
            if x.isupper():
                swapped.append(x.lower())
            else:
                swapped.append(x.upper())
        else:
            swapped.append(x)
    return ''.join(swapped)
    # return ''.join([x.lower() if (x.isupper() and x.lower() == to_swap.lower()) else x.upper() for x in phrase ])
    # [a if a else 2 for a in [0,1,0,3]]
"""Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

"""
