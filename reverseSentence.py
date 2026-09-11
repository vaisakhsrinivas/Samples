'''
Given a string of words, return a new string with the words in reverse order. For example, the first word should be at the end of the returned string, and the last word should be at the beginning of the returned string.

In the given string, words can be separated by one or more spaces.
The returned string should only have one space between words.
'''


def reverse_sentence(sentence):
    stk = []
    for word in sentence.split():
        stk.append(word)

    result = []
    while stk:
        result.append(stk.pop())
    return " ".join(result)
    #return " ".join(sentence.split()[::-1]) #pythonic oneline solution

print(reverse_sentence("world hello")) #should return "hello world".
print(reverse_sentence("push commit git")) #should return "git commit push".
print(reverse_sentence("npm  install   apt    sudo")) #should return "sudo apt install npm".
print(reverse_sentence("import    default   function  export")) #should return "export function default import".