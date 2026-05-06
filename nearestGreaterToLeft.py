def nearestGreaterToLeft(num):

    l = len(num)
    stk = []
    result = [-1] * l

    for i in reversed(range(l)):

        while stk and num[i] > num[stk[-1]]:
            index = stk.pop()
            result[index] = num[i]
        stk.append(i)

    return result



print(nearestGreaterToLeft([1,3,2,4]))

