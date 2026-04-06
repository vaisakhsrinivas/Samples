def lrotate(a):
    le = len(a)

    t = a[0]
    for i in range (0,le-1):
            a[i] = a[i+1]
    a[le-1] = t

    return a


a = [1,2,3,5]
print(lrotate(a))