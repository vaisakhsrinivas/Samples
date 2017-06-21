import string

size = int(input())
a = string.ascii_lowercase

for i in range(size-1,0,-1):
    r = ["-"]*(size * 2 - 1)

    for j in range(0, size-i):
        r[size-1-j]=a[j+i]
        r[size-1+j]=a[j+i]
    print("-".join(r))


for i in range(0, size):
    row = ["-"] * (size * 2 - 1)
    for j in range(0, size - i):
        row[size - 1 - j] = a[j + i]
        row[size - 1 + j] = a[j + i]
    print("-".join(row))