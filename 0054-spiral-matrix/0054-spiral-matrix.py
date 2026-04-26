class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        direcitons = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        i = 0
        j = 0
        m = len(matrix)
        n = len(matrix[0])
        num = m * n
        res_list = []
        d = 0
        direct = direcitons[d]
        l = 0
        while l < num:
            if 0 <= i < m and 0 <= j < n and matrix[i][j] != 101:
                res_list.append(matrix[i][j])
                matrix[i][j] = 101
                l += 1
            else:
                i -= direct[0]
                j -= direct[1]
                d = (d+1) % 4
                direct = direcitons[d]
            i += direct[0]
            j += direct[1]

        return res_list


        