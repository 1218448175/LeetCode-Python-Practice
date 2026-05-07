## [100. 相同的树](https://leetcode.cn/problems/same-tree/)

### 简单

给你两棵二叉树的根节点 `p` 和 `q` ，编写一个函数来检验这两棵树是否相同。

如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

**示例 1：**

<img alt="" src="https://assets.leetcode.com/uploads/2020/12/20/ex1.jpg" style="width: 622px; height: 182px;">

<pre><strong>输入：</strong>p = [1,2,3], q = [1,2,3]
<strong>输出：</strong>true
</pre>

---

## 题解：深度优先搜索 (DFS) 递归判定

### 1. 核心思路：递归的三要素

判定两棵树是否相同，本质上是同时对两棵树进行**前序遍历**。只有当当前节点相同，且它们的左右子树也分别相同时，整棵树才相同。

你的代码准确地捕捉到了递归的核心逻辑：

- **根节点相同**：$p.val == q.val$。

- **左子树相同**：递归判定 $p.left$ 和 $q.left$。

- **右子树相同**：递归判定 $p.right$ 和 $q.right$。

---

### 2. 执行逻辑的详细拆解

#### A. 基准情况 (Base Cases)

递归最关键的是如何停下来。你的代码处理得非常严谨：

1. **完全相等**：`if p == q: return True`
   
   - 这个判断涵盖了 $p$ 和 $q$ 同时为 `None` 的情况（此时引用相同），也处理了同一棵树的对比。

2. **结构不对称**：`if not p or not q: return False`
   
   - 在排除了两者皆为空的可能性后，如果其中一个为空，另一个不为空，说明结构不同，直接返回 `False`。

#### B. 递归判定与合并

1. **分治**：通过 `left_same` 和 `right_same` 将问题规模缩小到子树。

2. **验证**：最后通过 `p.val == q.val and left_same and right_same` 确保当前节点和后代全部达标。

---

### 3. 算法可视化：递归决策树

假设比较以下两棵树：

- 树 P: `[1, 2, 3]`

- 树 Q: `[1, 2, 3]`
1. **Level 1**: 比较根节点 `1`。值相同，继续递归。

2. **Level 2 (Left)**: 比较左子节点 `2`。值相同，其子节点皆为空，返回 `True`。

3. **Level 2 (Right)**: 比较右子节点 `3`。值相同，其子节点皆为空，返回 `True`。

4. **Result**: 三个条件全为 `True`，最终结果为 `True`。

---

### 4. 复杂度分析

- **时间复杂度**：$O(\min(N, M))$。其中 $N$ 和 $M$ 分别是两棵树的节点数。一旦发现不匹配就会提前返回，最坏情况下需要遍历整棵树。

- **空间复杂度**：$O(\min(H_p, H_q))$。其中 $H$ 是树的高度，主要开销是递归调用的系统栈空间。

---

### 5. 代码实现

```python
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # 1. 如果都为空，相同
        if not p and not q:
            return True
        # 2. 如果其中一个为空，或者值不相等，不同
        if not p or not q or p.val != q.val:
            return False

        # 3. 递归比较左右子树
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
```