class Solution:
    def getSmallestString(self, s: str) -> str:
        l = list(s)
        if l == sorted(l):
            return s
        for i in range(0,len(l)-1):
            if l[i] > l[i+1]:
                if (int(l[i])%2 == int(l[i+1])%2):
                    l[i],l[i+1] = l[i+1],l[i]
                    break
        return "".join(l)