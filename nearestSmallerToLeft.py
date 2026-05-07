def nearestSmallerToLeft(s):

    result = [-1] * len(s)
    stk = []
    for i in reversed(range(len(s))):
        while stk and s[i] < s[stk[-1]]:
            index = stk.pop()
            result[index] = s[i]
        stk.append(i)

    return result


print(nearestSmallerToLeft([4,5,2,10,8]))
