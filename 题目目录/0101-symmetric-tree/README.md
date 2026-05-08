## [101. 对称二叉树](https://leetcode.cn/problems/symmetric-tree/)

### 简单

给你一个二叉树的根节点 `root` ， 检查它是否轴对称。

**示例 1：**

<img alt="" src="https://pic.leetcode.cn/1698026966-JDYPDU-image.png" style="width: 354px; height: 291px;">

<pre><strong>输入：</strong>root = [1,2,2,3,4,4,3]
<strong>输出：</strong>true
</pre>

---

## 题解：双指针镜像递归法

### 1. 核心思路：镜像对比

判断一棵树是否对称，本质上不是看左右子树是否**相等**（那是 `isSameTree`），而是看它们是否**镜像**。

想象在根节点中间放一面镜子：

- 左子树的**左**孩子应该与右子树的**右**孩子相等。

- 左子树的**右**孩子应该与右子树的**左**孩子相等。

你的代码定义了一个辅助函数 `check(l, r)`，通过“双指针”同步移动，完美实现了这一逻辑。

---

### 2. 执行逻辑拆解

#### A. 辅助函数 `check(l, r)`

这是递归的核心，它同时接收两个节点进行比对：

1. **同时为空**：`if not l and not r: return True` —— 结构对称，匹配成功。

2. **一个为空一个不为空**：`if not l or not r: return False` —— 结构不对称，匹配失败。

3. **值判定与递归**：
   
   - `l.val == r.val`：当前两个镜像位置的值必须相等。
   
   - `self.check(l.left, r.right)`：递归比较“左的左”和“右的右”（外侧）。
   
   - `self.check(l.right, r.left)`：递归比较“左的右”和“右的左”（内侧）。

#### B. 主函数 `isSymmetric`

- 处理根节点。如果是空树，认为是对称的。

- 否则，从根节点的左右儿子开始进行 `check`。

---

### 3. 算法可视化：递归过程

以 `root = [1, 2, 2, 3, 4, 4, 3]` 为例：

1. **Start**: `check(Node_2_Left, Node_2_Right)`

2. **Compare Vals**: `2 == 2` (True)

3. **Recursive Call 1 (外侧)**: `check(Left_3, Right_3)` -> 返回 `True`

4. **Recursive Call 2 (内侧)**: `check(Left_4, Right_4)` -> 返回 `True`

5. **Final Result**: `True and True and True` -> `True`

---

### 4. 复杂度分析

- **时间复杂度**：$O(N)$。我们需要遍历树中所有的节点来确认对称性。

- **空间复杂度**：$O(H)$。其中 $H$ 是树的高度。空间消耗主要在于递归调用的系统栈。在最坏情况下（树退化为链状），高度为 $N$。

---

### 5. 代码实现回顾

```python
class Solution:
    def check(self, l: Optional[TreeNode], r: Optional[TreeNode]) -> bool:
        # 情况 1: 都为空，是对称的
        if not l and not r:
            return True
        # 情况 2: 只有一个为空，不对称
        if not l or not r:
            return False
        # 情况 3: 值相等，且 镜像子树也对称
        # 注意这里是 l.left 对应 r.right (外侧)
        # l.right 对应 r.left (内侧)
        return (l.val == r.val and 
                self.check(l.left, r.right) and 
                self.check(l.right, r.left))

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # 根节点为空或左右镜像
        return not root or self.check(root.left, root.right)### 总结
```