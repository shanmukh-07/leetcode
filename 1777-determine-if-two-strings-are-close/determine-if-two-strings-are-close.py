class Solution:
    def closeStrings(self, w1: str, w2: str) -> bool:
        def fun(n):
            d = {}
            for i in n:
                if i not in d:
                    d[i] = 1
                else:
                    d[i] += 1
            return d
        if len(w1) != len(w2):
            return 0
        d1 = fun(w1)
        d2 = fun(w2)
        l1 = list(d1.values())
        l2 = list(d2.values())
        l1.sort()
        l2.sort()
        if l1 == l2 and d1.keys() == d2.keys():
            return 1
        return 0