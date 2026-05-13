## [98. 验证二叉搜索树](https://leetcode.cn/problems/validate-binary-search-tree/)

### 中等

给你一个二叉树的根节点 `root` ，判断其是否是一个有效的二叉搜索树。

**有效** 二叉搜索树定义如下：

- 节点的左子树只包含 **严格小于** 当前节点的数。
- 节点的右子树只包含 **严格大于** 当前节点的数。
- 所有左子树和右子树自身必须也是二叉搜索树。

**示例 1：**

<img alt="" src="https://assets.leetcode.com/uploads/2020/12/01/tree1.jpg" style="width: 302px; height: 182px;">

<pre><strong>输入：</strong>root = [2,1,3]
<strong>输出：</strong>true
</pre>

---

## 题解：基于中序遍历的严格递增判定

### 1. 核心思路：中序遍历的单调性

验证二叉搜索树（BST）最直观的方法是利用其核心性质：**BST 的中序遍历序列必须是严格递增的。**

- **判定条件**：在遍历过程中，每一个当前节点的值 `root.val` 必须大于它前一个访问的节点值 `pre`。

- **全局状态**：通过一个类成员变量或全局变量 `self.pre` 来记录“上一个节点的值”，并在遍历过程中不断更新和比较。

- **严格限制**：题目要求“严格小于”和“严格大于”，因此如果 `root.val <= self.pre`，则该树不是有效的 BST。

---

### 2. 执行逻辑的详细拆解

#### A. 初始化与边界

- `self.pre = -inf`：初始值设为负无穷，确保树中最小的节点也能通过第一次比较。

- `if root is None: return True`：递归到底部或空树时，默认是符合要求的。

#### B. 递归左子树

Python

```
if not self.isValidBST(root.left):
    return False
```

- 优先检查左子树。如果左子树已经发现不符合 BST 定义，立即向上返回 `False`，实现**剪枝**。

#### C. 当前节点校验

Python

```
if root.val <= self.pre:
    return False
self.pre = root.val
```

- **核心逻辑**：检查当前节点值是否大于前驱节点值。

- 如果校验通过，更新 `self.pre` 为当前节点值，为进入右子树做准备。

#### D. 递归右子树

- 最后检查右子树，只有左子树、当前节点、右子树全部合法，整棵树才返回 `True`。

---

### 3. 陷阱提醒：为什么不能只比较父子？

一个常见的错误是只检查 `root.left.val < root.val < root.right.val`。

- **错误原因**：BST 要求左子树的**所有**节点都小于根节点。

- **示例**：如果根是 10，左孩子是 5，但 5 的右孩子是 11。虽然 $5 < 11$，但 $11 > 10$，这违反了 BST 的全局规则。

- **中序遍历**能完美避开这个陷阱，因为它通过 `pre` 变量携带了全局的约束信息。

---

### 4. 复杂度分析

- **时间复杂度**：$O(n)$。其中 $n$ 为节点总数，每个节点必须访问一次。

- **空间复杂度**：$O(h)$。其中 $h$ 为树的高度。这是递归调用栈的深度，最坏情况下为 $O(n)$。

---

### 5. 代码回顾

```pytho
class Solution:
    # 使用类变量记录前驱值，注意多次调用时需重置
    pre = -float('inf')

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        # 1. 递归左子树
        if not self.isValidBST(root.left):
            return False

        # 2. 访问当前节点：必须严格大于前驱节点
        if root.val <= self.pre:
            return False

        # 3. 更新前驱节点
        self.pre = root.val

        # 4. 递归右子树
        return self.isValidBST(root.right)
```