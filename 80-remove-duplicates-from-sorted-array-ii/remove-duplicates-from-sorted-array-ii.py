class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = []
        for i in nums:
            if i not in l:
                if nums.count(i) == 1:
                    l.append(i)
                elif nums.count(i) >= 2:
                    l.append(i)
                    l.append(i)
        for i in range(len(l)):
            nums[i] = l[i]
        return len(l)