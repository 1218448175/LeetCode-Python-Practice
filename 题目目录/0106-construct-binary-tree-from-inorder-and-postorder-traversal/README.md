## [106. 从中序与后序遍历序列构造二叉树](https://leetcode.cn/problems/construct-binary-tree-from-inorder-and-postorder-traversal/)

### 中等

给定两个整数数组 `inorder` 和 `postorder` ，其中 `inorder` 是二叉树的中序遍历， `postorder` 是同一棵树的后序遍历，请你构造并返回这颗 *二叉树* 。

**示例 1:**

<img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/tree.jpg">

<pre><b>输入：</b>inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
<b>输出：</b>[3,9,20,null,null,15,7]
</pre>

---

## 题解：后序遍历的倒序特性与递归构建

### 1. 核心思路：后序遍历的“尾部根节点”特性

从中序与后序遍历构造二叉树的逻辑，与“前序+中序”非常相似，但有一个关键的逆向思维。

- **后序遍历 (Postorder)**：序列格式为 `[ [左子树], [右子树], 根节点 ]`。这意味着序列的**最后一个元素**永远是当前树的根节点。

- **中序遍历 (Inorder)**：序列格式为 `[ [左子树], 根节点, [右子树] ]`。利用根节点在其中的位置，可以精确划分左右子树的边界。

你的代码利用了 Python 列表的 `pop()` 操作，配合**先递归右子树、再递归左子树**的顺序，极大地简化了指针计算。

---

### 2. 执行逻辑详细拆解

#### A. 倒序处理与 `pop()`

Python

```
val = postorder.pop()
```

由于后序遍历的根节点在最后，如果我们从后往前取值，取出的顺序依次是：**根节点 -> 右子树根节点 -> 左子树根节点**。

- **关键顺序**：在代码中，你**必须**先调用 `root.right = helper(...)` 再调用 `root.left = helper(...)`。因为 `postorder` 弹出的是右子树的根。

#### B. 哈希表定位

Python

```
idx_map = {val:idx for idx, val in enumerate(inorder)}
```

同理，为了避免在 $O(N)$ 的中序序列中扫描根节点位置，使用哈希表进行 $O(1)$ 定位是提升性能的核心。

#### C. 递归边界控制

`helper(in_left, in_right)` 仅需维护中序遍历的左右边界。

- 当 `in_left > in_right` 时，说明当前区间没有节点，返回 `None`。

- `index` 是根节点在中序序列中的位置。

- **右子树区间**：`[index + 1, in_right]`。

- **左子树区间**：`[in_left, index - 1]`。

---

### 3. 算法可视化：执行流模拟

以 `inorder = [9, 3, 15, 20, 7]`, `postorder = [9, 15, 7, 20, 3]` 为例：

1. **第一步**：`postorder` 弹出 `3`。中序中 `3` 的索引是 `1`。
   
   - 此时 `inorder` 被分为：左边 `[9]`，右边 `[15, 20, 7]`。

2. **第二步（必须处理右边）**：`postorder` 弹出 `20`（右子树根）。中序中 `20` 的索引是 `3`。
   
   - 右侧 `[15, 20, 7]` 被分为：左边 `[15]`，右边 `[7]`。

3. **第三步**：继续弹出 `7`（处理 `20` 的右孩子），然后是 `15`（处理 `20` 的左孩子）。

4. **最后**：才处理最初 `3` 的左边 `[9]`。

---

### 4. 复杂度分析

- **时间复杂度**：$O(N)$。每个节点仅被弹出一次，哈希表查询为 $O(1)$。

- **空间复杂度**：$O(N)$。哈希表占用 $O(N)$，递归栈深度最坏情况下为 $O(N)$。

---

### 5. 代码实现回顾

```python
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def helper(in_left, in_right):
            if in_left > in_right:
                return None

            # 1. 弹出后序遍历的最后一个元素作为根
            val = postorder.pop()
            root = TreeNode(val)

            # 2. 获取根在中序遍历中的位置
            index = idx_map[val]

            # 3. 注意！！！必须先构造右子树
            # 因为 postorder 弹出的是右子树的根
            root.right = helper(index + 1, in_right)

            # 4. 构造左子树
            root.left = helper(in_left, index - 1)

            return root

        idx_map = {val:idx for idx, val in enumerate(inorder)} 
        return helper(0, len(inorder) - 1)
```