class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        d = {i+1:[] for i in range(n)}
        for i in trust:
            d[i[0]].append(i[1])   
        c = -1
        l = []
        for i,j in d.items():
            if len(j) == 0:
                c = i
            else:
                l.append((i,j))
        dd = 0
        if c != -1:
            for i,j in l:
                if c in j:
                    dd += 1
        if dd != n-1:
            c = -1
        return c