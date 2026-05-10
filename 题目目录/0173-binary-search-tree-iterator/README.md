## [173. 二叉搜索树迭代器](https://leetcode.cn/problems/binary-search-tree-iterator/)

### 中等

实现一个二叉搜索树迭代器类 `BSTIterator` ，表示一颗二叉搜索树的迭代器：

- `BSTIterator(TreeNode root)` 用二叉搜索树的根节点初始化迭代器。
- `boolean hasNext()` 如果存在数值较小的下一个节点，返回 `true` ；否则返回 `false` 。
- `int next()` 指针向右移动，返回二叉搜索树中下一个最小的数字。

可以假设 `next()` 调用总是有效的，即调用 `next()` 时，迭代器中至少存在一个整数。

**示例：**

<img alt="" src="https://assets.leetcode.com/uploads/2018/12/25/bst-tree.png" style="width: 189px; height: 178px;">

<pre>
<b>输入</b>
["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
[[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]
<b>输出</b>
[null, 3, 7, true, 9, true, 15, true, 20, false]

<b>解释</b>
BSTIterator bSTIterator = new BSTIterator([7, 3, 15, null, null, 9, 20]);
bSTIterator.next();    // 返回 3
bSTIterator.next();    // 返回 7
bSTIterator.hasNext(); // 返回 True
bSTIterator.next();    // 返回 9
bSTIterator.hasNext(); // 返回 True
bSTIterator.next();    // 返回 15
bSTIterator.hasNext(); // 返回 True
bSTIterator.next();    // 返回 20
bSTIterator.hasNext(); // 返回 False
</pre>

---

## 题解：显式栈模拟中序遍历（惰性展开）

### 1. 核心思路：BST 中序 = 升序

二叉搜索树的中序遍历（左 → 根 → 右）会按**从小到大**访问所有节点。迭代器每次 `next()` 要返回「尚未输出的下一个最小值」，等价于**可控的中序遍历**：每调用一次 `next()`，就再往前走一步。

用**栈**保存「从当前视角还要先走完的左链」，与手写非递归中序遍历相同：始终保证栈顶是**下一个该访问的节点**。

---

### 2. 执行逻辑详细拆解

#### A. 构造函数：沿左链入栈

Python

```
self.stack = []
while root:
    self.stack.append(root)
    root = root.left
```

- 从根开始一直向左走，把路径上的节点依次压栈。
- 栈顶是当前子树里中序第一个（最小）节点；左侧整条链已「预约」好，右子树暂不处理。

#### B. `next`：弹出下一个，再展开右子树的左链

Python

```
node = self.stack.pop()
ans = node.val
if node.right:
    node = node.right
    while node:
        self.stack.append(node)
        node = node.left
return ans
```

- 弹出栈顶，其值即为下一个最小数。
- 若该节点有右子树，则中序的下一批节点在右子树里；对右子树重复「一路向左压栈」，把右子树的中序起点接到栈上。
- 无右子树时栈里剩下的就是上层祖先中尚未访问的部分，无需额外操作。

#### C. `hasNext`：栈非空即仍有后继

Python

```
return len(self.stack) != 0
```

- 只要栈里还有节点，就说明还有未输出的中序节点。

---

### 3. 算法可视化

以示例树 `7, 3, 15, 9, 20` 为例，初始化后栈底到栈顶大致为 `[7, 3]`（3 在栈顶）。

1. `next`：弹出 `3`，无右子树 → 输出 `3`，栈顶变为 `7`。
2. `next`：弹出 `7`，有右子树 `15` → 沿 `15` 左链压入 `9`，输出 `7`。
3. 后续依次弹出 `9`、`15`、`20`，栈空则 `hasNext` 为假。

---

### 4. 复杂度分析

- **`next`**：摊还 **O(1)**。每个节点最多被压栈、弹栈各一次，$n$ 次 `next` 总计 **O(n)**。
- **`hasNext`**：**O(1)**。
- **空间**：栈中节点数不超过树高 **O(h)**，最坏链状树 **O(n)**。

---

### 5. 代码实现回顾

```python
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        node = self.stack.pop()
        ans = node.val
        if node.right:
            node = node.right
            while node:
                self.stack.append(node)
                node = node.left
        return ans

    def hasNext(self) -> bool:
        return len(self.stack) != 0
```
