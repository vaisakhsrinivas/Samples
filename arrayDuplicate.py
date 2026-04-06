def duplicate (a):
    l = len(a)
    res = 1

    for i in range(1,l):
        if a[i] != a[res-1]:
            a[res] = a[i]
            res = res + 1

    return res


a = [1,2,4,0,0,7]
print(duplicate(a))