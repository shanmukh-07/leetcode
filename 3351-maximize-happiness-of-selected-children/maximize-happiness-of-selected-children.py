class Solution:
    def maximumHappinessSum(self, h: List[int], k: int) -> int:
        h.sort(reverse = True)
        s = 0
        for i in range(k):
            tv = h[i] - i
            s += max(0,tv)
        return s