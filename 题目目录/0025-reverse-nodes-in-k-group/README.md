## [25. K 个一组翻转链表](https://leetcode.cn/problems/reverse-nodes-in-k-group/)

### 困难

给你链表的头节点 `head` ，每 `k` 个节点一组进行翻转，请你返回修改后的链表。

`k` 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 `k` 的整数倍，那么请将最后剩余的节点保持原有顺序。

你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。

**示例 1：**

<img alt="" src="https://assets.leetcode.com/uploads/2020/10/03/reverse_ex1.jpg" style="width: 542px; height: 222px;">

<pre><strong>输入：</strong>head = [1,2,3,4,5], k = 2
<strong>输出：</strong>[2,1,4,3,5]
</pre>

---

## 题解：分组迭代与局部反转

### 1. 核心思路：分治与衔接

这道题是链表反转系列中的“终极挑战”。它的难点在于：**不仅要反转每一个大小为 $k$ 的小组，还要确保这些小组之间、以及小组与剩余未反转部分能够正确连接。**

你的代码采用了一种非常模块化的**分治解法**：

- **子问题拆解**：编写一个专门的 `reverse` 函数，负责翻转一个闭区间内的节点。

- **长度检查**：在翻转每一组前，先探测后续是否还有 $k$ 个节点。如果不足，则按题目要求保持原样。

- **指针接力**：使用一个 `pre` 指针始终指向“已翻转部分的尾部”，它是连接下一组新头部的“钩子”。

---

### 2. 执行逻辑的详细拆解

#### A. 局部翻转函数 `reverse(head, tail)`

这是一个针对区间设计的变体：

- **初始化**：`pre = tail.next`。这是一个极佳的设计，直接让翻转后的局部尾部（原 `head`）预先连接到了下一组的起始位置。

- **循环终止**：`while pre != tail`。当 `pre` 移动到原先的 `tail` 位置时，意味着该组内的 $k$ 个指针已全部完成反向。

- **返回值**：返回翻转后的新头（原 `tail`）和新尾（原 `head`），方便主函数更新指针。

#### B. 主循环控制 `reverseKGroup`

1. **哑节点 (Dummy Node)**：`dummy = ListNode(next=head)`。用于处理头节点可能被翻转的情况，确保最终能找到链表新起点。

2. **区间探测**：
   
   - 使用 `for i in range(k)` 尝试寻找当前组的末尾 `tail`。
   
   - **边界处理**：如果 `if not tail`，说明剩余节点不足 $k$ 个，直接返回 `dummy.next`，不再翻转。

3. **断开与衔接**：
   
   - 调用 `reverse` 函数获取翻转后的结果。
   
   - `pre.next = head`：将上一组的末端指向本组的新头。
   
   - `pre = tail`：移动 `pre` 指针，将当前组的末端作为下一组的前驱。
   
   - `head = tail.next`：更新 `head`，开启下一组的探测。

---

### 3. 算法可视化

以链表 `1->2->3->4->5`, `k=2` 为例：

| **步骤**     | **当前探测区间** | **翻转后局部形态** | **衔接后的链表状态**                          |
| ---------- | ---------- | ----------- | ------------------------------------- |
| **Step 1** | `[1, 2]`   | `2 -> 1`    | `dummy -> 2 -> 1 -> (3...)`           |
| **Step 2** | `[3, 4]`   | `4 -> 3`    | `dummy -> 2 -> 1 -> 4 -> 3 -> (5...)` |
| **Step 3** | `[5]`      | 不足 $k$ 个    | **结束返回**                              |

---

### 4. 复杂度分析

- **时间复杂度**：$O(N)$。虽然代码中有嵌套循环，但每个节点实际上只被访问了两次：一次是 `tail` 指针探测长度，一次是 `reverse` 函数进行指针反转。

- **空间复杂度**：$O(1)$。只使用了常数个额外的指针变量（`pre`, `nxt`, `head`, `tail`），属于原地修改。

---

### 5. 代码回顾

```python
class Solution:
    # 局部翻转：将 [head, tail] 区间内的节点反转
    def reverse(self, head: ListNode, tail: ListNode):
        pre = tail.next
        cur = head
        while pre != tail:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return tail, head

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        pre = dummy # pre 始终指向待翻转小组的前一个节点

        while head:
            tail = pre
            # 1. 查看剩余部分长度是否大于等于 k
            for i in range(k):
                tail = tail.next
                if not tail:
                    return dummy.next

            nxt = tail.next # 记录下一组的起点
            # 2. 翻转当前小组
            head, tail = self.reverse(head, tail)
            # 3. 将翻转后的子链表接回原链表
            pre.next = head
            tail.next = nxt
            # 4. 指针接力，准备下一组翻转
            pre = tail
            head = tail.next

        return dummy.next
```