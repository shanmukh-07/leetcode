class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s1 = s[:len(s)//2]
        s2 = s[len(s)//2:]
        c1,c2 = 0,0
        for i in s1:
            if i in 'AEIOUaeiou':
                c1 += 1
        for j in s2:
            if j in 'AEIOUaeiou':
                c2 += 1
        return c1 == c2