def is_palindrome(phrase):
    lst=[]
    for x in phrase:
        lst.append(x)
    lst.reverse()
    if phrase == ''.join(lst):
        return True
    else:
        return False




    # alph = 'abcdefghijklmnopqrstuvwxyz'
    # is_true = True
    # for x in alph:
    #     if phrase.count(x) > 0 and is_true == True:
    #         is_true = True
    #     elif phrase.count(x) == 0:
    #         return False
    # return True
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
