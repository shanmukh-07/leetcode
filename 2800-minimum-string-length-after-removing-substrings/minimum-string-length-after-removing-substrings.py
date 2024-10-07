class Solution:
    def minLength(self, s: str) -> int:
        st = []
        for i in s:
            if st and ((st[-1] == "A" and i == "B") or (st[-1] == "C" and i == "D")):
                st.pop()
            else:
                st.append(i)
        return len(st)