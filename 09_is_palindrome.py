def is_palindrome(phrase):
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

    #Turn string into list
    #Make copy of string that's reversed
    #Compare lists

    lowercase_phrase = phrase.lower().replace(" ","")
    lowercase_list = list(lowercase_phrase)
    reversed_list = lowercase_list[::-1]

    if lowercase_list == reversed_list:
        return True
    else:
        return False



## can just use to lower with stepping back