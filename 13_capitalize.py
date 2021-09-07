def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """

    phrase_list = list(phrase)

    phrase_list[0] = phrase_list[0].upper()
    result_str = "".join(phrase_list)
    return result_str