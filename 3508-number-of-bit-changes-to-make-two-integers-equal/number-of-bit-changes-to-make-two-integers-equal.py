class Solution:
    def minChanges(self, n: int, k: int) -> int:
        n1 = bin(n)[2:]
        n2 = bin(k)[2:]
        l = max(len(n1),len(n2))
        n1 = "0"*(l-len(n1)) + n1
        n2 = "0"*(l-len(n2)) + n2
        c = 0
        for i in range(l):
            if n1[i] == '0' and n2[i] == '1':
                return -1
            elif n1[i] != n2[i]:
                c += 1
        return c