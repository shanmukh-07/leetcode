class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        rl = [min(i) for i in matrix]
        l = list(zip(*matrix))
        e = float("inf")
        for i in l:
            if max(i) in rl:
                e = max(i)
        if e == float("inf"):
            return []
        return [e]