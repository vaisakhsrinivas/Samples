'''
Given a word, return its score using a standard letter-value table:
Upper and lowercase letters have the same value.
'''


def get_word_score(word):
    return sum(ord(c.lower()) - ord('a') + 1 for c in word if c.isalpha())


print(get_word_score("hi")) # should return 17.
print(get_word_score("hello")) # should return 52.
print(get_word_score("hippopotamus")) # should return 169.
print(get_word_score("freeCodeCamp"))# should return 94.