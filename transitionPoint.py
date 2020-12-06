def transitionPoint(arr, n):
    for i in range(n):
        if arr[i] == 1:
            return i

    return -1


a = [0,0,0,0,1]
l = len(a)
print(transitionPoint(a, l))