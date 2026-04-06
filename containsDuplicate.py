def containsDuplicate(nums):

    duplicate = {}

    for i in nums:
        if i in duplicate:
            duplicate[i] += 1
        else:
            duplicate[i] = 1

    for j in duplicate:
        if duplicate[j] >= 2:
            return True
    return False


n = [1,2,3,5,5]
print(containsDuplicate(n))
