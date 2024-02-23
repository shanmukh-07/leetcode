class Solution:
    def trap(self, h: List[int]) -> int:
        l = len(h)
        mp,ms = 0,0
        p,s = [],[]
        for i in range(l):
            mp = max(mp,h[i])
            p.append(mp)
        for j in range(l-1,-1,-1):
            ms = max(ms,h[j])
            s.append(ms)
        s = s[::-1]
        fs = 0
        for i in range(l):
            fs += min(p[i]-h[i],s[i]-h[i])
        return fs