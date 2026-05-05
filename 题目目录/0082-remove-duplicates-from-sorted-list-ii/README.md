## [82. 删除排序链表中的重复元素 II](https://leetcode.cn/problems/remove-duplicates-from-sorted-list-ii/)

### 中等

给定一个已排序的链表的头 `head` ， *删除原始链表中所有重复数字的节点，只留下不同的数字* 。返回 *已排序的链表* 。

**示例 1：**

<img alt="" src="https://assets.leetcode.com/uploads/2021/01/04/linkedlist1.jpg" style="height: 142px; width: 500px;">

<pre><strong>输入：</strong>head = [1,2,3,3,4,4,5]
<strong>输出：</strong>[1,2,5]
</pre>

---

## 题解：跳跃式删除——彻底清除重复节点

### 1. 核心思路：前驱指针与区域清扫

这道题与“删除排序链表中的重复元素 I”不同，要求是**只要重复，一个不留**。因此，我们不能简单地保留第一个重复节点，而是必须将整块重复区域彻底切断。

你的代码采用了 **“哑节点 + 双指针”** 的逻辑：

- **哑节点 (`dummy`)**：用于处理头节点就被删除的情况。

- **前驱指针 (`pre`)**：始终指向“已确定保留的最后一个节点”。

- **当前指针 (`cur`)**：用于探测和跨越重复区间。

---

### 2. 执行逻辑的详细拆解

#### A. 探测重复区间

`if cur.next and cur.next.val == cur.val:`

- 当发现当前节点与下一个节点值相同时，进入“清扫模式”。

- 内部 `while` 循环：`cur.next = cur.next.next`。这一步非常巧妙，它不断地把重复的后继节点剔除，直到 `cur.next` 不再等于 `cur.val`。

#### B. 彻底切断

`pre.next = cur.next`

- 注意：此时 `cur` 仍然是一个重复过的节点。通过将 `pre.next` 直接指向 `cur.next`，我们跳过了**所有**包含 `cur.val` 的节点。

- **关键点**：在这种情况下，`pre` 指针**不移动**。因为新接上来的 `cur.next` 依然可能是一个重复节点的开头，需要留在原地继续观察。

#### C. 保留唯一节点

`else: pre = cur; cur = cur.next`

- 如果没有发现重复，说明 `cur` 是安全的。此时才放心地将 `pre` 向后移动。

---

### 3. 算法可视化

以 `head = [1, 2, 3, 3, 4]` 为例：

1. `cur` 在 `1`，不重复：`pre` 移到 `1`，`cur` 移到 `2`。

2. `cur` 在 `2`，不重复：`pre` 移到 `2`，`cur` 移到 `3`。

3. `cur` 在 `3`，发现 `3.next` 也是 `3`：
   
   - 内部循环把第二个 `3` 删掉。
   
   - 执行 `pre.next = cur.next`（即 `2.next = 4`）。
   
   - 此时 `pre` 还在 `2`，`cur` 跳到了 `4`。

4. 最终结果：`1 -> 2 -> 4`。

---

### 4. 复杂度分析

- **时间复杂度**：$O(N)$。每个节点最多被访问两次（一次由 `cur` 指针探测，一次在重复块中被跳过）。

- **空间复杂度**：$O(1)$。原地修改指针，只使用了常数个额外变量。

---

### 5. 代码实现回顾

```py
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 1. 哑节点，val 设为范围外的 101 防止干扰判断
        dummy = ListNode(val=101, next=head)
        pre, cur = dummy, head

        while cur:
            # 2. 发现重复区域的起点
            if cur.next and cur.next.val == cur.val:
                # 3. 将后续重复的节点一个个“跳过”
                while cur.next and cur.next.val == cur.val:
                    cur.next = cur.next.next
                # 4. 此时 cur 也是重复值，pre.next 指向 cur.next 彻底删除该数值
                pre.next = cur.next
                cur = cur.next
            else:
                # 5. 无重复，pre 指针才前移
                pre = cur
                cur = cur.next

        return dummy.next
```