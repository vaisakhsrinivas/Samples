def largestAndSecondLargest(sizeOfArray, arr):
    mx=max(arr[0],arr[1])
    secondmax=min(arr[0],arr[1])
    li = []
    for i in range(2,sizeOfArray):
        if arr[i]>mx:
            secondmax=mx
            mx=arr[i]
        elif arr[i]>secondmax and mx != arr[i]:
            secondmax=arr[i]
        elif mx == secondmax:
            secondmax = -1

    li.append(mx)
    li.append(secondmax)
    return li




arr = [10,10,10,10,10]
n = len(arr)

print(largestAndSecondLargest(n, arr))
