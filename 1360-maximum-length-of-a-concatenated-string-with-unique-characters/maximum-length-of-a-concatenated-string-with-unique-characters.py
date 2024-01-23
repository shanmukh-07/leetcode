class Solution:
    def maxLength(self, arr: List[str]) -> int:
        m = 0
        for i in range(2**len(arr)):
            s = ""
            for j in range(len(arr)):
                if i&(1<<j):
                    s += arr[j]
            if len(s) == len(set(s)):
                m = max(m,len(s))
        return m