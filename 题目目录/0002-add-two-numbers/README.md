## [2. 两数相加](https://leetcode.cn/problems/add-two-numbers/)

### 中等

给你两个 **非空** 的链表，表示两个非负的整数。它们每位数字都是按照 **逆序** 的方式存储的，并且每个节点只能存储 **一位** 数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

**示例 1：**

<img alt="" src="https://assets.leetcode.cn/aliyun-lc-upload/uploads/2021/01/02/addtwonumber1.jpg" style="width: 483px; height: 342px;">

<pre><strong>输入：</strong>l1 = [2,4,3], l2 = [5,6,4]
<strong>输出：</strong>[7,0,8]
<strong>解释：</strong>342 + 465 = 807.
</pre>

---

## 题解：链表模拟竖式加法

这段精简代码的核心在于**模拟人类手工计算加法**的过程：从低位开始相加，处理进位，并逐位向高位推进。

### 1. 核心设计思想

- **哑节点 (Dummy Node)**：使用 `dummy` 节点作为结果链表的起点。这是一个常用的链表技巧，它可以让我们在不知道头节点具体值的情况下，统一地通过 `curr.next` 来构建链表，最后只需返回 `dummy.next` 即可。

- **统一循环条件**：将 `carry`（进位）也加入 `while` 循环条件中。这样做的好处是，当 `l1` 和 `l2` 都遍历完但最后还有一个进位时（例如 $99 + 1$），循环会自动多跑一轮来处理最高位的进位，代码更简洁。

- **空值补偿策略**：在遍历时，如果某个链表较短已经结束，我们通过 `if-else` 将其取值视为 `0`。这实现了对不等长数字相加的完美兼容。

---

### 2. 执行逻辑拆解

1. **初始化**：
   
   - `dummy`：结果链表的“哨兵”。
   
   - `curr`：指向当前已经处理好的最后一个节点。
   
   - `carry`：存储进位，初始为 $0$。

2. **迭代累加**：
   
   - 获取当前位的值：`v1` 来自 `l1`，`v2` 来自 `l2`。如果指针已空，则取 $0$。
   
   - 计算当前位总和：$Total = v1 + v2 + carry$。
   
   - 更新进位：$carry = Total // 10$（取整）。
   
   - 创建新位：结果链表的新节点值为 $Total \% 10$（取余）。

3. **指针移动**：
   
   - 结果链表指针 `curr` 向后移。
   
   - 输入链表 `l1` 和 `l2` 若不为空则向后移。

4. **返回结果**：
   
   - 返回 `dummy.next`，即跳过哨兵节点，返回真正存储数字的链表头。

---

### 3. 复杂度分析

- **时间复杂度：$O(\max(M, N))$**
  
  其中 $M$ 和 $N$ 是两个链表的长度。我们必须遍历完最长的那个链表，每个节点的操作（加法、取模、创建节点）都是 $O(1)$ 的。

- **空间复杂度：$O(\max(M, N))$**
  
  新链表的长度最多为 $\max(M, N) + 1$。这是存储结果所必须消耗的空间。

---

### 4. 代码实现回顾

```python
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        carry = 0

        # 只要还有数没加完，或者还有进位没处理，就继续
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # 核心计算：当前和 = 左值 + 右值 + 进位
            total = v1 + v2 + carry
            carry = total // 10        # 更新下一次的进位

            # 将当前位的余数存入新节点
            curr.next = ListNode(total % 10)
            curr = curr.next

            # 移动原链表指针
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy.next
```