class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        st = []
        i = 0
        ans = 0
        while i<len(s):
            if s[i] == '(':
                st.append(ans)
                ans = 0
            else:
                if ans == 0:
                    ans = st.pop()+1
                else:
                    ans = st.pop()+2*ans
            i += 1
        return ans