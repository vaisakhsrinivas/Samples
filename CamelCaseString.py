def CamelCaseString (s):
    count = 1
    for i in s:
        if i.isupper():
            count += 1
    return count


text = input()
result = CamelCaseString(text)
print(result)