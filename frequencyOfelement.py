def frequency(a):
    le = len(a)
    f = 1
    i = 0

    while i < le:
        while i < le and a[i] == a[i-1]:
            f=f+1
            i=i+1
        print(a[i-1],f)
        f = 1
        i = i+1



a = [1,2,3,5,5,6,7]
frequency(a)