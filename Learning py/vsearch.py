def search4letter(phrase: str, letters: str = 'aeiou') -> set:
    """Returns the characters in the defined set"""
    return set(letters).intersection(set(phrase))