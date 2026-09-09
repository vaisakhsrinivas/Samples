'''
Given a string, determine if all the characters in the string are unique.

Uppercase and lowercase letters should be considered different characters.
'''


def all_unique(s):

    unique = set ()

    for char in s:
        if char not in unique:
            unique.add(char)
            continue
        else:
            return False
    return True


print(all_unique("abc")) #should return True.
print(all_unique("aA")) #should return True.
print(all_unique("QwErTy123!@")) #should return True.
print(all_unique("~!@#$%^&*()_+")) #should return True.
print(all_unique("hello")) #should return False.
print(all_unique("freeCodeCamp")) #should return False.
print(all_unique("!@#*$%^&*()aA")) #should return False.