class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        l = []
        c = True
        for i in range(0,n,3):
            a = nums[i:i+3]
            l.append(a)
            if abs(a[2]-a[0]) > k:
                c = False
        if c:
            return l
        return []