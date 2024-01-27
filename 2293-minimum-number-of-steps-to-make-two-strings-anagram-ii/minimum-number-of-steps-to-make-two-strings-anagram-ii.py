class Solution:
    def minSteps(self, s: str, t: str) -> int:
        d1 = {}
        d2 = {}
        strg = "abcdefghijklmnopqrstuvwxyz"
        c = 0
        for i in strg:
            d1[i] = s.count(i)
            d2[i] = t.count(i)
            c += abs(d1[i]-d2[i])
        return c