class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while 1:
            if n%3 == 2 or n//3 == 2:
                return False
            elif n<3:
                break
            n//=3
        if n == 2:
            return False
        return True