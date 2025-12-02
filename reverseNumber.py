def rev(N):

    if N < 0:
        return -1 * convert(abs(N))
    else:
        return convert(N)
    
def convert(N):
    reverse = 0
    x = N
    while (x>0):
        a =  x % 10
        reverse = reverse * 10 + a
        x = x // 10
    return reverse

print(rev(-123))