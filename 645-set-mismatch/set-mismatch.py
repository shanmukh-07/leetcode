class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:

        i = 1
        while 1:
            if i not in nums:
                c = i
                break
            i += 1
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
            if d[i] == 2:
                b = i
                break
        return b,c