class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        d = {i+1:[] for i in range(n)}
        for i in trust:
            d[i[0]].append(i[1])
        c = -1
        ll = []
        for i,j in d.items():
            if len(j) == 0:
                c = i
            else:
                ll.append((i,j))
        tc = 0
        if c != -1:
            for i,j in ll:
                if c in j:
                    tc += 1
        if tc != n-1:
            c = -1
        return c