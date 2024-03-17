class Solution:
    def insert(self, l1: List[List[int]], l2: List[int]) -> List[List[int]]:
        if not l1:
            return [l2]
        i,j = 0,len(l1)-1
        while i<=j:
            m = (i+j)//2
            if l1[m][0]<l2[0]:
                i = m + 1
            else:
                j = m - 1
        l1.insert(i,l2)
        res = [l1[0]]
        for i in range(1,len(l1)):
            pi = res[-1]
            ci = l1[i]
            if pi[1] >= ci[0]:
                res[-1] = [pi[0],max(pi[1],ci[1])]
            else:
                res.append(ci)
        return res