def sortedArraySwap(arr):

    l = len(arr)
    for i in range(1, l):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] = key

    for k in range(1, l):
        if k%3 == 0:
            arr[k], arr[k-1] = arr[k-1], arr[k]
    return arr


a = [1,2,3,4,5,6,7,8,9,10]
arr = [12, 5, 8, 1, 3, 10, 2, 7, 6, 4, 9, 11]
print(sortedArraySwap(a))
print(sortedArraySwap(arr))