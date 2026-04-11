'''

Given an array of numbers where all but one number follow a pattern, return a new array with the one number that doesn't follow the pattern fixed.

The pattern will be one of:

The numbers increase from one to the next by a fixed amount (addition).
The numbers decrease from one to the next by a fixed amount (subtraction).
For example, given [2, 4, 7, 8, 10] return [2, 4, 6, 8, 10].

Examples:
- prankNumber([2, 4, 7, 8, 10]) -> [2, 4, 6, 8, 10]
- prankNumber([10, 8, 6, 4, 2]) -> [10, 8, 6, 4, 2]
- prankNumber([1, 3, 5, 7, 9]) -> [1, 3, 5, 7, 9]

'''

def prankNumber(nums):

    if len(nums) < 2:
        return nums

    diff = [nums[i] - nums[i-1] for i in range(1, len(nums))]
    step = max(set(diff), key=diff.count)

    for i in range(1, len(nums)):
        if nums[i] - nums[i-1] != step:
            if i == 1 and i+1 < len(nums) and nums[i+1] - nums[i] == step:
                nums[0] = nums[1] - step
            else:
                nums[i] = nums[i-1] + step
            break
    return nums


nums = [2, 4, 7, 8, 10]
print(prankNumber(nums))