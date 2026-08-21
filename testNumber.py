#code
def subarray(a, s, n):
    for i in range (n):
        subarraysum = a[i]
        j = i+1
        while j <= n:
            if subarraysum == s:
                print(i, j-1)
            if subarraysum > s or j == n:
                break
            subarraysum = subarraysum + arr[j]
            j += 1
            print("-1")


tc = int(input())
for i in range(tc):
    arr_size, given_sum = [int(x) for x in input().split()]
    print(arr_size, given_sum)
    arr = [int(x) for x in input().split()]
    print(arr)
    l = len(arr)
    subarray(arr, given_sum, l)