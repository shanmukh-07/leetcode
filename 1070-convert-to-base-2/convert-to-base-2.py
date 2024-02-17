class Solution:
    def baseNeg2(self, n: int) -> str:
        s = ""
        if n == 0:return "0"
        while n:
            r = n % -2
            n //= -2
            if r < 0:
                r += 2
                n += 1
            s = str(r) + s
        return s