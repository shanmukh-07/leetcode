class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        p,n = [],[]
        for i in nums:
            if i<0:
                n.append(i)
            else:
                p.append(i)
        l = []
        f = True
        while 1:
            if not n and not p:
                return l
            if f:
                l.append(p[0])
                p.pop(0)
            else:
                l.append(n[0])
                n.pop(0)
            f = not f