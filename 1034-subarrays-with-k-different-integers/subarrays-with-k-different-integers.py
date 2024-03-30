class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        cnt = [0]*(len(nums)+1)
        res,l,m = 0,0,0
        for i in nums:
            cnt[i] += 1
            if cnt[i] == 1:
                k -= 1
                if k<0:
                    cnt[nums[m]] = 0
                    m += 1
                    l = m
            if k <= 0:
                while cnt[nums[m]] > 1:
                    cnt[nums[m]] -= 1
                    m += 1
                res += m-l+1
        return res