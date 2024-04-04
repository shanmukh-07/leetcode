class Solution:
    def maxDepth(self, s: str) -> int:
        c,m = 0,0
        for i in s:
            if i == '(':
                c += 1
            if i == ')':
                c -= 1
            m = max(m,c)
        return m