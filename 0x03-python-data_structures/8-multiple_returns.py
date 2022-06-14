#!/usr/bin/python3
def multiple_returns(sentence):
    """
    Gives a tuple with the length of string and it's first character

    Args:
        sentence: string to be used

    Return:
        tuple with length of string and it's first character
    """
    string_length = len(sentence)
    first_character = sentence[:1] if (sentence) else None
    return (string_length, first_character,)
