class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix) // 2
        max_idx = len(matrix) - 1
        for i in range(n):
            for j in range(n):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[max_idx - j][i]
                matrix[max_idx - j][i] = matrix[max_idx - i][max_idx - j]
                matrix[max_idx - i][max_idx - j] = matrix[j][max_idx - i]
                matrix[j][max_idx - i] = tmp

        if len(matrix) % 2 == 1:
            j = n
            for i in range(n):
                    tmp = matrix[i][j]
                    matrix[i][j] = matrix[max_idx - j][i]
                    matrix[max_idx - j][i] = matrix[max_idx - i][max_idx - j]
                    matrix[max_idx - i][max_idx - j] = matrix[j][max_idx - i]
                    matrix[j][max_idx - i] = tmp

                

        