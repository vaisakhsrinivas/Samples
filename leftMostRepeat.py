def leftMostRepeat(s):
    l = len(s)

    for i in range (0,l):
        for j in range (i+1,l):
            if s[i] == s[j]:
                return i
    return -1

s = "abcdc"
print(leftMostRepeat(s))
