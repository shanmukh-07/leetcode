class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        d = collections.Counter({0:1})
        c = 0
        ps = 0
        for i in nums:
            ps += i
            c += d[ps-goal]
            d[ps] += 1
        return c