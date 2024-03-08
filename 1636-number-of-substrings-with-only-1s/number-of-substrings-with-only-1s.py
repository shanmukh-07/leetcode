class Solution:
    def numSub(self, s: str) -> int:
        m = 10**9 + 7
        l = len(s)
        sm = 0
        c = 0
        for i in range(l):
            if s[i] == '1':
                c += 1
            else:
                sm += (c*(c+1))//2
                c = 0
        if c > 0:
            sm += (c*(c+1))//2
        return sm%m