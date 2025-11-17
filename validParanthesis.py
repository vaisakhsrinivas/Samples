class Solution:
    def isValid(self, s: str) -> bool:
        d = {"}":"{", "]":"[", ")":"("}
        st  = []

        for i in s:
            if i in d.values():
                st.append(i)
            elif i in d:
                if not st:
                    return False
                combination = st.pop()
                if d[i] != combination:
                    return False
        return not st

check = "[]("
c = Solution()
print(c.isValid(check))