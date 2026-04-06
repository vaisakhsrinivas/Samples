#countfunction
def minimumSwaps(arr):

    count = 0
    for j in range(0, len(arr)):
        while arr[j] != j+1:
            t = arr[j]-1
            arr[j],arr[t] = arr[t],arr[j]
            count = count + 1
    return count


n = int(input())

arr = list(map(int, input().rstrip().split()))

res = minimumSwaps(arr)

print(res)

