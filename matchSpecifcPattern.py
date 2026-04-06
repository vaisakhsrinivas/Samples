def stringhash(s):

    d = dict()
    i = 0
    res = ""
    for char in s:

        if char not in d:
            d[char] = i
            i += 1
        res = res + str(d[char])
    return res

def patternmatching(Dict, pattern):

    result = []
    l = len(pattern)
    patternhash = stringhash(pattern)

    for w in Dict:

        if len(w) == l and stringhash(w) == patternhash:
            result.append(w)
    return result




Dict = ["abb","abc","xyz","xyy"]
pattern = "foo"
print(patternmatching(Dict, pattern))