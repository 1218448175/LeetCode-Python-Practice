## [399. 除法求值](https://leetcode.cn/problems/evaluate-division/)

### 中等

给你一个变量对数组 `equations` 和一个实数值数组 `values` 作为已知条件，其中 `equations[i] = [Ai, Bi]`，`values[i]` 表示方程 `Ai / Bi = values[i]`。每个 `Ai` 或 `Bi` 是一个表示单个变量的字符串。

另有一些以数组 `queries` 表示的问题，其中 `queries[j] = [Cj, Dj]` 表示第 `j` 个问题，请你根据已知条件找出 `Cj / Dj = ?` 作为答案。

返回 **所有问题的答案**。如果存在某个无法确定的答案，则用 `-1.0` 替代这个答案。

**示例 1：**

<pre><strong>输入：</strong>equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
<strong>输出：</strong>[6.00000,0.50000,-1.00000,1.00000,-1.00000]
<strong>解释：</strong>
条件：a / b = 2.0, b / c = 3.0
问题：a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
结果：[6.0, 0.5, -1.0, 1.0, -1.0 ]
</pre>

**示例 2：**

<pre><strong>输入：</strong>equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
<strong>输出：</strong>[3.75000,0.40000,5.00000,0.20000]
</pre>

**提示：**

- `1 <= equations.length <= 20`
- `equations[i].length == 2`
- `1 <= values.length <= 20`
- `values.length == equations.length`
- `1.0 <= values[i] <= 20.0`
- `values[i]` 是一个浮点数
- `1 <= queries.length <= 20`
- `queries[i].length == 2`
- `Ai, Bi, Ci, Di` 由小写英文字母组成

---

## 题解：带权并查集（Weighted Union-Find）

### 1. 核心思路：把除法关系建模为连通分量

这道题的本质是：若已知 `a / b = k`，则变量 `a` 与 `b` 属于同一个**连通分量**，且它们之间存在确定的倍数关系。查询 `c / d` 等价于判断 `c` 与 `d` 是否连通；若连通，则答案可由两者到公共根节点的权重推导。

你的代码采用 **带权并查集**，为每个变量维护一个到其代表元的权重 `mul[x]`，表示 `root(x) / x`。这样同一集合内任意两点的商，都可以转化为它们各自到根的权重之比。

---

### 2. 执行逻辑的详细拆解

#### A. 变量映射与初始化

```python
variable_to_id = {}
for equation in equations:
    for s in equation:
        if s not in variable_to_id:
            variable_to_id[s] = len(variable_to_id)
uf = UnionFind(len(variable_to_id))
```

- 将所有出现过的变量字符串映射为整数编号，便于并查集操作。
- `UnionFind` 初始化时，`fa[i] = i`，`mul[i] = 1.0`，表示每个变量初始自成一组，且 `root / x = 1`。

#### B. 合并方程：建立带权关系

```python
for (a, b), value in zip(equations, values):
    uf.merge(variable_to_id[b], variable_to_id[a], value)
```

- 方程 `a / b = value` 意味着 `b / a = 1 / value`，合并时以 `b` 为子节点、`a` 为父节点方向建立权重。
- `merge(from_, to, value)` 在路径压缩后，将 `from_` 所在集合挂到 `to` 的根上，并更新 `mul[x]`，使得合并后所有节点的相对关系仍满足已知方程。

#### C. 路径压缩与权重传递

```python
def find(self, x: int) -> int:
    if fa[x] != x:
        root = self.find(fa[x])
        self.mul[x] *= self.mul[fa[x]]
        fa[x] = root
    return fa[x]
```

- 标准路径压缩的同时，将父节点的权重累乘到当前节点，使 `mul[x]` 始终表示 `root / x`。
- 这是带权并查集的关键：压缩路径时不能丢失倍数关系。

#### D. 查询答案

```python
if c != -1 and d != -1 and uf.same(c, d):
    ans.append(uf.mul[d] / uf.mul[c])
else:
    ans.append(-1.0)
```

- 若 `c` 或 `d` 未出现过，或两者不在同一集合，返回 `-1.0`。
- 若连通，利用 `c / d = (root/c) / (root/d) = mul[d] / mul[c]` 直接计算。

---

### 3. 算法可视化

已知：`a / b = 2.0`，`b / c = 3.0`

1. **合并 a、b**：`a` 与 `b` 进入同一集合，权重记录 `root / a` 与 `root / b` 的关系。
2. **合并 b、c**：`b` 与 `c` 连通，传递得 `a / c = (a/b) × (b/c) = 6.0`。
3. **查询 a、c**：`same(a, c)` 为真，用 `mul[c] / mul[a]` 得 `6.0`。
4. **查询 a、e**：`e` 未出现或不在同一集合，返回 `-1.0`。

---

### 4. 复杂度分析

- **时间复杂度**：$O((E + Q) \cdot \alpha(N))$。其中 $E$ 为方程数，$Q$ 为查询数，$N$ 为变量数，$\alpha$ 为反阿克曼函数，近似常数。
- **空间复杂度**：$O(N)$。并查集数组与变量映射表的空间。

---

### 5. 代码回顾

```python
class UnionFind:
    def __init__(self, n: int):
        self.fa = list(range(n))
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
```
