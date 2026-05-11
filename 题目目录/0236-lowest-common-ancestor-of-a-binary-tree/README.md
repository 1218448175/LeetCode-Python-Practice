## [236. 二叉树的最近公共祖先](https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/)

### 中等

给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：「对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（**一个节点也可以是它自己的祖先**）。」

**示例 1：**

<img alt="" src="https://assets.leetcode.com/uploads/2018/12/14/binarytree.png" style="width: 200px; height: 190px;">

<pre><b>输入：</b>root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
<b>输出：</b>3
<b>解释：</b>节点 5 和节点 1 的最近公共祖先是节点 3 。
</pre>

**示例 2：**

<pre><b>输入：</b>root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
<b>输出：</b>5
<b>解释：</b>节点 5 和节点 4 的最近公共祖先是节点 5 。因为根据定义最近公共祖先节点可以为节点本身。
</pre>

**提示：**

- 树中节点数目在范围 `[2, 10^5]` 内。
- `-10^9 <= Node.val <= 10^9`
- 所有 `Node.val` 互不相同。
- `p != q`
- `p` 和 `q` 均存在于给定的二叉树中。

---

## 题解：后序 DFS 一次遍历

### 1. 核心思路：自底向上「汇报」是否见过 p / q

从根做**后序**（先左、再右、最后处理当前根）：子树递归返回的是「在这一侧子树里找到的 p 或 q（若存在）」。

- 若当前 `root` 为空，或 `root` 本身就是 `p` 或 `q`，直接返回 `root`：空无贡献；命中目标则把该节点当作「已找到的一侧」向上传递（**一个节点可以是自己的祖先**，因此与 p、q 重合时立即返回）。
- 否则分别在左右子树递归，得到 `left`、`right`。
- **若 `left` 与 `right` 都非空**：说明 `p`、`q` 分居当前根的两侧，**当前 `root` 即为 LCA**。
- **若只有一侧非空**：LCA 一定在那一侧（另一侧子树完全没找到 p/q），返回非空的那一侧即可。

---

### 2. 执行逻辑拆解

#### A. 递归终止 / 剪枝（Base Case）

Python

```
if root in (None, p, q):
    return root
```

- `None`：无节点可找。
- `root is p` 或 `root is q`：当前根就是目标之一，无需再向下找「另一个」，直接把该节点返回给父层拼接路径。

#### B. 左右子树递归

Python

```
left = self.lowestCommonAncestor(root.left, p, q)
right = self.lowestCommonAncestor(root.right, p, q)
```

- `left`：左子树里若存在 p 或 q（或它们的 LCA），会返回对应节点；否则为 `None`。
- `right`：同理。

#### C. 合并结果

Python

```
if left and right:
    return root
return left or right
```

- 两侧都有结果 → 当前根是**分叉点**，即 LCA。
- 只有一侧有 → 继续向上冒泡那一侧的结果。

---

### 3. 算法可视化（示例 1）

树中 `p=5`、`q=1` 分居根 `3` 的左右子树：左递归最终在左子树找到与 `5` 相关的结构，右递归在右子树找到 `1`，在根处 `left` 与 `right` 同时非空 → 返回 `3`。

若 `p=5`、`q=4` 都在根的左子树内：右子树递归得到 `None`，左子树会返回**较深层的 LCA**（此处为 `5`），根处只一侧非空 → 返回 `5`。

---

### 4. 复杂度分析

- **时间复杂度**：$O(N)$。每个节点最多访问一次。
- **空间复杂度**：$O(H)$。$H$ 为树高，递归栈深度；链状树最坏 $O(N)$。

---

### 5. 代码实现回顾

```python
class Solution:

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root in (None, p, q):
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root

        return left or right
```
