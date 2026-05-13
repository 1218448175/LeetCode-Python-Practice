## [530. 二叉搜索树的最小绝对差](https://leetcode.cn/problems/minimum-absolute-difference-in-bst/)

### 简单

给你一个二叉搜索树的根节点 `root` ，返回 **树中任意两不同节点值之间的最小差值** 。

差值是一个正数，其数值等于两值之差的绝对值。

**示例 1：**

<img alt="" src="https://assets.leetcode.com/uploads/2021/02/05/bst1.jpg" style="width: 292px; height: 301px;">

<pre><strong>输入：</strong>root = [4,2,6,1,3]
<strong>输出：</strong>1
</pre>

---

## 题解：利用二叉搜索树的中序遍历特性

### 1. 核心思路：将 BST 转化为有序序列

这道题的关键在于理解 **二叉搜索树（BST）** 的本质特性：**中序遍历的结果是一个升序序列**。

- **性质推导**：在一个升序序列中，任意两个元素之间的最小差值，一定出现在**相邻两个元素**之间。

- **算法选择**：我们不需要比较所有节点对，只需要通过中序遍历，依次比较当前节点值与它的“前驱节点值”（即前一个访问的节点），记录下最小的差值即可。

- **状态维护**：在递归过程中，我们需要维护一个全局（或 nonlocal）变量 `pre` 来记录上一个访问的节点值，以及一个 `ans` 来存储当前找到的最小差值。

---

### 2. 执行逻辑的详细拆解

#### A. 初始化

- `ans = inf`：初始最小差值设为无穷大。

- `pre = -1`：用于记录上一个遍历到的节点值。初始化为 -1 是为了标记“当前还没有访问过任何节点”。

#### B. 中序遍历过程（递归）

1. **左**：`inorder(node.left)` —— 优先深入最左侧，找到最小值。

2. **根（处理逻辑）**：
   
   - 检查 `pre` 是否有效（不为 -1）。
   
   - 如果有效，计算 `node.val - pre`（因为是升序，所以结果必为正）。
   
   - 对比并更新全局最小值 `ans`。
   
   - **更新前驱**：将 `pre` 更新为当前节点的值，供下一个节点使用。

3. **右**：`inorder(node.right)` —— 处理完当前节点后，转向右子树。

#### C. 返回结果

- 遍历结束后，`ans` 中存储的就是整棵树中相邻节点差值的最小值。

---

### 3. 与普通二叉树的区别（可选思路）

如果这只是一棵普通二叉树，我们可能需要先遍历整棵树存入数组，排序后再计算，或者进行 $O(n^2)$ 的暴力对比。正是由于 BST 的有序性，我们才能在 $O(n)$ 的一次遍历中完成计算。

---

### 4. 复杂度分析

- **时间复杂度**：$O(n)$。其中 $n$ 为二叉树的节点数。中序遍历需要访问每个节点恰好一次。

- **空间复杂度**：$O(h)$。其中 $h$ 为二叉树的高度。空间复杂度主要取决于递归调用栈的深度，最坏情况下（树呈链状）为 $O(n)$，平均情况下为 $O(\log n)$。

---

### 5. 代码回顾

```pyt
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        ans = float('inf')
        pre = -1

        def inorder(node):
            nonlocal pre, ans
            if not node:
                return

            # 1. 递归左子树
            inorder(node.left)

            # 2. 处理当前节点逻辑
            if pre != -1:
                # BST 中序遍历是递增的，所以 node.val > pre
                ans = min(ans, node.val - pre)
            # 更新前驱节点
            pre = node.val

            # 3. 递归右子树
            inorder(node.right)

        inorder(root)
        return ans
```