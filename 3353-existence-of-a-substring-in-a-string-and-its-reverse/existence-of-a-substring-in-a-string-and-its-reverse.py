class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        for i in  range(len(s)-1):
            if (s[i] + s[i+1])[::-1] in s:
                return True
        return False