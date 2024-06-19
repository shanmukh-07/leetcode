class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000
        }
        l = [d[i] for i in s]
        l1 = []
        ln = len(l)-2
        l1.append(l[-1])
        while ln>=0:
            if l1[-1]>l[ln]:
                b = l1[-1]
                l1.pop()
                l1.append(b-l[ln])
            else:
                l1.append(l[ln])
            ln -= 1
        return sum(l1)