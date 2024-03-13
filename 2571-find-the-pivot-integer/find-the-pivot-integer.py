class Solution:
    def pivotInteger(self, n: int) -> int:
        s = n*(n+1)//2
        sq = s**(0.5)
        if sq == int(sq):return int(sq)
        else:return -1