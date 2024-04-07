class Solution:
    def checkValidString(self, s: str) -> bool:
        st = []
        sr = []
        for ind,val in enumerate(s):
            if val == "(":
                st.append(ind)
            elif val == ")":
                if st:
                    st.pop()
                elif sr:
                    sr.pop()
                else:
                    return False
            else:
                sr.append(ind)
        while st and sr:
            if st[-1]>sr[-1]:
                return False
            st.pop()
            sr.pop()
        print(st,sr)
        return len(st) == 0