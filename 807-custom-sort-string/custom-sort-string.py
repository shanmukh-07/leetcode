class Solution:
    def customSortString(self, order: str, s: str) -> str:
        ds = s
        s = list(s)
        fs = ""
        for i in range(len(order)):
            if order[i] in s:
                c = s.count(order[i])
                for j in range(c):
                    fs += order[i]
                    s.remove(order[i])
        for i in s:
            fs += str(i)
        return fs