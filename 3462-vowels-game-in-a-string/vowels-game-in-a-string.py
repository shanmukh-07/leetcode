class Solution:
    def doesAliceWin(self, s: str) -> bool:
        l = []
        for i in range(len(s)):
            if s[i] in 'aeiou':
                l.append(1)
            else:
                l.append(0)
        if l.count(1) == 0:
            return False
        return True