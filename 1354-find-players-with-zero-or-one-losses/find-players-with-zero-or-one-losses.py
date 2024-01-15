class Solution:
    def findWinners(self, m: List[List[int]]) -> List[List[int]]:
        d = {}
        s = set()
        for i in m:
            s.add(i[0])
            s.add(i[1])
            if i[1] not in d:
                d[i[1]] = 1
            else:
                d[i[1]] += 1
        l1,l2 = [],[]
        l = list(s)
        l.sort()
        for i in l:
            c = d.get(i,0)
            if c == 0:
                l1.append(i)
            if c == 1:
                l2.append(i)
        return [l1,l2]