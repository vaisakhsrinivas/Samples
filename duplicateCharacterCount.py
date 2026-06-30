'''
Given two strings, return a count of characters from the second string that can be found in the first.

Duplicate characters in the second string are counted separately.
'''

def duplicate_character_count(str1, str2):
    countstr1 = {}
    countstr2 = {}
    duplicatecount = 0

    for char1 in str1:
        countstr1[char1] = 1 + countstr1.get(char1, 0)

    for char2 in str2:
        countstr2[char2] = 1 + countstr2.get(char2, 0)

        if char2 in countstr1:
            duplicatecount += 1
    return duplicatecount


print(duplicate_character_count("aloha", "hei")) # should return 1.
print(duplicate_character_count("jambo", "bonjour")) # should return 4.
print(duplicate_character_count("hello", "hola")) # should return 3.
print(duplicate_character_count("ola", "hej")) # should return 0.
print(duplicate_character_count("ciao", "konnichiwa")) #should return 5.
print(duplicate_character_count("merhaba", "xin chao")) #should return 2.
print(duplicate_character_count("hello world", "hello to everyone around the world")) #should return 26.