## [92. 反转链表 II](https://leetcode.cn/problems/reverse-linked-list-ii/)

### 中等

给你单链表的头指针 `head` 和两个整数 `left` 和 `right` ，其中 `left <= right` 。请你反转从位置 `left` 到位置 `right` 的链表节点，返回 **反转后的链表** 。

**示例 1：**

<img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/rev2ex2.jpg" style="width: 542px; height: 222px;">

<pre><strong>输入：</strong>head = [1,2,3,4,5], left = 2, right = 4
<strong>输出：</strong>[1,4,3,2,5]
</pre>

---

## 题解：穿针引线 —— 链表局部反转算法

### 1. 核心思路：定位、反转、重连

反转链表的一部分比反转整个链表要复杂一些，因为你需要处理反转部分与原链表前后两端的**连接关系**。

你的代码采用了非常清晰的“三步走”策略：

1. **定位前驱节点 (`p0`)**：找到待反转部分的前一个节点。

2. **局部反转**：标准的双指针迭代法，反转从 `left` 到 `right` 的这一段。

3. **桥接重连**：将反转后的子链表重新接回到原链表中。

---

### 2. 执行逻辑拆解

#### A. 引入哑节点与定位

`p0 = dummy = ListNode(next=head)`

- **哑节点 (Dummy Node)**：处理 `left=1`（即从头开始反转）的边界情况。

- **定位 `p0`**：通过 `left - 1` 次循环，使 `p0` 指向反转区域的前一个节点。

#### B. 局部反转过程

这里使用了标准的双指针逻辑：

```python
pre = None
cur = p0.next
for _ in range(right - left + 1):
    nxt = cur.next
    cur.next = pre
    pre = cur
    cur = nxt
```

- **`pre`**：反转后的局部新头节点。

- **`cur`**：遍历到反转区域之外的第一个节点（即 `right` 之后的节点）。

- 在此循环结束后，`p0.next` 依然指向反转前的第一个节点（现在的最后一个节点），而 `pre` 指向反转后的第一个节点。

#### C. 关键的重连逻辑

这是代码最精华的部分，需要极强的空间想象力：

1. `p0.next.next = cur`：反转后的尾部（原 `left` 节点）指向反转区域后的剩余部分。

2. `p0.next = pre`：反转区域前的节点指向反转后的头部。

---

### 3. 算法可视化模拟

假设链表为 `1 -> 2 -> 3 -> 4 -> 5`，`left=2, right=4`：

1. **定位**：`p0` 指向节点 `1`。

2. **反转**：将 `2 -> 3 -> 4` 反转为 `4 -> 3 -> 2`。此时 `pre` 指向 `4`，`cur` 指向 `5`。

3. **重连**：
   
   - `p0.next` 还是节点 `2`。
   
   - 执行 `2.next = 5`（即 `p0.next.next = cur`）。
   
   - 执行 `1.next = 4`（即 `p0.next = pre`）。

4. **结果**：`1 -> 4 -> 3 -> 2 -> 5`。

---

### 4. 复杂度分析

- **时间复杂度**：$O(N)$。最坏情况下我们需要遍历整个链表（当 `right` 等于链表长度时）。

- **空间复杂度**：$O(1)$。只使用了有限的指针变量，是在原地修改链表结构。

---

### 5. 代码回顾

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        p0 = dummy = ListNode(next=head)
        for _ in range(left - 1):
            p0 = p0.next
        pre = None
        cur = p0.next
        for _ in range(right - left + 1):
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        p0.next.next = cur
        p0.next = pre
        return dummy.next
```