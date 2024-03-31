class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        c = 0
        mx,mn,ne = -1,-1,-1
        for i,j in enumerate(nums):
            if j == minK:
                mn = i
            if j == maxK:
                mx = i
            if not minK <= j <= maxK:
                ne = i
            c += max(0,min(mn,mx)-ne)
        return c