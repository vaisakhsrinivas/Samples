class Solution:
    def isValid(self, s: str) -> bool:
        d = {"{":"}", "[":"]", "(":")"}
        st  = []

        for i in s:
            if i in d:
                st.append(i)
            else:
                if not st or d[st.pop()] != i:
                    return False
        return len(st) == 0
    
check = "[]("
c = Solution()
print(c.isValid(check))