class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        z = 0
        p = 1
        k = -1
        for i in range(n):
            if nums[i] == 0:
                z += 1
                k = i
            else:
                p *= nums[i]
        if z>1:
            l = [0 for i in range(n)]
            return l
        elif z == 1:
            l = [0 for i in range(n)]
            l[k] = p
            return l
        else:
            l = []
            for i in range(n):
                l.append(p//nums[i])
            return l