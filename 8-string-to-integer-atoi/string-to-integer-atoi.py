class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        sgn = 1
        res = 0
        i = 0
        if i<len(s) and (s[i] == '-' or s[i] == "+"):
            if s[i] == '-':
                sgn = -1
            i += 1
        while i < len(s) and s[i].isdigit():
            res = res*10 + int(s[i])
            i += 1
        res *= sgn
        if res < -2**31:
            return -2**31
        if res > 2**31 - 1:
            return 2**31 - 1
        return res