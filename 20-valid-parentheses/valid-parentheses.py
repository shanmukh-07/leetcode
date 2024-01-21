class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for i in s:
            if not st:
                st.append(i)
            elif st[-1] == '(' and i == ')':
                st.pop(-1)
            elif st[-1] == '{' and i == '}':
                st.pop(-1)
            elif st[-1] == '[' and i == ']':
                st.pop(-1)
            else:
                st.append(i)
        if not st:
            return True
        return False