class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        else:
            s1, s2 = set(word1), set(word2)
            if s1 == s2:
                o1, o2 = [], []
                for e in s1:
                    o1.append(word1.count(e))
                for e in s2:
                    o2.append(word2.count(e))
                o1.sort()
                o2.sort()
                return o1 == o2
            return False