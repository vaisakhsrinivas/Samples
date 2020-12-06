def convertToWave(A, N):

    for i in range(0,N,2):

        if i < N-1 and A[i] < A[i+1]:
            A[i], A[i+1] = A[i+1], A[i]

    return A



a = [2,4,7,8,9,10]
print(convertToWave(a, len(a)))