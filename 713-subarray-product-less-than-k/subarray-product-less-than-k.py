class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        c = 0
        p = 1
        l = 0
        for r,n in enumerate(nums):
            p *= n
            while p >= k:
                p /= nums[l]
                l += 1
            c += r-l+1
        return c