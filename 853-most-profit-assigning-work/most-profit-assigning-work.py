class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        ln = len(profit)
        l = []
        for i in range(ln):
            l.append((profit[i],difficulty[i]))
        l.sort(reverse = True)
        worker.sort(reverse = True)
        ind,j = 0,0
        s = 0
        while ind<len(worker) and j<ln:
            if worker[ind] < l[j][1]:
                j += 1
            else:
                s += l[j][0]
                ind += 1
        return s