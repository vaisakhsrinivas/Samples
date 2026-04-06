def binarysearchsquareroot(n):
    if n < 1:
        return None
    left, right = 1, n
    res = 0
    while left <= right:
        mid = (left + right) // 2
        if mid * mid == n:
            return mid
        elif mid * mid < n:
            left = mid + 1
        else:
            res = mid
            right = mid - 1
    return res-1 


print (binarysearchsquareroot(10))  # Output: 3



