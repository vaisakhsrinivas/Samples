""" def lrotate(a):
    le = len(a)

    t = a[0]
    for i in range (0,le-1):
        a[i] = a[i+1]
    a[le-1] = t


def rotatedtimes(a, d):
    for i in range(0,d):
        lrotate(a)
    return a """

""" def rotatedtimes(a, d):
    d = d % len(a)  # Handle cases where d > len(a)
    return a[d:] + a[:d]  # Slicing to rotate the array """

""" def rotatedtimes(a, d):
    for i in range(d):
        t = a[0]
        for j in range(len(a)-1):
            a[j] = a[j+1]
        a[-1] = t
    return a
 """

def rotatedtimestoright(a, d):
    d = d % len(a)  # Handle cases where d > len(a)
    return a[-d:] + a[:-d]  # Slicing to rotate the array

a = [1,2,3,5]
print(rotatedtimestoright(a,2))