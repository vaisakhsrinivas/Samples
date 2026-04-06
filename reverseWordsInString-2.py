class Solution:
    def reverseWords(self, s: str) -> str:
        reverse = []
        s = s.split()

        while s:
            word = s.pop()
            if word != '':
                reverse.append(word)
        return ' '.join(reverse)

        
s = "the sky is blue"
c = Solution()
print(c.reverseWords(s))