def moveZeros(a):
    l = len(a)
    count = 0
    for i in range (l):
        if a[i]!=0:
            a[i], a[count] = a[count],a[i]
            count = count+1
    return a


a = [10,8,0,0,12,0]
print(moveZeros(a))