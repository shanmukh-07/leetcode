class Solution:
    def bagOfTokensScore(self, tokens: List[int], p: int) -> int:
        l = len(tokens)
        mc,c = 0,0
        tokens.sort()
        i = 0
        j = l-1
        while i<=j:
            if p>=tokens[i]:
                c += 1
                mc = max(mc,c)
                p -= tokens[i]
                i += 1
            elif c >= 1:
                c -= 1
                p += tokens[j]
                j -= 1
            else:
                return mc
        return mc