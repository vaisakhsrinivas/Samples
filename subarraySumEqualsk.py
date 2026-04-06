def subArraySumEqualsk(a,givensum):
    s = givensum
    s1 = {0:1}
    sum = 0
    count = 0
    l = len(a)

    for n in a:

        sum = sum + n

        if sum-givensum in s1:

            count = count + s1[sum-givensum]

        if sum not in s1:

            s1[sum] = 1

        else:

            s1[sum] += 1

    return count






a = [1,1,1]
s = 2

print(subArraySumEqualsk(a, 2))