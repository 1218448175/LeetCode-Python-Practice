class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        for i in range(1, numRows):
            r = [1]
            for j in range(1, i):
                r.append(ans[-1][j - 1] + ans[-1][j])
            r.append(1)
            ans.append(r)
        return ans
        