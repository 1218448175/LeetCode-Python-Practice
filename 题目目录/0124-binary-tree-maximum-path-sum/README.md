## [124. 二叉树中的最大路径和](https://leetcode.cn/problems/binary-tree-maximum-path-sum/)

### 困难

二叉树中的 **路径** 被定义为一条节点序列，序列中相邻节点之间存在一条父子边；同一个节点在路径中最多出现一次；路径 **不必** 经过根节点，也 **不必** 到达叶节点。

路径和是路径上各节点值之和。

给你一个二叉树的根节点 `root` ，返回其 **最大路径和** 。

**示例 1：**

<img alt="" src="https://assets.leetcode.com/uploads/2020/10/13/exx1.jpg" style="width: 322px; height: 182px;">

<pre><strong>输入：</strong>root = [1,2,3]
<strong>输出：</strong>6
<strong>解释：</strong>最优路径是 2 → 1 → 3，路径和为 2 + 1 + 3 = 6。
</pre>

**示例 2：**

<pre><strong>输入：</strong>root = [-10,9,20,null,null,15,7]
<strong>输出：</strong>42
<strong>解释：</strong>最优路径是 15 → 20 → 7，和为 42。
</pre>

---

## 题解：后序 DFS ——「子树全局最优」与「可接父边的单链」

### 1. 核心思路：在每个节点合并「拐弯」与「向上延伸」

最大路径和若经过当前节点 `root`，只有两类形状：

1. **只向一侧延伸再折回**：从左子树某处沿单链上到 `root` 再沿单链下到右子树某处（可退化为只走左或只走右），即「以 `root` 为最高点的弧形路径」，其和为  
   `l_tail_max + root.val + r_tail_max`（两侧单链都来自子树内部、且以各自子树根为端点向深处延伸）。

2. **整条路径完全落在某一侧子树**：不包含当前 `root` 作为「拐弯点」，答案已在左或右子树的递归结果里。

因此每个节点在 DFS 中要维护两类信息：

- **`root_max`**：在以 `root` 为根的子树中，任意合法路径的最大和（路径可在子树内任意拐弯一次）。
- **`root_tail_max`**：从 `root` 出发、**只能向下** 走到某个后代的路径最大和（供父节点把 `root` 接在下方，延续成更长的单链）。

空子树用极小哨兵 `-1001` 表示（题目保证节点值 ∈ [−1000, 1000]，比任何「单节点 + 空侧」的误用更差，从而不会误选空侧）。

这与 [112. 路径总和](../题目目录/0112-path-sum) 不同：112 要求根到叶的固定形状；本题路径可在任意节点拐弯，且节点值可为负，必须允许「不选某侧」。

---

### 2. 执行逻辑详细拆解

#### A. 空节点：不参与路径

Python

```
if not root:
    return -1001, -1001
```

- 没有节点，既无子树内最大路径，也无向下单链，用统一哨兵占位。

#### B. 后序：先拿到左右子树的 `(max, tail_max)`

Python

```
l_max, l_tail_max = dfs(root.left)
r_max, r_tail_max = dfs(root.right)
```

- `l_max` / `r_max`：左右子树内部已算好的最大路径和。
- `l_tail_max` / `r_tail_max`：从左孩子 / 右孩子出发向下延伸的最优单链和。

#### C. 经过 `root` 的向下单链（供父节点使用）

Python

```
root_tail_max = max(l_tail_max + root.val, r_tail_max + root.val, root.val)
```

- 只能选左链或右链之一接上 `root`（路径不能分叉），再与「只取 `root`」取最大。
- 若一侧为负贡献，上式自然退化为只走另一侧或只要 `root.val`。

#### D. 子树内全局最大：子树答案 vs 过 `root` 的弧形

Python

```
root_max = max(l_max, r_max, root_tail_max, l_tail_max + r_tail_max + root.val)
```

- `l_max`、`r_max`：路径完全在左或右子树。
- `root_tail_max`：整条路径只在以 `root` 为端点的下垂链上（仍在「子树内」）。
- `l_tail_max + r_tail_max + root.val`：以 `root` 为拐点，左右各接一条向下链。

#### E. 返回值与最终答案

Python

```
return root_max, root_tail_max
...
return max(dfs(root))
```

- 向上一层返回二元组；根处取 `max(tuple)` 等价于取 `root_max`（因必有 `root_max ≥ root_tail_max`）。

---

### 3. 算法可视化

以 `root = [1,2,3]` 为例：

1. 叶子 `2`：`tail = 2`，子树内最大 `2`。

2. 叶子 `3`：`tail = 3`，子树内最大 `3`。

3. 根 `1`：  
   
   - 向下单链：`max(2+1, 3+1, 1) = 4`。  
   - 弧形：`2 + 1 + 3 = 6`。  
   - 子树最大：`max(2, 3, 4, 6) = 6`。

---

### 4. 复杂度分析

- **时间复杂度**：$O(N)$，每个节点访问一次。

- **空间复杂度**：$O(H)$，递归栈深度为树高 $H$；链状树为 $O(N)$。

---

### 5. 代码实现回顾

```python
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return -1001, -1001
            l_max, l_tail_max = dfs(root.left)
            r_max, r_tail_max = dfs(root.right)
            root_tail_max = max(l_tail_max + root.val, r_tail_max + root.val, root.val)
            root_max = max(l_max, r_max, root_tail_max, l_tail_max + r_tail_max + root.val)

            return root_max, root_tail_max
        return max(dfs(root))
```
