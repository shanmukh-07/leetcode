class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p = 0
        st = []
        i = len(prices)-2
        st.append(prices[-1])
        while i>=0:
            if st[-1] < prices[i]:
                st.append(prices[i])
            else:
                p = max(p,st[-1]-prices[i])
            i -= 1
        return p