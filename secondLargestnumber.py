def secondLargestnumber (a):
    largest = a[0]
    secondlargest = -1

    for i in range (1,len(a)):

        if a[i] > largest:
            secondlargest = largest
            largest = a[i]
        elif a[i] > secondlargest and a[i] < largest:
            secondlargest = a[i]

    return secondlargest



duplicatevalues = [12, 35, 1, 10, 35, 1]
sample = [10,30,50,40,60]
samevalues = [12,12,12,12,12]

print(secondLargestnumber(duplicatevalues))
print(secondLargestnumber(sample))
print(secondLargestnumber(samevalues))