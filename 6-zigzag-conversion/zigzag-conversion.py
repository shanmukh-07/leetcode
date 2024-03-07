class Solution:
    def convert(self, s: str, n: int) -> str:
        l = len(s)
        if n == 1:
            return "".join(s)
        s = list(s)
        lst = []
        t = 1
        f = True
        while 1:
            if len(lst) == l:
                break
            if f:
                if t<=n:
                    lst.append(t)
                    t += 1
                else:
                    t -= 2
                    f = not f
            if not f:
                if t>=1:
                    lst.append(t)
                    t-=1
                else:
                    t += 2
                    f = not f
        fl = []
        ft = 1
        while ft <= n:
            tl = []
            for i in range(l):
                if lst[i] == ft:
                    tl.append(s[i])
            fl += tl
            ft += 1
        return "".join(fl)
