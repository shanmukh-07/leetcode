class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st = set()
        l = 0
        m = 0
        for i in range(len(s)):
            while s[i] in st:
                st.remove(s[l])
                l += 1
            st.add(s[i])
            m = max(m,i-l+1)
        return m