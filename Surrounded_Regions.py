# Backtracking的做法，从边界向内延伸，如果从边界点出发有一块“O”，这块就是没法转换的，标记为“E”，其他的“O”都能换成“X”
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if board in ([], [[]]):
            return
        m = len(board)
        n = len(board[0])
        def dfs(board, row, col, m, n):
            if board[row][col] != "O":
                return
            board[row][col] = "E"
            if row < m - 1:
                dfs(board, row+1, col, m, n)
            if row > 0:
                dfs(board, row-1, col, m, n)
            if col < n - 1:
                dfs(board, row, col+1, m, n)
            if col > 0:
                dfs(board, row, col-1, m, n)
        
        for i in range(m):
            dfs(board, i, 0, m, n)
            dfs(board, i, n-1, m, n)
        for j in range(1, n-1):
            dfs(board, 0, j, m, n)
            dfs(board, m-1, j, m, n)
            
        for r in range(m):
            for c in range(n):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "E":
                    board[r][c] = "O"
                
            
