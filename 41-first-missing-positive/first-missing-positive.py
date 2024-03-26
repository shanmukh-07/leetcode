class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 1
        s = set(nums)
        while i in s:
            i += 1
        return i