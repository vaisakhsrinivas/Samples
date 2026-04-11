def reverseVowels(s):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    l = len(s)
    start = 0
    end = l-1
    s = list(s)

    while start < end:
        if s[start] in vowels and s[end] in vowels:
            s[start], s[end] = s[end], s[start]
            start = start + 1
            end = end - 1
        elif s[start] in vowels:
            end = end-1
        elif s[end] in vowels:
            start = start+1
        else:
            start = start + 1
            end = end - 1


    return "".join(s)


'''
Alternative solution using set

def reverseVowels(s):
    vowels = set("aeiouAEIOU") # Using a set for faster lookup
    s = list(s)
    start, end = 0, len(s) - 1

    while start < end:
        if s[start] not in vowels:
            start += 1
        elif s[end] not in vowels:
            end -= 1
        else: # Both are vowels
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1

    return "".join(s)
'''


print(reverseVowels("hello"))


