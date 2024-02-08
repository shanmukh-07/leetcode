class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        l = len(nums)
        ll = l//2
        s = 0
        for i in range(l):
            s += abs(nums[i]-nums[ll])
        return s