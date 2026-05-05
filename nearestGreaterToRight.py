def nearestGreaterToRight(s):

    l = len(s)
    stk = []
    result = [-1]*l
    for i in range(l):
        while stk and s[i] > s[stk[-1]]:
            index = stk.pop()
            result[index] = s[i]
        stk.append(i)

    return result


s = [1,3,2,4]
print(nearestGreaterToRight(s))
