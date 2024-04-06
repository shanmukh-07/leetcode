class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        st = []
        n = len(s)
        res = ""
        for i in range(n):
            if s[i] == '(':
                ind = len(res)
                st.append(ind)
            elif s[i] == ")":
                if len(st)>0:
                    ind = st[-1]
                    st.pop()
                    res = res[:ind]+"("+res[ind:]+")"
            else:
                res += s[i]
        return res