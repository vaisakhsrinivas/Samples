def subarray(a, s, n):
    for i in range (n):
        subarraysum = a[i]
        j = i+1
        while j <= n:
            if subarraysum == s:
                print(i+1, j)
                return 1
            if subarraysum > s or j == n:
                break
            subarraysum = subarraysum + arr[j]
            j += 1
    print("-1")
    return 0

tc = int(input())

for i in range(tc):
    arr_size, given_sum = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]
    l = len(arr)
    subarray(arr, given_sum, l)