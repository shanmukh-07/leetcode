class Solution:
    def minSteps(self, s: str, t: str) -> int:
        ds,dt = {},{}
        for i in s:
            if i not in ds:
                ds[i] = 1
            else:
                ds[i] += 1
        for i in t:
            if i not in dt:
                dt[i] = 1
            else:
                dt[i] += 1
        if ds == dt:
            return 0
        else:
            c = 0
            for i,j in dt.items():
                if i in ds:
                    ds[i]-=j
            for i in ds.values():
                if i>0:
                    c+=i
            return c