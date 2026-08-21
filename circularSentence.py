'''
A sentence is a list of words that are separated by a single space with no leading or trailing spaces.

For example, "Hello World", "HELLO", "hello world hello world" are all sentences.
Words consist of only uppercase and lowercase English letters. Uppercase and lowercase English letters are considered different.

A sentence is circular if:

The last character of each word in the sentence is equal to the first character of its next word.
The last character of the last word is equal to the first character of the first word.
For example, "leetcode exercises sound delightful", "eetcode", "leetcode eats soul" are all circular sentences. However, "Leetcode is cool", "happy Leetcode", "Leetcode" and "I like Leetcode" are not circular sentences.

Given a string sentence, return true if it is circular. Otherwise, return false.
'''


def circularSentence(sentence: str) -> bool:

    l = len(sentence)

    if sentence[0] != sentence[-1]:
        return False

    for i in range(1, l):
        if sentence[i] == ' ':
            if sentence[i-1] != sentence[i+1]:
                return False
    return True

print(circularSentence("leetcode exercises sound delightful"))
print(circularSentence("eetcode"))
print(circularSentence("leetcode is cool"))
print(circularSentence("happy Leetcode"))