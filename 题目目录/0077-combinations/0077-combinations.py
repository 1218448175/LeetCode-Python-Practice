class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        path = []
        def back(num: int) -> None:
            d = k - len(path)
            if d == 0:
                ans.append(path.copy())
                return

            for i in range(num, d - 1, -1):
                path.append(i)
                back(i - 1)
                path.pop()
        
        back(n)
        return ans
        