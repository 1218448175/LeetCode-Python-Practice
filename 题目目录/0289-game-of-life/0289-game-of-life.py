class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        neighbors = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]

        for i in range(m):
            for j in range(n):
                live_count = 0
                for x_d, y_d in neighbors:
                    neighbor_x = i + x_d
                    neighbor_y = j + y_d
                    if 0 <= neighbor_x < m and 0 <= neighbor_y < n:
                        neighbor = board[neighbor_x][neighbor_y]
                        if neighbor == 1 or neighbor == 2:
                            live_count += 1
                if (live_count < 2 or live_count > 3) and board[i][j] == 1:
                    board[i][j] = 2
                    continue
                if live_count == 3 and board[i][j] == 0:
                    board[i][j] = -1
                    continue

        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 0
                    continue
                if board[i][j] == -1:
                    board[i][j] = 1
                    continue
        