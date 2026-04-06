def subArrayWithGivenSum(a,givensum):
    s = givensum
    s1 = set()
    sum = 0
    l = len(a)

    for i in range(0,l):

        sum = sum + a[i]

        if sum == givensum:
            return True
        if sum - givensum in s1:
            return True
        else:
            s1.add(sum)
    return False




a = [5,8,6,13,3,-1]
s = 22

print(subArrayWithGivenSum(a, 22))
