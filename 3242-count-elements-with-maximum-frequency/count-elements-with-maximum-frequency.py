class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        l = [i for i in d.values()]
        m = max(l)
        a = l.count(m)
        return a*m