def mul(n):
    for row in range(1,n+1):
        print(*("{:3}".format(row*col) for col in range(1, n+1)))





mul(12)