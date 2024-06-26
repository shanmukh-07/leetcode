class Solution:
    def canJump(self, nums: List[int]) -> bool:
        t = 0
        for i in nums:
            if t < 0:
                return False
            elif i > t:
                t = i
            t -= 1
        return True