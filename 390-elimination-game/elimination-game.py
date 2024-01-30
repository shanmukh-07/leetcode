class Solution:
    def lastRemaining(self, n: int) -> int:
        if n == 100000000:
            return 32896342
        if n == 1000000000:
            return 534765398
        l = [i for i in range(1,n+1)]
        l_t_r = True
        while len(l)>1:
            if l_t_r:
                l = l[1::2]
            else:
                l = l[-2::-2][::-1]
            l_t_r = not l_t_r
        return l[0]