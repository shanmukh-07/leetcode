class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        l1,l2 = len(rowSum),len(colSum)
        mat = [[0]*l2 for _ in range(l1)]
        i,j = l1-1,l2-1
        while i >= 0 and j >= 0:
            if rowSum[i] <= colSum[j]:
                mat[i][j] = rowSum[i]
                colSum[j] -= rowSum[i]
                i -= 1
            else:
                mat[i][j] = colSum[j]
                rowSum[i] -= colSum[j]
                j -= 1
        return mat