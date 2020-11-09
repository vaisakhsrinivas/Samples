def rev(N):

    reverse = 0

    while (N > 0):

        a =  N % 10
        reverse = reverse * 10 + a
        N = N // 10

    return reverse



print(rev(123))