class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        l = []
        for i in range(1,10):
            n = i
            nn = i+1
            while n <= high and nn <= 9:
                n = n*10 + nn
                if n >= low and n <= high:
                    l.append(n)
                nn += 1
        l.sort()
        return l