class UnionFind:
    def __init__(self, n: int):
        self.fa = list(range(n))    # 代表元
        self.mul = [1.0] * n
    
    def find(self, x: int) -> int:
        fa = self.fa
        if fa[x] != x:
            root = self.find(fa[x])
            self.mul[x] *= self.mul[fa[x]]
            fa[x] = root
        return fa[x]

    def same(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def merge(self, from_: int, to: int, value: float) -> None:
        x, y = self.find(from_), self.find(to)
        if x == y:
            return
        
        self.mul[x] = self.mul[to] * value / self.mul[from_]
        self.fa[x] = y

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        variable_to_id = {}
        for equation in equations:
            for s in equation:
                if s not in variable_to_id:
                    variable_to_id[s] = len(variable_to_id)
        uf = UnionFind(len(variable_to_id))
        for (a, b), value in zip(equations, values):
            uf.merge(variable_to_id[b], variable_to_id[a], value)
        
        ans = []
        for c, d in queries:
            c = variable_to_id.get(c, -1)
            d = variable_to_id.get(d, -1)
            if c != -1 and d != -1 and uf.same(c, d):
                ans.append(uf.mul[d] / uf.mul[c])
            else:
                ans.append(-1.0)
        return ans
        