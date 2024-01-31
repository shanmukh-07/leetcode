class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        n = len(t)
        l = [0]*n
        st = []
        for i in range(n):
            while st and t[i] > t[st[-1]]:
                p = st.pop()
                l[p] = i-p
            st.append(i)
        return l