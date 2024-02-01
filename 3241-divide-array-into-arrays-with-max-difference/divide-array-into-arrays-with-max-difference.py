class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        l = []
        c = 0
        for i in range(0,n,3):
            a = nums[i:i+3]
            l.append(a)
            if abs(a[2]-a[0]) <= k:
                c += 1
        if len(l) == c:
            return l
        return []