def equilibriumpoint(a):

    l = len(a)

    for i in range(l):
        right_sum = 0
        left_sum = 0

        for j in range(i):
            left_sum = left_sum + a[j]

        for j in range(i+1, l):
            right_sum =right_sum + a[j]

        if left_sum == right_sum:
            return i+1

    return -1




l = [20,17,42,25,32,32,30,32,37,9,2,33,31,17,14,40,9,12,36,21,8,33,6,6,10,37,12,26,21,3]

print(equilibriumpoint(l))