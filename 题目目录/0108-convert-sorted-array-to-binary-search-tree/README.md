## [108. 将有序数组转换为二叉搜索树](https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree/)

### 简单

给你一个整数数组 `nums`，其中元素已经按 **升序** 排列，请你将其转换为一棵 **高度平衡** 二叉搜索树。

**示例 1：**

<pre><strong>输入：</strong>nums = [-10,-3,0,5,9]
<strong>输出：</strong>[0,-3,9,-10,null,5]
<strong>解释：</strong>[0,-10,5,null,-3,null,9] 也将被视为正确答案
</pre>

**示例 2：**

<pre><strong>输入：</strong>nums = [1,3]
<strong>输出：</strong>[3,1]
<strong>解释：</strong>[1,null,3] 和 [3,1] 都是高度平衡二叉搜索树。
</pre>

---

## 题解：分治递归，取中点作根

### 1. 核心思路：有序数组与 BST 的天然对应

数组已严格升序，若把当前区间的 **中间元素** 作为子树根，则：

- 左侧子数组全部小于根 → 自然构成 **左子树**；
- 右侧子数组全部大于根 → 自然构成 **右子树**。

每次选 `mid = (left + right) // 2`，左右子区间规模最多相差 1，递归下去即可得到 **高度平衡** 的 BST，无需额外旋转或平衡操作。

---

### 2. 执行逻辑拆解

#### A. 递归边界

```python
if left > right:
    return None
```

当前区间为空时，对应空子树。

#### B. 建根与划分子区间

```python
mid = (left + right) // 2
node = TreeNode(nums[mid])
node.left = helper(left, mid - 1)
node.right = helper(mid + 1, right)
```

- `helper(left, mid - 1)`：左子树；
- `helper(mid + 1, right)`：右子树。

#### C. 入口

```python
return helper(0, len(nums) - 1)
```

对整个有序数组做一次分治即可。

---

### 3. 算法可视化

以 `nums = [-10, -3, 0, 5, 9]` 为例：

1. 区间 `[0, 4]`，`mid = 2`，根为 `0`；
2. 左区间 `[-10, -3]`，`mid = 0`，根为 `-10`，再挂右子 `-3`；
3. 右区间 `[5, 9]`，`mid = 1`，根为 `9`，左子为 `5`。

得到结构 `[0, -3, 9, -10, null, 5]`，满足 BST 性质且左右子树高度差不超过 1。

---

### 4. 复杂度分析

- **时间复杂度**：$O(n)$。每个元素恰好被访问一次并建为一个节点。
- **空间复杂度**：$O(\log n)$。递归栈深度为树高；若计入结果树本身则为 $O(n)$。

---

### 5. 代码实现回顾

```python
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(left: int, right: int):
            if left > right:
                return None
            mid = (left + right) // 2
            node = TreeNode(nums[mid])
            node.left = helper(left, mid - 1)
            node.right = helper(mid + 1, right)
            return node
        return helper(0, len(nums) - 1)
```
