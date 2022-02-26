def twoSum(givenlist, target):

    result = {}
    l = len(givenlist)

    for i in range(l):
        diff = target - givenlist[i]
        if diff in result:
            return [i,result[diff]]
        result[givenlist[i]] = i



givenlist = [2,7,11,15]
target = 9
print(twoSum(givenlist,target))