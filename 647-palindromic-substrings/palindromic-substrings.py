class Solution:
    def countSubstrings(self, s: str) -> int:
        c = 0
        for i in range(len(s)):
            for j in range(i,len(s)):
                a = s[i:j+1]
                if a == a[::-1]:
                    c += 1
        return c
        