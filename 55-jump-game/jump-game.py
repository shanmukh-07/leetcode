class Solution:
    def canJump(self, nums: List[int]) -> bool:
        ind = 0
        for i in range(len(nums)):
            if ind < i:
                return False
            ind = max(ind,nums[i]+i)
        return True