'''
Given two strings, return a new string that interleaves their characters one at a time. If one string is longer, append the remaining characters at the end.

Begin with the first character of the first string.

'''







def zip_strings(a, b):
    lena = len(a)
    lenb = len(b)
    result = ""

    i = 0
    j = 0

    while i < lena and j < lenb:
        result = result + a[i] + b[j]
        i += 1
        j += 1
    while i < lena:
        result = result + a[i]
        i += 1
    while j < lenb:
        result = result + b[j]
        j += 1

    return result


print(zip_strings("abc", "123"))
print(zip_strings("python", "javascript"))
print(zip_strings("acegikmoqsuwy", "bdfhjlnprtvxz"))