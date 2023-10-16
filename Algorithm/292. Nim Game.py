class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0


        '''
        # dp approach
        dp = [True] * n
        for i in range(3, n):
            dp[i] = not dp[i - 1] or not dp[i - 2] or not dp[i - 3]
        return dp[n-1]
        '''