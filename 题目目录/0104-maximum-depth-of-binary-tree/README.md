## [104. 二叉树的最大深度](https://leetcode.cn/problems/maximum-depth-of-binary-tree/)

### 简单

给定一个二叉树 `root` ，返回其最大深度。

二叉树的 **最大深度** 是指从根节点到最远叶子节点的最长路径上的节点数。

**示例 1：**

<img alt="" src="https://assets.leetcode.com/uploads/2020/11/26/tmp-tree.jpg" style="width: 400px; height: 277px;">

<pre><b>输入：</b>root = [3,9,20,null,null,15,7]
<b>输出：</b>3
</pre>

---

## 题解：分治递归法求二叉树深度

### 1. 核心思路：分治思想 (Divide and Conquer)

要求整棵树的最大深度，可以将其拆解为子问题：

**“整棵树的最大深度 = max(左子树深度, 右子树深度) + 1”**

这里的 `+ 1` 是因为要加上根节点本身占据的一层。这种自底向上的思考方式是解决二叉树递归问题的经典套路。

---

### 2. 执行逻辑拆解

#### A. 递归终止条件 (Base Case)

Python

```
if not root:
    return 0
```

- 当递归到空节点时（即越过了叶子节点），说明当前路径已经结束，深度为 `0`。

#### B. 递归计算左右子树

- `self.maxDepth(root.left)`：递归计算左子树的高度。

- `self.maxDepth(root.right)`：递归计算右子树的高度。

#### C. 合并结果 (Return)

- 使用 `max()` 函数取出左右子树中较大的那个深度。

- 最后 `+ 1` 回溯给父节点。

---

### 3. 算法可视化

以树 `[3, 9, 20, null, null, 15, 7]` 为例：

1. **节点 15**: 左右皆空，返回 `max(0, 0) + 1 = 1`。

2. **节点 7**: 左右皆空，返回 `max(0, 0) + 1 = 1`。

3. **节点 20**: 左边返回 1，右边返回 1，返回 `max(1, 1) + 1 = 2`。

4. **节点 9**: 左右皆空，返回 `max(0, 0) + 1 = 1`。

5. **根节点 3**: 左边返回 1，右边返回 2，最终返回 `max(1, 2) + 1 = 3`。

---

### 4. 复杂度分析

- **时间复杂度**：$O(N)$。其中 $N$ 为二叉树的节点数，每个节点必须访问且仅访问一次。

- **空间复杂度**：$O(H)$。其中 $H$ 为二叉树的高度。空间消耗主要来自递归调用的栈空间。
  
  - 最坏情况（树呈链状）：$O(N)$。
  
  - 最好情况（完全二叉树）：$O(\log N)$。

---

### 5. 代码实现回顾

```python
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # 如果节点为空，深度为 0
        if not root:
            return 0

        # 递归求左子树深度
        left_h = self.maxDepth(root.left)
        # 递归求右子树深度
        right_h = self.maxDepth(root.right)

        # 当前深度 = 左右子树最大深度 + 1（根节点自己）
        return max(left_h, right_h) + 1
```