def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """

    #Is this possible to do in a comprehension?
    #{ltr:  for ltr in phrase}

    #Our approach:
    #obj[key] = obj[key] || 0
    #obj[key] += 1

    phrase_to_dict = {}

    for ltr in phrase:
        if ltr in phrase_to_dict:
            phrase_to_dict[ltr] += 1
        else:
            phrase_to_dict[ltr] = 1
    
    return phrase_to_dict
