def single_letter_count(word, letter):
    """How many times does letter appear in word (case-insensitively)?
    
        >>> single_letter_count('Hello World', 'h')
        1
        
        >>> single_letter_count('Hello World', 'z')
        0
        
        >>> single_letter_count("Hello World", 'l')
        3
    """

    # we need to make the whole string lowercase
    # normal ltr of word + if statement

    lowercase_word = word.lower()
    counter = 0

    for ltr in lowercase_word:
        if ltr == letter:
            counter +=1

    return counter

# look into the count method here - this makes thsi a lot easier


