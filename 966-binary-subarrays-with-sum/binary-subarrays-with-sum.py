class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        c,res,d = 0,0,0
        for i in range(len(nums)):
            if nums[i] == 1:
                goal -= 1
                c = 0
            while goal == 0 and d <= i:
                goal += nums[d]
                d += 1
                c += 1
                if d > i-goal+1:
                    break
            while goal < 0 :
                goal += nums[d]
                d += 1
            res += c
        return res
        # d = collections.Counter({0:1})
        # c = 0
        # ps = 0
        # for i in nums:
        #     ps += i
        #     c += d[ps-goal]
        #     d[ps] += 1
        # return c