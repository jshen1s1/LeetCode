class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or len(matrix) < 1:
            return 0

        m = len(matrix)
        n = len(matrix[0])
        dp = [[0]*(n+1) for _ in range(m+1)]
        max_size = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    dp[i+1][j+1] = min(dp[i][j], dp[i][j+1], dp[i+1][j]) + 1
                    max_size = max(max_size, dp[i+1][j+1])

        return max_size**2