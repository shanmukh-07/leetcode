class Solution:
    def maxOperations(self, s: str) -> int:
        r,c = 0,0
        for i in range(len(s)-2,-1,-1):
            if s[i] == '1' and s[i+1] == '0':
                c += 1
            if s[i] == '1':
                r += c
        return r