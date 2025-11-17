class Solution:
    def isValid(self, s: str) -> bool:
        d = {"{":"}", "[":"]", "(":")"}
        st  = []

        for i in s:
            if i in d:
                st.append(i)
            elif i in d.values():
                if not st:
                    return False
                combination = st.pop()
                if d.get(i) == combination:
                    return True
        return not st
    
check = "[]("
c = Solution()
print(c.isValid(check))