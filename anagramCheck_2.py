'''
Given two strings, determine if they are anagrams of each other (contain the same characters in any order).

Ignore casing and white space.
'''


def are_anagrams(word1, word2):

    word1 = word1.replace(" ", "").lower()
    word2 = word2.replace(" ", "").lower()

    dict1 = {}
    dict2 = {}

    for word in word1:
        dict1[word] = dict1.get(word, 0) + 1
    for word in word2:
        dict2[word] = dict2.get(word, 0) + 1

    return dict1 == dict2

print(are_anagrams("listen", "silent")) #should return true.
print(are_anagrams("School master", "The classroom")) #should return true.
print(are_anagrams("A gentleman", "Elegant man")) #should return true.
print(are_anagrams("Hello", "World")) #should return false.
print(are_anagrams("apple", "banana")) #should return false.
print(are_anagrams("cat", "dog")) #should return false.