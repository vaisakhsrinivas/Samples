def equilibriumpoint(a):

    right_sum = 0
    left_sum = 0
    l = len(a)

    for i in range(1,l):
        right_sum = right_sum + a[i]

    i, j = 0, 1


    while j < l:

        right_sum = right_sum - a[j]
        left_sum = left_sum + a[i]

        if right_sum == left_sum:

            return i+1

        i = i + 1
        j = j + 1

    return -1




l = [6,4,5,10]

print(equilibriumpoint(l))