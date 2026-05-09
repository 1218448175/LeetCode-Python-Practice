## [117. 填充每个节点的下一个右侧节点指针 II](https://leetcode.cn/problems/populating-next-right-pointers-in-each-node-ii/)

### 中等

给定一个二叉树：

> struct Node {
>   int val;
>   Node *left;
>   Node *right;
>   Node *next;
> }

填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 `NULL` 。

初始状态下，所有 next 指针都被设置为 `NULL` 。

**示例 1：**

<img alt="" src="https://assets.leetcode.com/uploads/2019/02/15/117_sample.png" style="width: 500px; height: 171px;">

<pre><strong>输入</strong>：root = [1,2,3,4,5,null,7]
<strong>输出：</strong>[1,#,2,3,#,4,5,7,#]
<strong>解释：</strong>给定二叉树如图 A 所示，你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点，如图 B 所示。序列化输出按层序遍历顺序（由 next 指针连接），'#' 表示每层的末尾。</pre>

---

## 题解：利用已建立的 `next` 指针实现 $O(1)$ 空间层序遍历

### 1. 核心思路：把每一层看作一个单链表

这道题是“填充每个节点的下一个右侧节点指针 I”的进阶版。在第 I 题中树是完美二叉树，而本题是**任意二叉树**。

你的代码采用了一种极其巧妙的思路：**利用当前层已经建立好的 `next` 指针，来构建下一层的 `next` 指针。**

- **空间优化**：传统的层序遍历需要使用队列（$O(N)$ 空间），但通过 `next` 指针，我们可以像遍历单链表一样遍历当前层，从而将空间复杂度降至 **$O(1)$**。

- **虚拟链表思想**：在处理每一层时，引入 `last` 指针记录下一层最新找到的节点，并用 `next_start` 记录下一层的第一个节点。

---

### 2. 执行逻辑详细拆解

#### A. 辅助函数 `handle(p)`

这个函数的作用是将下一层的节点“串起来”：

1. **连接操作**：如果 `last` 存在，说明之前已经找到了下一层的某个节点，于是执行 `last.next = p`。

2. **记录起点**：如果 `next_start` 为空，说明 `p` 是下一层的第一个节点，记录下来供主循环切换层级使用。

3. **指针后移**：更新 `last = p`，为连接下一个节点做准备。

#### B. 主循环逻辑 `connect`

1. **外层循环 (`while start`)**：负责层与层之间的切换。每次循环开始时，重置下一层的起始点和末尾记录指针。

2. **内层循环 (`while p`)**：负责在当前层“横向移动”。
   
   - 通过 `p.next` 访问当前层的下一个节点。
   
   - 依次检查当前节点的左、右孩子，并调用 `handle` 进行连接。

3. **层级跳转**：当前层处理完后，`start = self.next_start` 直接跳到下一层的开头。

---

### 3. 算法可视化

假设当前层是第 $i$ 层，节点已经通过 `next` 连好了：

- 我们遍历第 $i$ 层。

- 当我们看到节点 `A` 有左孩子 `L1` 和右孩子 `R1` 时，`handle` 会把它们连成 `L1 -> R1`。

- 当我们通过 `A.next` 移到节点 `B` 且它有左孩子 `L2` 时，`handle` 会把之前的 `R1` 连向 `L2`，变成 `L1 -> R1 -> L2`。

---

### 4. 复杂度分析

- **时间复杂度**：$O(N)$。每个节点只被访问一次。

- **空间复杂度**：$O(1)$。除了递归调用（本题是迭代实现）外，只使用了常数个指针变量。

---

### 5. 代码实现回顾

```python
class Solution:
    def handle(self, p):
        # 如果当前层已经有了前驱节点，则连接
        if self.last:
            self.last.next = p
        # 记录下一层的起始节点
        if not self.next_start:
            self.next_start = p
        # 更新上一节点指针
        self.last = p

    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None

        start = root
        while start:
            self.last = None
            self.next_start = None
            p = start # p 在当前层移动
            while p:
                if p.left:
                    self.handle(p.left)
                if p.right:
                    self.handle(p.right)
                p = p.next # 利用已经建好的 next 指针横向移动
            # 切换到下一层
            start = self.next_start

        return root
```