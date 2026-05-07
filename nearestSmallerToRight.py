def nearestSmallerToRight(s):

    stk = []
    result = [-1] * len(s)
    for i in range(len(s)):
        while stk and s[i] < s[stk[-1]]:
            index = stk.pop()
            result[index] = s[i]
        stk.append(i)
    return result



arr = [4,5,2,10,8]
arr1 = [1,2,3,4,5]
print(nearestSmallerToRight(arr))
print(nearestSmallerToRight(arr1))