class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        cnt = 0

        def dfs(grid, i, j):
            if i<0 or j<0 or i>=m or j>=n or grid[i][j] != "1":
                return
            grid[i][j] = "#"
            dfs(grid, i-1, j)
            dfs(grid, i, j-1)
            dfs(grid, i+1, j)
            dfs(grid, i, j+1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    dfs(grid, i, j)
                    cnt += 1

        return cnt