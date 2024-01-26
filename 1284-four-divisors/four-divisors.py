class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def fun(n):
            c = 0
            s = 0
            for i in range(1,int(n**0.5)+1):
                if n%i == 0:
                    c += 1
                    s += i
                    if n//i != i:
                        c+=1
                        s += n//i
                if c>4:
                    break
            if c == 4:
                return s
            return 0
        s = 0
        for i in nums:
            s += fun(i)
        return s