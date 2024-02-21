class Solution:
    def rangeBitwiseAnd(self, l: int, r: int) -> int:
        while l<r:
            r = r&(r-1)
        return l&r