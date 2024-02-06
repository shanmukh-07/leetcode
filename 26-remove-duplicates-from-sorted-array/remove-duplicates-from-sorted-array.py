class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        t = nums
        l = []
        for i in t:
            if i not in l:
                l.append(i)
        for i in range(len(l)):
            nums[i] = l[i]
        print(nums)
        return len(l)