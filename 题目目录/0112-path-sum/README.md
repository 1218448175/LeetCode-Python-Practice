## [112. 路径总和](https://leetcode.cn/problems/path-sum/)

### 简单

给你二叉树的根节点 `root` 和一个表示目标和的整数 `targetSum` 。判断该树中是否存在 **根节点到叶子节点** 的路径，这条路径上所有节点值相加等于 `targetSum` 。

**叶子节点** 是指没有子节点的节点。

**示例 1：**

<img alt="" src="https://assets.leetcode.com/uploads/2021/01/18/pathsum1.jpg" style="width: 500px; height: 356px;">

<pre><strong>输入：</strong>root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
<strong>输出：</strong>true
<strong>解释：</strong>存在一条路径 5 → 4 → 11 → 2，和为 22。
</pre>

---

## 题解：自顶向下递减目标值的 DFS

### 1. 核心思路：把「凑目标和」变成「一路扣减」

要在根到叶的某条路径上判断「节点值之和是否等于 `targetSum`」，可以等价地看成：从根出发，每经过一个节点，就用剩余目标减去当前节点的值；走到**叶子**时，若剩余值恰好为 `0`，说明存在合法路径。

你的写法是经典的 **深度优先搜索（DFS）递归**：在每一层维护「还需要多少」这个子问题，边界是空树与叶子。

---

### 2. 执行逻辑详细拆解

#### A. 空节点：直接否定

Python

```
if not root:
    return False
```

- 空树不存在任何根到叶的路径，返回 `False`。这也统一处理了递归中某一侧子树为空的情况。

#### B. 更新剩余目标和

Python

```
nxt_target = targetSum - root.val
```

- 进入当前节点后，先把当前值从目标里减掉，后续子树只关心「还差 `nxt_target`」。

#### C. 叶子节点：一次性判定

Python

```
if not root.left and not root.right:
    return nxt_target == 0
```

- **必须是叶子**：左右孩子都为空时，路径在此结束；此时若 `nxt_target == 0`，说明从根到该叶子的累加和等于最初的 `targetSum`。

#### D. 非叶子：左右子树任选一条成立即可

Python

```
return self.hasPathSum(root.left, nxt_target) or self.hasPathSum(root.right, nxt_target)
```

- 只要左或右子树中存在满足条件的路径，整棵树就返回 `True`。  
- 若某一侧为空，`hasPathSum(None, ...)` 会在 **A** 处返回 `False`，不会影响另一侧的正确性。

---

### 3. 算法可视化

以示例树 `targetSum = 22` 为例，关注一条合法路径：

1. **根 5**：剩余 `22 - 5 = 17`。

2. **节点 4**：剩余 `17 - 4 = 13`。

3. **节点 11**：剩余 `13 - 11 = 2`。

4. **叶子 2**：剩余 `2 - 2 = 0`，且为叶子 → 返回 `True`。

递归过程中，若某条分支在中间就「减过头」或「减不够」但在叶子处不为 0，该分支返回 `False`；最终由 **D** 的 `or` 汇总结果。

---

### 4. 复杂度分析

- **时间复杂度**：$O(N)$。其中 $N$ 为节点个数，每个节点最多访问常数次。

- **空间复杂度**：$O(H)$。其中 $H$ 为树高，主要来自递归栈；链状树时 $H = N$，平衡树时约为 $O(\log N)$。

---

### 5. 代码实现回顾

```python
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        nxt_target = targetSum - root.val
        if not root.left and not root.right:
            return nxt_target == 0
        return self.hasPathSum(root.left, nxt_target) or self.hasPathSum(root.right, nxt_target)
```
