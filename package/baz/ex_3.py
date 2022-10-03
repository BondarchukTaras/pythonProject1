def encode_symbol_cesar(message: str, key: int):
    """
    Cesar`s code ()
    :param message: str
    :param key: int
    :return: str
    """
    result = ''
    for item in message:
        result += chr(ord('a') + (ord(item) - ord('a') + key) % (ord('z') - ord('a') + 1))
    return result


print(encode_symbol_cesar('abcdxyz', 3))
