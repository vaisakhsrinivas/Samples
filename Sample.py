def countletter(n, a):
    c = 0
    for i in n:
        if a == i:
            c = c+1
    return c


n = str (input().strip())
a = str(input())
occur = countletter(n, a)
print(occur)

##print(n.count(a))



