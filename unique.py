def ulist(l):
    x = []
    for a in l:
        if a not in x:
            x.append(a)
    return x

l = [int (i) for i in input().split()]
unique = ulist(l)
print(unique)