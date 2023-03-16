def reverse_string(phrase):
    x = len(phrase)-1
    revWord = ''
    while x >= 0:
        revWord=revWord + phrase[x]
        x=x-1
    return revWord
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
