class Solution:
    def minSteps(self, s: str, t: str) -> int:
        l1,l2 = [0]*26,[0]*26
        for i in s:
            l1[ord(i)-97] += 1
        for i in t:
            l2[ord(i)-97] += 1  
        s = 0
        for i in range(26):
            s+=(abs(l1[i]-l2[i]))
        return s