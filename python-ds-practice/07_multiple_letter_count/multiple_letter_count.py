def multiple_letter_count(phrase):
    d={}
    for x in phrase:
        d[x] = phrase.count(x)
    return d
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """