class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ans = False
        m = len(board)
        n = len(board[0])
        def backtrack(r: int, c: int, index: int) -> None:
            nonlocal ans
            if index == len(word) - 1:
                ans = True
                return
            for x_d, y_d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                x, y = r + x_d, c + y_d
                if 0 <= x < m and 0 <= y < n and board[x][y] != '#':
                    char = board[x][y]
                    if char == word[index + 1]:
                        board[x][y] = '#'
                        backtrack(x, y, index + 1)
                        board[x][y] = char
            return
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    char = board[i][j]
                    board[i][j] = '#'
                    backtrack(i, j, 0)
                    board[i][j] = char
        return ans
        