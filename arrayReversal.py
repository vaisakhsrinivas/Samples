def reversal (a):
    l = len(a)

    f = 0
    la = l-1

    while f < la:
        a[f],a[la] = a[la],a[f]
        f = f + 1
        la = la-1
    return a

a = [1,2,4,0]
print(reversal(a))