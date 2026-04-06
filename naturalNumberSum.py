s = 0

for i in range(1,1001):

    if (i%3 == 0) or (i%7==0):

        s = s + i

print(s)