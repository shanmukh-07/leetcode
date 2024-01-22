class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if s == s[::-1]:
            return s
        for i in range(len(s)-1,0,-1):
            p = s[i:]
            p = p[::-1]
            a = p+s
            if  a==a[::-1]:
                return a