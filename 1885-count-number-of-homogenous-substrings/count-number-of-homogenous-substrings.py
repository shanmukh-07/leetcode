class Solution:
    def countHomogenous(self, s: str) -> int:
        m = 10**9+7
        l = []
        c = 0
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                c += 1
            else:
                l.append(c+1)
                c = 0
        l.append(c+1)
        s = 0
        for i in l:
            s += (i*(i+1))//2
        return s%m