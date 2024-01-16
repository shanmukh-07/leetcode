class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        l = [1 for i in range(n)]
        m = 0
        for i in range(n):
            t = 0
            for j in range(i):
                if nums[j]<nums[i]:
                    if l[j]>t:
                        t = l[j]
            l[i]+=t
            if l[i]>m:
                m=l[i]
        return m