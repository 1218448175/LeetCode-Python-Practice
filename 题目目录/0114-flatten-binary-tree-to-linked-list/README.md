## [114. 二叉树展开为链表](https://leetcode.cn/problems/flatten-binary-tree-to-linked-list/)

### 中等

给你二叉树的根结点 `root` ，请你将它展开为一个单链表：

- 展开后的单链表应该同样使用 `TreeNode` ，其中 `right` 子指针指向链表中下一个结点，而左子指针始终为 `null` 。
- 展开后的单链表应该与二叉树 [**先序遍历**](https://baike.baidu.com/item/%E5%85%88%E5%BA%8F%E9%81%8D%E5%8E%86/6442839?fr=aladdin) 顺序相同。

**示例 1：**

<img alt="" src="https://assets.leetcode.com/uploads/2021/01/14/flaten.jpg" style="width: 500px; height: 226px;">

<pre><strong>输入：</strong>root = [1,2,5,3,4,null,6]
<strong>输出：</strong>[1,null,2,null,3,null,4,null,5,null,6]
</pre>

---

## 题解：寻找前驱节点的原地展开法

### 1. 核心思路：寻找左子树的“最右节点”

题目要求将二叉树按 **先序遍历** 的顺序就地（in-place）展开为链表。先序遍历的顺序是：`根 -> 左 -> 右`。

你的代码采用了一种非常巧妙的非递归 $O(1)$ 空间算法：

- **观察规律**：在先序遍历中，左子树的所有节点都会出现在右子树的所有节点之前。

- **寻找前驱**：对于当前节点 `cur`，它的右子树（`cur.right`）应该被接到左子树先序遍历的最后一个节点（即左子树中“最靠右”的节点）的右边。

- **移动与置空**：完成连接后，将整个左子树移到右边，并将左指针置为空。

---

### 2. 执行逻辑详细拆解

#### A. 遍历与条件判断

Python

```
cur = root
while cur:
    if cur.left:
        # 如果有左子树，才需要进行“搬运”操作
```

- 我们从根节点开始向下遍历。如果当前节点没有左子树，它已经符合链表结构的一部分，直接处理下一个右节点。

#### B. 寻找左子树的最右节点

Python

```
prev = cur.left
while prev.right:
    prev = prev.right
```

- `prev` 最终会停在左子树的最右侧节点。根据先序遍历的特性，这个节点正是 `cur.right` 应该紧跟的位置。

#### C. 指针重组

Python

```
prev.right = cur.right  # 1. 将原有的右子树接到左子树的最右侧
cur.right = cur.left    # 2. 将整个左子树挪到右边
cur.left = None         # 3. 将左指针置空
```

- 这三行代码完成了核心的“拉直”动作。原先分叉的树结构，在这一步被合并成了一个暂时的单链表趋势。

#### D. 迭代向后

Python

```
cur = cur.right
```

- 继续处理下一个节点。注意，因为我们把左子树挪到了右边，所以这里的 `cur.right` 实际上就是原先的 `cur.left`。

---

### 3. 算法可视化

以树 `[1, 2, 5, 3, 4, null, 6]` 为例：

1. **处理节点 1**：
   
   - 左子树 `2` 的最右节点是 `4`。
   
   - 将 `1` 的右子树 `5` 接到 `4` 的后面：`4.right = 5`。
   
   - 将 `1` 的左子树移到右边：`1.right = 2`, `1.left = None`。
   
   - 此时树形如：`1 -> 2 -> 3 -> 4 -> 5 -> 6`（呈单链表状）。

2. **处理节点 2**：重复上述逻辑，将 `3` 的右边连上 `4`。

3. **最终结果**：所有节点都被拉平成只有右孩子的链表。

---

### 4. 复杂度分析

- **时间复杂度**：$O(N)$。虽然有嵌套循环，但每个节点最多被访问两次（一次是 `cur` 遍历，一次是作为 `prev` 的右边界被寻找）。

- **空间复杂度**：$O(1)$。只使用了两个辅助指针，没有使用递归栈或额外的数据结构。

---

### 5. 代码实现回顾

```python
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """        原地修改，不返回任何值        """
        cur = root
        while cur:
            if cur.left:
                # 寻找左子树中序遍历的最后一个节点（最右节点）
                prev = cur.left
                while prev.right:
                    prev = prev.right

                # 将原来的右子树接到左子树的最右节点上
                prev.right = cur.right
                # 将左子树整体移动到右边
                cur.right = cur.left
                # 记得将左子树置空
                cur.left = None

            # 继续处理下一个右节点
            cur = cur.right
```