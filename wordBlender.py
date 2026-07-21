'''
Given two words, return a new word by combining the first half of the first word with the second half of the second word.

For odd-length words, the first half is the shorter half.
'''


def blend_words(word1, word2):

    lword1 = len(word1)
    lword2 = len(word2)
    mword1 = lword1 // 2
    mword2 = lword2 // 2
    return word1[:mword1] + word2[mword2:]


print(blend_words("turtle", "toucan")) # should return "turcan".
print(blend_words("chipmunk", "flamingo")) # should return "chipingo".
print(blend_words("falcon", "pelican")) # should return "falican".
print(blend_words("hyena", "iguana")) #should return "hyana".
print(blend_words("scorpion", "gorilla")) #should return "scorilla".
print(blend_words("platypus", "wolverine")) #should return "platerine".