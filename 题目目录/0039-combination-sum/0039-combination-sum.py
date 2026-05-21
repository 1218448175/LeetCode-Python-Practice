class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        def backtrack(index: int) -> None:
            for i in range(index, n):
                path.append(candidates[i])
                total = sum(path)
                if total == target:
                    ans.append(path.copy())
                    path.pop()
                    return
                elif total < target:
                    backtrack(i)
                    path.pop()
                else:
                    path.pop()
                    return
        ans = []
        path = []
        n = len(candidates)
        backtrack(0)
        return ans
        