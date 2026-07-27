'''
Given two strings of equal length, return the sum of the shortest distances between each pair of characters.

The input will only contain lowercase letters
The alphabet is treated as a circle, so the distance between a and z is 1.
'''


def letter_distance(string1, string2):

    dict = {char : i for i, char in enumerate("abcdefghijklmnopqrstuvwxyz")}
    total = 0

    for char1, char2 in zip(string1, string2):
        diff = abs(dict[char1] - dict[char2])
        total += min(diff, 26-diff)
    return total


print(letter_distance("abc", "bcd")) #should return 3.
print(letter_distance("abc", "xyz")) #should return 9.
print(letter_distance("encrypt", "decrypt")) #should return 10.
print(letter_distance("algorithm", "codeblock")) #should return 43.
print(letter_distance("lobster", "penguin")) #should return 47.
print(letter_distance("alligator", "crocodile")) #should return 55
