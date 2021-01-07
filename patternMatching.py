def patternMatching(s, p):
    stringlength = len(s)
    patternlength = len(p)

    c = 0

    index = []

    while c < stringlength:
        if s[c:c+patternlength] == p:
            index.append(c)
        c = c+1
    return index


s = "GCTCTCTGCCTCTACTTA"
p = "CT"

print(patternMatching(s,p))