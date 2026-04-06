class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        def find_gcd(pattern, target):
            constructed = ""
            while (len(constructed) < len(target)):
                constructed += pattern
            return constructed == target

        lstr1 = len(str1)
        lstr2 = len(str2)

        for i in range (min (lstr1, lstr2), 0, -1):
            candidate = str1[:i]

            if find_gcd(candidate, str1) and find_gcd(candidate, str2):
                return candidate
        return ""
        


str1 ="ABCABC"
str2 = "ABC"
c = Solution()
print(c.gcdOfStrings(str1, str2))