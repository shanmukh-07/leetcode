class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num)<=k:
            return "0"
        st = []
        for i in num:
            while st and k>0 and st[-1]>i:
                st.pop()
                k-=1
            st.append(i)
        while k:
            st.pop()
            k-=1
        st = "".join(st).lstrip("0")
        return st if st else "0"