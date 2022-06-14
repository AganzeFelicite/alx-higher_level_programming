#!/usr/bin/python3
def remove_char_at(str, n):
    return ''.join([str[i] for i in range(len(str)) if i != n])
