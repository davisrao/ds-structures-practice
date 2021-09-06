def last_element(lst):
    """Return last item in list (None if list is empty.
    
        >>> last_element([1, 2, 3])
        3
        
        >>> last_element([]) is None
        True
    """

    # if list is empty, return None
    # go into the list at index -1 and return value
 

    if lst == []:
        return None
    else:
        return lst[-1]