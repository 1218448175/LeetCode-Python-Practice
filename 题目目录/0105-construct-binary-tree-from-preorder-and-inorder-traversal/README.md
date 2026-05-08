## [105. 从前序与中序遍历序列构造二叉树](https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)

### 中等

给定两个整数数组 `preorder` 和 `inorder` ，其中 `preorder` 是二叉树的**先序遍历**， `inorder` 是同一棵树的**中序遍历**，请构造二叉树并返回其根节点。

**示例 1:**

<img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/tree.jpg" style="height: 302px; width: 277px;">

<pre><strong>输入</strong><strong>:</strong> preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
<strong>输出:</strong> [3,9,20,null,null,15,7]
</pre>

---

## 题解：分治递归与哈希表加速映射

### 1. 核心思路：利用遍历特性定位根与子树

从前序和中序遍历序列构造二叉树，关键在于利用两种遍历的固有特点：

- **前序遍历 (Preorder)**：序列的第一个元素永远是**根节点**。

- **中序遍历 (Inorder)**：一旦确定了根节点的值，该值在序列中的位置就将树分成了**左子树**（左侧所有元素）和**右子树**（右侧所有元素）。

你的代码采用了**分治法**：通过前序遍历找到根，在中序遍历中确定左右子树的大小，然后递归地构造左、右子树。

---

### 2. 执行逻辑详细拆解

#### A. 哈希表优化

Python

```
index_hash = {element: i for i, element in enumerate(inorder)}
```

这是代码中的一个巨大亮点。在中序遍历中寻找根节点索引的操作，如果每次都用 `list.index()`，复杂度会退化到 $O(N^2)$。使用哈希表预存储，可以将定位根节点的时间复杂度降低到 **$O(1)$**。

#### B. 递归函数参数设计

`myBuildTree` 使用了四个指针（`preorder_left, preorder_right, inorder_left, inorder_right`），这种**下标传递**的方式比直接切片（Slicing）更节省空间和时间，避免了频繁创建数组副本。

#### C. 计算左子树大小

Python

```
size_left_subtree = inorder_root - inorder_left
```

这是连接两个序列的“桥梁”。知道左子树有多少个节点后，我们就能在前序序列中精准划定左子树和右子树的边界。

#### D. 指针推导逻辑

- **左子树**：
  
  - 前序：从 `preorder_left + 1` 到 `preorder_left + size_left_subtree`。
  
  - 中序：从 `inorder_left` 到 `inorder_root - 1`。

- **右子树**：
  
  - 前序：从 `preorder_left + size_left_subtree + 1` 到 `preorder_right`。
  
  - 中序：从 `inorder_root + 1` 到 `inorder_right`。

---

### 3. 算法可视化

以 `preorder = [3, 9, 20, 15, 7]`, `inorder = [9, 3, 15, 20, 7]` 为例：

1. **第一层递归**：前序首位是 `3`。中序中 `3` 的位置在索引 `1`。
   
   - 左子树只有 `9`（大小为 1）。
   
   - 右子树有 `[15, 20, 7]`（大小为 3）。

2. **第二层递归（左）**：处理 `9`，构建叶子节点。

3. **第二层递归（右）**：前序剩余 `[20, 15, 7]`，首位是 `20`。中序中 `20` 的位置将 `15` 分在左，`7` 分在右。

---

### 4. 复杂度分析

- **时间复杂度**：$O(N)$。其中 $N$ 是节点个数。哈希表初始化 $O(N)$，递归每个节点访问一次 $O(N)$。

- **空间复杂度**：$O(N)$。哈希表需要 $O(N)$ 空间，递归栈深度在最坏情况下（树退化为链表）也是 $O(N)$。

---

### 5. 代码实现回顾

```python
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def myBuildTree(pre_l: int, pre_r: int, in_l: int, in_r: int):
            if pre_l > pre_r:
                return None

            # 1. 前序遍历的第一个节点就是根节点
            pre_root_idx = pre_l
            # 2. 在中序遍历中定位根节点
            in_root_idx = index_hash[preorder[pre_root_idx]]

            # 3. 建立根节点
            root = TreeNode(preorder[pre_root_idx])

            # 4. 得到左子树中的节点数目
            size_left = in_root_idx - in_l

            # 5. 递归构造左子树
            # 前序：[根+1, 根+左子树大小]；中序：[中序左, 根索引-1]
            root.left = myBuildTree(pre_l + 1, pre_l + size_left, in_l, in_root_idx - 1)

            # 6. 递归构造右子树
            # 前序：[根+左子树大小+1, 末尾]；中序：[根索引+1, 中序右]
            root.right = myBuildTree(pre_l + size_left + 1, pre_r, in_root_idx + 1, in_r)

            return root

        n = len(preorder)
        # 预处理哈希表
        index_hash = {val: i for i, val in enumerate(inorder)}
        return myBuildTree(0, n - 1, 0, n - 1)
```