class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        g = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            g[b].append(a)
        colors = [0] * numCourses
        ans = []
        def dfs(x: int) -> bool:
            colors[x] = 1
            nonlocal ans
            for y in g[x]:
                if colors[y] == 1 or colors[y] == 0 and dfs(y):
                    return True
            colors[x] = 2
            ans.append(x)
            return False
        
        for i, c in enumerate(colors):
            if c == 0 and dfs(i):
                return []
        return ans[::-1]
        