class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                b = i
        nums.remove(b)
        c = (n*(n+1)//2)-sum(nums)
        return b,c