class Solution:
    def dfs(self, board, r, c):
        board[r][c] = "I"
        nr, nc = len(board), len(board[0])
        for x, y in [(r, c + 1), (r, c - 1), (r - 1, c), (r + 1, c)]:
            if 0 <= x < nr and 0 <= y < nc and board[x][y] == "O":
                self.dfs(board, x, y)
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        nr = len(board)
        if nr == 0:
            return
        nc = len(board[0])
        for r in range(nr):
            for c in range(nc):
                if (r == 0 or c == 0 or r == nr - 1 or c == nc - 1) and board[r][c] == "O":
                    self.dfs(board, r, c)
        
        for r in range(nr):
            for c in range(nc):
                if board[r][c] == "O": board[r][c] = "X"
                elif board[r][c] == "I": board[r][c] = "O"
        