class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def fun(arr,l,h,t):
            if l>h:return -1
            m = (l+h)//2
            if arr[m] == t:
                return m
            elif t>arr[m]:
                return fun(arr,m+1,h,t)
            else:
                return fun(arr,l,m-1,t)
        l = 0
        r = len(nums)-1
        return fun(nums,l,r,target)