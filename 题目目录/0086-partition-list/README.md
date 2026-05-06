## [86. 分隔链表](https://leetcode.cn/problems/partition-list/)

### 中等

给你一个链表的头节点 `head` 和一个特定值 `x` ，请你对链表进行分隔，使得所有 **小于** `x` 的节点都出现在 **大于或等于** `x` 的节点之前。

你应当 **保留** 两个分区中每个节点的初始相对位置。

**示例 1：**

<img alt="" src="https://assets.leetcode.com/uploads/2021/01/04/partition.jpg" style="width: 662px; height: 222px;">

<pre><strong>输入：</strong>head = [1,4,3,2,5,2], x = 3
<strong>输出</strong>：[1,2,2,4,3,5]
</pre>

---

## 题解：双哑节点分流法

### 1. 核心思路：分而治之，合二为一

这道题要求在不改变节点相对顺序的前提下，按照特定值 $x$ 将链表“分隔”开。最直观且高效的方法是：**将原链表拆分成两个独立的子链表，最后再把它们首尾相连。**

你的代码完美体现了这种 **“分流”** 思想：

- **小链表 (`small`)**：专门收集所有值 **小于** $x$ 的节点。

- **大链表 (`large`)**：专门收集所有值 **大于或等于** $x$ 的节点。

- **双指针移动**：使用 `small_q` 和 `large_q` 分别作为两个新链表的末尾指针，负责“挂载”新发现的符合条件的节点。

---

### 2. 执行逻辑的详细拆解

#### A. 初始化哑节点

Python

```
small = ListNode()
large = ListNode()
small_q = small
large_q = large
```

- 使用两个哑节点作为哨兵，可以避免在循环中不断判断“子链表是否为空”，让插入逻辑高度统一。

#### B. 遍历与断链

Python

```
while head:
    if head.val < x:
        small_q.next = head
        small_q = small_q.next
        head = head.next
        small_q.next = None  # 关键：手动断开原有的连接
    else:
        # 对 large 链表执行相同操作
```

- **断链的重要性**：在将 `head` 挂载到新链表后，你的代码通过 `small_q.next = None` 立即切断了该节点在原链表中的后续指向。这是一个非常稳健的做法，能够有效防止最终合并后的链表产生环路（Cycle）。

#### C. 合并链表

Python

```
small_q.next = large.next
return small.next
```

- 最后一步将 `small` 链表的尾部指向 `large` 链表的首部（跳过 `large` 的哑节点）。

- 返回 `small.next` 作为最终结果。

---

### 3. 算法可视化

假设链表为 `1 -> 4 -> 3 -> 2`, $x = 3$：

1. **节点 1** ($< 3$): 挂载到 `small` -> `small: 1`

2. **节点 4** ($\ge 3$): 挂载到 `large` -> `large: 4`

3. **节点 3** ($\ge 3$): 挂载到 `large` -> `large: 4 -> 3`

4. **节点 2** ($< 3$): 挂载到 `small` -> `small: 1 -> 2`

5. **合并**: `small(1->2)` + `large(4->3)` -> `1 -> 2 -> 4 -> 3`

---

### 4. 复杂度分析

- **时间复杂度**：$O(N)$。只需对原链表进行一次完整的线性扫描。

- **空间复杂度**：$O(1)$。虽然我们创建了两个哑节点，但除此之外只是在修改节点之间的 `next` 指针指向，并没有创建与 $N$ 等比例的新节点空间。

---

### 5. 代码实现回顾

```python
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # 1. 初始化两个区域的哑节点
        small = ListNode()
        large = ListNode()
        small_q = small
        large_q = large

        while head:
            if head.val < x:
                # 2. 属于小区
                small_q.next = head
                small_q = small_q.next
                head = head.next
                small_q.next = None # 断开原有连接，保证安全
            else:
                # 3. 属于大区
                large_q.next = head
                large_q = large_q.next
                head = head.next
                large_q.next = None

        # 4. 首尾相连
        small_q.next = large.next

        return small.next
```