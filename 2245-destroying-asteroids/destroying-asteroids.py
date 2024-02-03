class Solution:
    def asteroidsDestroyed(self, m: int, a: List[int]) -> bool:
        a.sort()
        for i in range(len(a)):
            if a[i] > m:
                return False
            else: 
                m += a[i]
                print(m)
        return True