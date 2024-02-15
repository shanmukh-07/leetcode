class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        s = sum(nums)
        for i in range(len(nums)-1,-1,-1):
            s -= nums[i]
            if nums[i] < s:
                return s + nums[i]
        return -1