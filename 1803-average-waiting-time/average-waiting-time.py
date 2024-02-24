class Solution:
    def averageWaitingTime(self, cst: List[List[int]]) -> float:
        l = len(cst)
        # fl = []
        p = cst[0][1]
        t = cst[0][1]+cst[0][0]
        # fl.append(p)
        s = p
        for i in range(1,l):
            if t < cst[i][0]:
                t = cst[i][0]+cst[i][1]
            else:
                t += cst[i][1]
            p = t-cst[i][0]
            # fl.append(p)
            s += p
        # print(fl)
        return s/l