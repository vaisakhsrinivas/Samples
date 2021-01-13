def equilibriumPoint(A, N):
    total_sum = sum(A)
    leftsum = 0
    for i, num in enumerate(A):

        total_sum -= num

        if leftsum == total_sum:
            return i+1
        leftsum += num

    return -1



A = [1,3,5,2,2]
N = len(A)

print(equilibriumPoint(A, N))