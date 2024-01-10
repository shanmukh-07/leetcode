class Solution:
    def twoSum(self, n: List[int], t: int) -> List[int]:
        l = len(n)
        for i in range(l):
            for j in range(i+1,l):
                if n[i]+n[j] == t:
                    return [i,j]