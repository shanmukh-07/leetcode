class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        l = len(nums)
        j = 0
        res = 0
        d = {}
        for i in range(l):
            d[nums[i]] = d.get(nums[i],0)+1
            while d[nums[i]] > k:
                d[nums[j]] -= 1
                j += 1
            res = max(res,i-j+1)
        return res