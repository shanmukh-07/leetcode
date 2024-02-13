class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def fun(n):
            return n == n[::-1]
        for i in words:
            if fun(i):
                return i
        return ""
