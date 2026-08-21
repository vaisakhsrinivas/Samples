class SolutiontwoSum:
    def twoSum (self, nums: list[int], target:int) -> list[int]:

        result = {}
        l = len(nums)

        for i in range (l):
            d = target - nums[i]
            if d in result:
                return [i, result[d]]
            result[nums[i]] = i
        return []
    
s = SolutiontwoSum()

n = [2,7,11,15]
t = 9

print(s.twoSum(n,t))