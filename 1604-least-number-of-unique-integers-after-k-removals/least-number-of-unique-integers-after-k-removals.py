class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        d = {}
        for i in arr:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        l = [i for i in d.values()]
        l.sort()
        s = 0
        c = 0
        for i in l:
            s += i
            c += 1
            if s > k:
                c -= 1
                break
        print(l,s,c)
        return len(l[c:])