def sorted (a):
    l = len(a)

    f = 0
    la = l-1

    for i in range (l):
        if a[f] > a[la]:
            return False

    return True


a = [1,2,4,0]
print(sorted(a))