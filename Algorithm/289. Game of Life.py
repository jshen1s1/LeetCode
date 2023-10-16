import itertools
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])

        def count_neighbors(row, col):
            count = 0
            for (i, j) in itertools.product([-1, 0, 1], repeat=2):
                if (i, j) == (0, 0):
                    continue
                if 0 <= row + i < m and 0 <= col + j < n:                    
                    if abs(board[row+i][col+j]) == 1:
                        count += 1

            return count

        for i in range(m):
            for j in range(n):
                lives = count_neighbors(i, j)
                if board[i][j] == 1 and lives not in (2, 3):
                    board[i][j] = -1
                elif board[i][j] == 0 and lives == 3:
                    board[i][j] = 2


        for i in range(m):
            for j in range(n):
                if board[i][j] > 0:
                    board[i][j] = 1
                else:
                    board[i][j] = 0