class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        r = 0
        if x>=0:
            r = int(s[::-1])
        else:
            s = s[1:]
            ss = '-'+s[::-1]
            r = int(ss)
        if r<(-2**31) or r>(2**31-1):
            return 0
        return r