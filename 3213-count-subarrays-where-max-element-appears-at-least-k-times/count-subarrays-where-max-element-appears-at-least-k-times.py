class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        m = max(nums)
        n = len(nums)
        cnt = 0
        ans = 0
        l = 0
        for i in range(n):
            if nums[i] == m:
                cnt += 1
            while cnt >= k:
                if nums[l] == m:
                    cnt -= 1
                l += 1
            ans += l
        return ans