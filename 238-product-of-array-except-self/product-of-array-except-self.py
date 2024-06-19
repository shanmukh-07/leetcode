class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        zeroes_count = nums.count(0)
        product = 1
        for i in nums:
            if i != 0:
                product *= i
        final_list = [0 for _ in range(length)]
        if zeroes_count == 1:
            index = nums.index(0)
            final_list[index] = product
        elif zeroes_count > 1:
            pass
        else:
            for i in range(length):
                final_list[i] = product//nums[i]
        return final_list