'''
Given a string, return a compressed version of the string using the following rules:
The first occurrence of a word remains unchanged.
Subsequent occurrences are replaced with the position of the first occurrence, where the first word is at position 1.
Words are separated by a single space.
For example, given "practice makes perfect and perfect practice makes perfect", return "practice makes perfect and 3 1 2 3".
'''
from curses.ascii import isdigit


def decompress(s):

    stringsplit = s.split()
    position = {}
    result = []

    for i, token in enumerate(stringsplit):
        pos = i+1
        if token.isdigit():
            word = position[int(token)]
        else:
            word = token

        position[pos] = word
        result.append(word)
    return " ".join(result)



s = "practice makes perfect and 3 1 2 3"
print(decompress(s))