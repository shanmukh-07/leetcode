class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        ps = {0:-1}
        res = 0
        s = 0
        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
                s += -1
            else:
                s += 1
            if s in ps:
                res = max(res,i-ps[s])
            else:
                ps[s] = i
        print(ps)
        return res