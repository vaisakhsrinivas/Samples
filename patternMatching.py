def patternMatching(s, p):
    stringlength = len(s)
    patternlength = len(p)

    start = 0
    end = 0

    while start < stringlength:
        if s[start+end] != p[end]:
            start = start + 1
            end = 0
            continue
        end = end + 1

        if end == patternlength:
            return start
    return -1


s = "CAbCCDAA"
p = "AA"

print(patternMatching(s,p))