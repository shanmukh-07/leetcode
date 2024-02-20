class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        i = 1
        n = len(score)
        l = []
        while i!=n+1:
            if i == 1:
                l.append("Gold Medal")
            elif i == 2:
                l.append("Silver Medal")
            elif i == 3:
                l.append("Bronze Medal")
            else:
                l.append(str(i))
            i += 1
        dl = score.copy()
        dl.sort(reverse = True)
        d = {}
        for i in range(n):
            d[dl[i]] = l[i]
        pl = []
        for i in score:
            pl.append(d[i])
        return pl