def reverseK (queue, k, n):

    stack = []
    temp_q_one = queue[k:]
    i = 0

    while (i < k):
        stack.append(queue.pop(0))
        i = i + 1

    temp_q_two = []
    j = 0
    while (j < k):
        temp_q_two.append(stack.pop(-1))
        j = j + 1

    queue =  temp_q_two + temp_q_one
    return queue



q = [1,2,3,4,5]
k = 4
n = len(q)

print(reverseK(q,k,n))