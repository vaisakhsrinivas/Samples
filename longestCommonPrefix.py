def lcp(p , s):

    i = 0
    j = 0

    l1 = len(p)
    l2 = len (s)


    result = ""


    while i < l1-1 and j < l2-1:

        if p[i] != s[i]:
            break

        else:

            result = result + p[i]

        i = i + 1
        j = j + 1
    return result



s = ["flower", "flow", "flight"]

prefix = s[0]

for i in range (1,len(s)):

    r =  lcp(prefix, s[i])

print(r)


