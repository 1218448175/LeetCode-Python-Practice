class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        def binarySearch(l: int, r: int):
            if l > r:
                return False

            mid = (l + r) // 2
            cur = matrix[mid // n][mid % n]
            
            if cur == target:
                return True
            if cur < target:
                return binarySearch(mid + 1, r)
            else:
                return binarySearch(l, mid - 1)
        return binarySearch(0, m * n - 1)
            