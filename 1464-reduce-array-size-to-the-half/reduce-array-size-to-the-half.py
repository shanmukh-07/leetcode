class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        d = {}
        n = len(arr)
        for i in arr:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        l = [i for i in d.values()]
        c = 1
        l.sort()
        sl = 0
        for i in range(len(l)-1,-1,-1):
            sl += l[i]
            if sl < n//2:
                c += 1
            else:
                return c
                break