class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        def fun(i,arr,k,n,dp):
            if i==n:
                return 0
            m = float("-inf")
            ans = float("-inf")
            l = 0
            if dp[i] != -1:
                return dp[i]
            for j in range(i,min(n,i+k)):
                l += 1
                m = max(m,arr[j])
                s = l*m + fun(j+1,arr,k,n,dp)
                ans = max(ans,s)
            dp[i] = ans
            return ans

        n = len(arr)
        dp = [-1]*n
        return fun(0,arr,k,n,dp)