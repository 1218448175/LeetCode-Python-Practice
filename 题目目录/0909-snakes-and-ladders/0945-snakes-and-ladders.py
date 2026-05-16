class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        visited = [False] * (n * n + 1)
        visited[1] = True
        q = [1]
        step = 0
        while q:
            tmp = q
            q = []
            for x in tmp:
                if x == n * n:
                    return step
                for y in range(x + 1, min(x + 6, n * n) + 1):
                    r, c = divmod(y - 1, n)
                    if r % 2:
                        c = n - 1 - c
                    nxt = board[-1 - r][c]
                    if nxt < 0:
                        nxt = y
                    if not visited[nxt]:
                        visited[nxt] = True
                        q.append(nxt)
            step += 1
        return -1
        