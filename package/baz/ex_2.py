def is_palindrome(input_text):
    """
    Check if a string is a palindrome
    :param input_text: str
    :return: boolean
    # tenet
    """
    return input_text == input_text[::-1]


print(is_palindrome('tenet'))
