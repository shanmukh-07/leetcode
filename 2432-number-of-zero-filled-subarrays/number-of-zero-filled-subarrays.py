class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        c = 0
        s = 0
        for i in nums:
            if i == 0:
                c += 1
                s += c
            else:
                c = 0
        return s