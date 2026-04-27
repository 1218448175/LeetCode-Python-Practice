class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)
        T = 2 * numRows - 2
        if T == 0:
            return s
        matrix = [[] for _ in range(numRows)]
        for i in range(n):
            loc = i % T
            if loc < numRows:
                matrix[loc].append(s[i])
            else:
                matrix[numRows - loc - 2].append(s[i])
        ans = ""
        for sub_str in matrix:
            ans = ans + "".join(sub_str)
        return ans