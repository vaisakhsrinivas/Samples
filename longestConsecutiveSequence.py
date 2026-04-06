def longestConsecutive(nums) -> int:
    count = 1
    currmax = 1
    l = len(nums)
    start = 1
    end = l-1

    if not nums:
        return 0

    sortednums = sorted(nums)

    while start<=end:
        if sortednums[start]-sortednums[start-1] == 1:
            count += 1
            start = start+1
            currmax = max(currmax, count)
        elif sortednums[start] == sortednums[start-1]:
            start += 1
        else:
            count = 1
            start += 1
    return currmax


#l = [100, 4, 200, 1, 3, 2]
l=[0,3,2,5,4,6,1,1]
result = longestConsecutive(l)
print(result)  # Output: 4        