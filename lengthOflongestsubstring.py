s = "abcabcbb"

d = dict()

i = 0
j = 0

l = len(s)


res = 0


while i < l and j < l:

    if s[j] not in d:
        d[s[j]] = 1
        j = j + 1

        res = max(res, j-i)

    else:

        d.pop(s[j])
        i = i + 1

print(res)
