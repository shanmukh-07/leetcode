class Solution:
    def concatenatedBinary(self, n: int) -> int:
        s = ""
        for i in range(1,n+1):
            i = bin(i)[2:]
            s += i
        return int(s,2)%(10**9+7)