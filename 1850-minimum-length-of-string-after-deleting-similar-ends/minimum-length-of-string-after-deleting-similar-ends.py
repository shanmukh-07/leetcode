class Solution:
    def minimumLength(self, s: str) -> int:
        i = 0
        j = len(s)-1
        while i<=j:
            if i == j and s[i] == s[j]:
                return 1
            if s[i] != s[j]:
                return j-i+1
            a,b = i,j
            while a<j and s[a] == s[i]:
                a += 1
            i = a
            while b>=0 and s[b] == s[j]:
                b -= 1
            j = b
        return 0