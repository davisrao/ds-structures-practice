def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """

#convert string to list
#reverse list
#stringify

    new_lst = list(phrase)

    reverse_lst = new_lst[::-1]

    reverse_str = "".join(reverse_lst)

    return reverse_str
