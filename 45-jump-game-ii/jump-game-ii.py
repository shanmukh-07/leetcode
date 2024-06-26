class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        dp = [nums[0]]
        m = dp[-1]
        for i in range(1,len(nums)):
            if i <= dp[-1]:
                m = max(m,i+nums[i])
            else:
                dp.append(m)
                m = max(m,i+nums[i])
        return len(dp)