def decodeways(s):


    if len(s) == 0 or s[0] == '0': return 0

    if len(s) == 1: return 1


    c1,c2 = 1,1

    for i in range (1, len(s)):

        d = ord(s[i]) - ord('0')
        dd = (ord(s[i-1]) - ord('0'))*10 + d

        c = 0

        if d > 0:
            c += c2

        if dd >= 10 and dd <= 26:
            c += c1

        c1 = c2
        c2 = c

    return c2



print(decodeways("1423"))

