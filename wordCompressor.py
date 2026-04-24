'''
Given a string, return a compressed version of the string using the following rules:

The first occurrence of a word remains unchanged.
Subsequent occurrences are replaced with the position of the first occurrence, where the first word is at position 1.
Words are separated by a single space.
For example, given "practice makes perfect and perfect practice makes perfect", return "practice makes perfect and 3 1 2 3".

'''

def compress(s):

    words = s.split()
    position = {}
    result = []

    for i in range(len(words)):
        if words[i] not in position:
            position[words[i]] = i+1
            result.append(words[i])
        else:
            result.append(str(position[words[i]]))
    return " ".join(result)


s = "practice makes perfect and perfect practice makes perfect"
print(compress(s))