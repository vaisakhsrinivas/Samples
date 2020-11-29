def reverseVowels(s):
    vowels = ["a", "e", "i", "o", "u"]
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


print(reverseVowels("hello"))


