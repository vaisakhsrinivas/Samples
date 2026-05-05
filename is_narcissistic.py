def is_narcissistic(n):
    num = 0
    n = str(n)
    l = len(n)
    for i in range(l):
        num += int(n[i])**l
    return int(n) == num



print(is_narcissistic(5))
print(is_narcissistic(153))
print(is_narcissistic(154))