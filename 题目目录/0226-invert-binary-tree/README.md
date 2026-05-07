## [226. 翻转二叉树](https://leetcode.cn/problems/invert-binary-tree/)

### 简单

给你一棵二叉树的根节点 `root` ，翻转这棵二叉树，并返回其根节点。

**示例 1：**

<p><img alt="" src="https://assets.leetcode.com/uploads/2021/03/14/invert1-tree.jpg" style="height: 165px; width: 500px;"></p>

<pre><strong>输入：</strong>root = [4,2,7,1,3,6,9]
<strong>输出：</strong>[4,7,2,9,6,3,1]
</pre>

---

## 题解：自底向上的递归翻转

### 1. 核心思路：镜像交换

翻转二叉树（又称“二叉树的镜像”）的核心逻辑非常直观：**对于树中的每一个节点，交换其左子节点和右子节点。**

你的代码采用了典型的**后序遍历**（自底向上）递归思路：

1. 先递归地翻转左子树。

2. 再递归地翻转右子树。

3. 最后交换当前节点的左右指针。

---

### 2. 执行逻辑拆解

#### A. 递归终止条件

Python

```
if not root:
    return None
```

- 当遇到空节点时，直接返回 `None`。这是递归的出口，确保不会对不存在的节点进行操作。

#### B. 递去：处理子树

Python

```
invert_left = self.invertTree(root.left)
invert_right = self.invertTree(root.right)
```

- 通过递归调用，程序会一直深入到叶子节点。

- `invert_left` 接收的是已经翻转好的左子树根节点。

- `invert_right` 接收的是已经翻转好的右子树根节点。

#### C. 归回：交换位置

Python

```
root.left, root.right = invert_right, invert_left
```

- 利用 Python 的元组解包特性，一行代码直接完成左右指针的交换。

- **注意**：在当前节点完成交换后，以当前节点为根的子树就已经完成了“镜像翻转”。

---

### 3. 算法可视化

以 `root = [4, 2, 7]` 为例：

1. 进入 `4`，递归调用 `2` 和 `7`。

2. `2` 的左右为空，返回 `2` 给父节点。

3. `7` 的左右为空，返回 `7` 给父节点。

4. 回到 `4`，执行交换：`4.left` 变为 `7`，`4.right` 变为 `2`。

5. 结果变为 `[4, 7, 2]`。

---

### 4. 复杂度分析

- **时间复杂度：$O(N)$**
  
  其中 $N$ 是节点的数量。我们需要访问树中的每一个节点来执行交换操作。

- **空间复杂度：$O(H)$**
  
  其中 $H$ 是树的高度。这是由于递归调用产生的系统栈空间。在最坏情况下（树退化成链表），空间复杂度为 $O(N)$。

---

### 5. 代码实现回顾

```python
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 1. 终止条件
        if not root:
            return None

        # 2. 递归获取翻转后的左右子树
        # 这里实际上是后序遍历的思想
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)

        # 3. 交换当前节点的左右指向
        root.left, root.right = right, left

        # 4. 返回当前节点给上一层
        return root
```