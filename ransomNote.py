class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        ransom = dict()
        mag = dict()


        for i in magazine:
            if i not in mag:
                mag[i] = 1
            else:
                mag[i] += 1

        for i in ransomNote:
            if i not in ransom:
                ransom[i] = 1
            else:
                ransom[i] += 1

        for i in ransom:
            if i not in mag.keys() or ransom[i] > mag[i] :
                return False
        return True


ransom_solution = Solution()
print(ransom_solution.canConstruct('aa','aab'))