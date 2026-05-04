## [21. 合并两个有序链表](https://leetcode.cn/problems/merge-two-sorted-lists/)

### 中等

将两个升序链表合并为一个新的 **升序** 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

**示例 1：**

<img alt="" src="https://assets.leetcode.com/uploads/2020/10/03/merge_ex1.jpg" style="width: 662px; height: 302px;">

<pre><strong>输入：</strong>l1 = [1,2,4], l2 = [1,3,4]
<strong>输出：</strong>[1,1,2,3,4,4]
</pre>

---

## 题解：迭代法合并有序链表

### 1. 核心思路：双指针归并排序思想

合并两个有序链表的过程，就像是两个排好队的队伍合并成一个。我们只需要对比两个队伍最前面的人，谁更小就让谁先进入新队伍。

你的代码采用了**迭代法**，配合哑节点（Dummy Node）技巧，逻辑非常清晰：

- **哑节点 (`head`)**：作为结果链表的哨兵，避免了处理“第一个节点是谁”的逻辑，使代码统一化。

- **比较与拼接**：使用 `q` 指针不断移动，将 `list1` 和 `list2` 中较小的节点接到 `q` 的后面。

- **尾部处理**：当其中一个链表走完时，另一个链表剩下的部分由于原本就有序，直接整体挂载到新链表的末尾即可。

---

### 2. 执行逻辑拆解

#### A. 准备阶段

- `head = ListNode()`：创建一个虚拟头节点。

- `q = head`：`q` 是结果链表的末尾指针。

#### B. 核心循环（拉链式合并）

`while list1 and list2:`

- **逻辑判定**：如果 `list1.val <= list2.val`，说明 `list1` 的当前节点更小。
  
  - `q.next = list1`：把小节点接过去。
  
  - `list1 = list1.next`：`list1` 指针后移。

- 反之则对 `list2` 执行相同操作。

- `q = q.next`：每合并一个节点，结果链表的尾部指针 `q` 都要向后移动一位。

#### C. 收尾阶段

`q.next = list1 if list1 else list2`

- 由于循环条件是 `list1 and list2`，当循环结束时，意味着至少有一个链表已经空了。

- 如果 `list1` 还没走完，直接把剩下的 `list1` 全部接在 `q` 后面；否则接 `list2`。

---

### 3. 复杂度分析

- **时间复杂度**：$O(M + N)$。其中 $M$ 和 $N$ 分别是两个链表的长度。我们最多只需要遍历两个链表的所有节点一次。

- **空间复杂度**：$O(1)$。我们只是在修改节点之间的 `next` 指向（拼接），并没有创建新的节点（除了哑节点），因此只需要常数级别的额外空间。

---

### 4. 代码回顾

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        q = head
        while list1 and list2:
            if list1.val <= list2.val:
                q.next = list1
                list1 = list1.next
            else:
                q.next = list2
                list2 = list2.next
            q = q.next
        q.next = list1 if list1 else list2
        return head.next
        
```