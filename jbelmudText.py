'''Given a string, return a jumbled version of that string where each word is transformed using the following constraints:

The first and last letters of the words remain in place
All letters between the first and last letter are sorted alphabetically.
The input strings will contain no punctuation, and will be entirely lowercase.'''

def jbelmu(text):

    words = text.split()
    result = []

    for word in words:
        if len(word) <= 3:
            result.append(word)
        else:
            first, last = word[0], word[-1]
            middle = "".join(sorted(word[1:-1]))
            result.append(first+middle+last)
            '''first, last = word[0], word[-1]
            middle = list(word[1:-1])

            # manual bubble sort approach using ord()
            for i in range(len(middle)):
                for j in range(len(middle) - 1 - i):
                    if ord(middle[j]) > ord(middle[j + 1]):
                        middle[j], middle[j + 1] = middle[j + 1], middle[j]

            result.append(first + "".join(middle) + last)'''
    return " ".join(result)

print(jbelmu("hello world")) #should return "hello wlord".
print(jbelmu("i love jumbled text")) #should return "i love jbelmud text".
print(jbelmu("freecodecamp is my favorite place to learn to code")) #should return "faccdeeemorp is my faiortve pacle to laern to cdoe".
print(jbelmu("the quick brown fox jumps over the lazy dog")) #should return "the qciuk borwn fox jmpus oevr the lazy dog"