class Solution:
    def maxTurbulenceSize(self, A):
        
        @lru_cache(None)
        def dp(i, dr):
            if i == 0 or (A[i] - A[i-1])*dr >= 0: return 1
            return dp(i-1, -dr) + 1
        
        return max(dp(i, dr) for i in range(len(A)) for dr in [-1, 1])
