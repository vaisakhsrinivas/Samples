class SolutionLongestCommonPrefix:
    def LongestCommonPrefix (self, strs: list[str]) -> str:
        if len(strs) == 0:
            return ""
        prefix = strs[0]
        for i in range (1, len(strs)):
            while strs[i].find(prefix) != 0:
                prefix = prefix[0: len(prefix)-1]
                if prefix == "":
                    return ""
        return prefix
    



lcp = SolutionLongestCommonPrefix()
strs = ["flower","flow","flight"]
strs1 = ["racecar","race","racecar3"]
print(lcp.LongestCommonPrefix(strs))
print(lcp.LongestCommonPrefix(strs1))

