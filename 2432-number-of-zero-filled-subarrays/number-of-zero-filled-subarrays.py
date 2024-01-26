class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        c = 0
        s = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                c += 1
            else:
                s += (c*(c+1))//2
                c = 0
        if c > 0:
            s += (c*(c+1)//2)
        return s