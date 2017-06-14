def listmultiply(l):
    total = l[0]
    for a in l:
        total *= a
    return total

l = [int (i) for i in input().split()]
multiply = listmultiply(l)
print(multiply)