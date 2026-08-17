'''
Given an array of numbers and an integer target,
find two unique numbers in the array that add up to the target value.
Return an array with the indices of those two numbers, or "Target not found" if no two numbers sum up to the target.
The returned array should have the indices in ascending order.
'''


def find_target(arr, target):

    d = {}
    for i in range(len(arr)):
        diff = target - arr[i]
        if diff in d:
            return [d[diff], i]
        else:
            d[arr[i]] = i
    return "Target not found"

print(find_target([2, 7, 11, 15], 9)) #should return [0, 1].
print(find_target([3, 2, 4, 5], 6)) #should return [1, 2].
print(find_target([1, 3, 5, 6, 7, 8], 15)) #should return [4, 5].
print(find_target([1, 3, 5, 7], 14))  #return 'Target not found'
