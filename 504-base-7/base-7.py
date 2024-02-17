class Solution:
    def convertToBase7(self, num: int) -> str:
        s = ""
        f = False
        if num == 0:return "0"
        if num < 0:
            f = True
            num = abs(num)
        while num:
            r = num % 7
            s = str(r)+s
            num //= 7
        if f:
            s = '-'+s
        return s