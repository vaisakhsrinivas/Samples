def removeDuplicates(a):

    l = len(a)
    result = 1
    for i in range (1,l):
        if a[i] != a[result-1]:
            a[result] = a[i]
            result = result + 1
    return a[:result]




a = [10,20,20,30,30,30,40]
print(removeDuplicates(a))
