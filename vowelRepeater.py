'''
Given a string, return a new version of the string where each vowel is duplicated one more time than the previous vowel you encountered. For instance, the first vowel in the sentence should remain unchanged. The second vowel should appear twice in a row. The third vowel should appear three times in a row, and so on.

The letters a, e, i, o, and u, in either uppercase or lowercase, are considered vowels.
The original vowel should keeps its case.
Repeated vowels should be lowercase.
All non-vowel characters should keep their original case.
'''


def repeat_vowels(s):

    result = ""
    vowels = "aeiouAEIOU"
    count = 0

    for char in s:
        if char in vowels:
            count += 1
            result += char + char.lower() * (count - 1)
        else:
            result += char
    return result



print(repeat_vowels("hello world")) #should return "helloo wooorld".
print(repeat_vowels("freeCodeCamp")) #should return "freeeCooodeeeeCaaaaamp".
print(repeat_vowels("AEIOU")) #should return "AEeIiiOoooUuuuu".
print(repeat_vowels("I like eating ice cream in Iceland"))
#should return "I liikeee eeeeaaaaatiiiiiing iiiiiiiceeeeeeee creeeeeeeeeaaaaaaaaaam iiiiiiiiiiin Iiiiiiiiiiiiceeeeeeeeeeeeelaaaaaaaaaaaaaand"