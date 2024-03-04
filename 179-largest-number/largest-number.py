class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        l = []
        for i in nums:
            l.append((str(i)*10,i))
        l.sort(reverse = True)
        s = ""
        for i,j in l:
            s += str(j)
        s = int(s)
        return str(s)