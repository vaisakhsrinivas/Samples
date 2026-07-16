'''
Given a string, convert it to Pig Latin using the following rules:

If a word begins with a vowel ("a", "e", "i", "o", or "u"), add "way" to the end. For example, "universe" converts to "universeway".
If a word begins with one or more consonants, move them to the end and add "ay". For example, "hello" converts to "ellohay".
Preserve the case of the first letter. For example, "Hello" converts to "Ellohay".
'''

def pig_latin(s):

    result = []
    vowels = ["a", "e", "i", "o", "u"]

    for word in s.split():
        upper = word[0].isupper()
        w = word.lower()

        if w[0] in vowels:
            final = w + "way"
        else:
            i = 0
            while i < len(w) and w[i] not in vowels:
                i += 1
                final = w[i:] + w[:i] + "ay"
        if upper:
            final = final[0].upper() + final[1:]
        result.append(final)
    return " ".join(result)

print(pig_latin("universe")) #should return "universeway".
print(pig_latin("hello")) # should return "ellohay".
print(pig_latin("hello universe")) #should return "ellohay universeway".
print(pig_latin("Hello universe")) #should return "Ellohay universeway".
print(pig_latin("Pig Latin is fun")) #should return "Igpay Atinlay isway unfay".
print(pig_latin("The quick brown fox jumped over the lazy dog")) #should return "Ethay uickqay ownbray oxfay umpedjay overway ethay azylay ogday"