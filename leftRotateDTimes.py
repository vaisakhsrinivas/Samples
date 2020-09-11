def lrotate(a):
    le = len(a)

    t = a[0]
    for i in range (0,le-1):
        a[i] = a[i+1]
    a[le-1] = t


def rotatedtimes(a, d):
    for i in range(0,d):
        lrotate(a)
    return a


a = [1,2,3,5]
print(rotatedtimes(a,2))