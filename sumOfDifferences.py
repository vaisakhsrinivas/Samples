def sumOfDifference(arr):

    '''total = 0
    for i in range(len(arr)-1):
        total += arr[i+1] - arr[i]
    return total'''

    return sum(arr[i+1]-arr[i] for i in range(len(arr)-1))


print(sumOfDifference([1, 3, 4]))
print(sumOfDifference([5, -3, 3, 9, 10]))
print(sumOfDifference([9, 6, 15, -20, 33, 14, 25, 16, -7]))