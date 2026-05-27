## [772. 建立四叉树](https://leetcode.cn/problems/construct-quad-tree/)

### 中等

给你一个 `n * n` 矩阵 `grid`，其中 `n` 是 2 的幂，表示一个 `n * n` 区域。每个单元格的值为 `0` 或 `1`。 请你构建并返回表示该矩阵的 **四叉树**。

四叉树是一种树形数据结构，每个内部节点恰好有四个子节点。每个节点有两个属性：

- `isLeaf`：若节点为叶子则为 `True`，否则为 `False`。
- `val`：节点存储的值。叶子节点为 `0` 或 `1`；非叶子节点为 `True`（题目约定，无实际意义）。

**示例 1：**

```
输入：grid = [[0,1],[1,0]]
输出：[[0,1],[1,0],[1,1],[1,1],[1,0]]
解释：四个子区域值不全相同，无法合并为单叶子，故为内部节点。
```

**示例 2：**

```
输入：grid = [[1,1],[1,1]]
输出：[[1,1]]
解释：四个子区域均为 1，合并为一个叶子节点。
```

---

## 题解：四叉分治 + 自底向上合并

### 1. 核心思路：按象限递归，再尝试压缩

将 `n × n` 矩阵视为四叉树的根区域，用 DFS `(r, c, length)` 表示当前子方阵左上角与边长：

1. **递归基准**：`length == 1` 时，直接返回叶子 `Node(val, isLeaf=True)`。
2. **四叉切分**：边长减半 `nxt = length // 2`，分别递归 **左上、右上、左下、右下** 四个象限。
3. **合并优化**：若四个子节点 **均为叶子** 且 **值相同**，则不必保留四个子节点，压缩为一个叶子。
4. **否则**：返回内部节点，四个指针分别挂接四个子树。

这与 [148. 排序链表](../0148-sort-list) 同属 **分治**：先拆成四个规模更小的子问题，再在合并阶段决定能否向上压缩。

---

### 2. 执行逻辑拆解

#### A. 四象限坐标划分

```python
nxt = length // 2
tl = dfs(r, c, nxt)           # 左上
tr = dfs(r, c + nxt, nxt)     # 右上
bl = dfs(r + nxt, c, nxt)     # 左下
br = dfs(r + nxt, c + nxt, nxt)  # 右下
```

- 行坐标 `r`、列坐标 `c` 始终指向当前子方阵左上角。
- 边长每次减半，保证 `n` 为 2 的幂时递归能自然终止。

#### B. 合并条件

```python
if (tl.isLeaf and tr.isLeaf and bl.isLeaf and br.isLeaf and
    tl.val == tr.val == bl.val == br.val):
    return Node(tl.val, True, None, None, None, None)
return Node(True, False, tl, tr, bl, br)
```

- 只有 **四个子节点都是叶子且同值** 才能合并；任一子树仍是内部节点则必须保留结构。
- 非叶子节点的 `val` 按题目要求设为 `True`，实际含义由子树决定。

---

### 3. 算法可视化

以 `grid = [[1,1],[1,1]]` 为例：

1. 根区域 `length=2`，拆为四个 `1×1` 叶子，值均为 `1`。
2. 合并阶段发现四叶子同值 → 压缩为单个叶子 `Node(1, True, ...)`。
3. 最终四叉树仅一个节点。

以 `grid = [[0,1],[1,0]]` 为例：

1. 四个 `1×1` 叶子值分别为 `0,1,1,0`，不全相同。
2. 无法合并，返回内部节点，四子指针分别指向四个叶子。

---

### 4. 复杂度分析

- **时间复杂度**：$O(n^2 \log n)$。最坏情况下（如棋盘格交替）几乎无法合并，递归深度 $O(\log n)$，每层处理 $O(n^2)$ 规模区域；若合并充分则实际访问节点更少。
- **空间复杂度**：$O(\log n)$ 递归栈深度；结果树节点数最坏 $O(n^2)$，由题目输出结构决定。

---

### 5. 代码实现回顾

```python
class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)

        def dfs(r: int, c: int, length: int) -> 'Node':
            if length == 1:
                return Node(grid[r][c] == 1, True, None, None, None, None)

            nxt = length // 2
            tl = dfs(r, c, nxt)
            tr = dfs(r, c + nxt, nxt)
            bl = dfs(r + nxt, c, nxt)
            br = dfs(r + nxt, c + nxt, nxt)

            if (tl.isLeaf and tr.isLeaf and bl.isLeaf and br.isLeaf and
                tl.val == tr.val == bl.val == br.val):
                return Node(tl.val, True, None, None, None, None)

            return Node(True, False, tl, tr, bl, br)

        return dfs(0, 0, n)
```

与 [108. 将有序数组转换为二叉搜索树](../0108-convert-sorted-array-to-binary-search-tree) 类似：通过 **均匀切分区间** 构造树形结构，区别在四叉树每步拆成四个子区域并在合并时做 **同值叶子压缩**。
