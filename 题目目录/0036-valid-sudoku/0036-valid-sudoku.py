class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9
        m = int(pow(n, 0.5))
        col_set_list = [set() for _ in range(n)]
        row_set_list = [set() for _ in range(n)]
        matric_set_list = [[set() for _ in range(m)] for _ in range(m)]
        ans = True
        for i in range(n):
            for j in range(n):
                num = board[i][j]
                if num == '.':
                    continue
                elif num not in col_set_list[j] and num not in row_set_list[i] and num not in matric_set_list[i // m][j // m]:
                    col_set_list[j].add(num)
                    row_set_list[i].add(num)
                    matric_set_list[i // m][j // m].add(num)
                else:
                    ans = False
                    break
        return ans
        