class Solution:
    def maxDifference(self, s: str) -> int:
        d = {}
        for i in s:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        l = list(d.values())
        o = 0
        e = float("inf")
        for i in l:
            if i%2 == 0:
                e = min(e,i)
            else:
                o = max(o,i)
        return o-e