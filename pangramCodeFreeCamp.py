'''
Given a word or sentence and a string of lowercase letters, determine if the word or sentence uses all the letters
from the given set at least once and no other letters.

Ignore non-alphabetical characters in the word or sentence.
Ignore letter casing in the word or sentence.

'''


def pangram(sentence, letter):

    letterset = set(letter)
    sentenceset = set(s.lower() for s in sentence if s.isalpha())
    return letterset == sentenceset



print(pangram("hello", "helo")) #should return True
print(pangram("hello", "hel")) #should return False
print(pangram("hello", "helow")) #should return False
print(pangram("hello world", "helowrd")) #should return True
print(pangram("Hello World!", "helowrd")) #should return True
print(pangram("Hello World!", "heliowrd")) #should return False
print(pangram("freeCodeCamp", "frcdmp")) #should return False
print(pangram("The quick brown fox jumps over the lazy dog.", "abcdefghijklmnopqrstuvwxyz")) #should return True

