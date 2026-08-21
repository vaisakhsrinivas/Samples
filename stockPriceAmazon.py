a = [55.39, 109.23, 48.29, 81.59, 105.53, 94.45, 12.24]


p = 0

for i in range(0,len(a)+1,1):
    if i != a[len(a)-1]:
        for j in range(i+1, len(a), 1):
            if a[j] > a[i]:
                profit = a[j] - a[i]
                if profit > p:
                    p = profit
                    buy = a[i]
                    sp = a[j]
    else:
        print("EOD")

print(buy)
print(sp)
print(p)


