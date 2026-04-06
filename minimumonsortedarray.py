def minimumonsortedarray(nums):
    left, right = 0, len(nums) - 1
    index = -1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] > nums[-1]:
            left = mid + 1
        else:
            index = mid
            right = mid-1
    return index


print(minimumonsortedarray([4, 5, 6, 7, 0, 1, 2]))