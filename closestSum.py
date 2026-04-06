def ReturnPairs (a,s):
    n = len(a)
    sum = 0
    r = []
    for i in range (0,n):
        for j in range(i+1,n):

            sum = a[i] + a[j]

            if sum < s:
                r.append(sum)
    r.sort()

    s1 = r[-1]

    for i in range (0,n):
        for j in range(i+1,n):

            sum = a[i] + a[j]

            if s1 == sum:

                print(a[i],a[j])





l = [10, 22, 28, 29, 30, 40]
m = 54
ReturnPairs(l,m)



