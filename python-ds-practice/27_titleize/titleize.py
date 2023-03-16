def titleize(phrase):
    stri = ''
    for word in phrase.split(' '):
        stri = stri + ' ' + word.capitalize()
    return stri
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
