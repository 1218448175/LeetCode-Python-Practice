## [19. 删除链表的倒数第 N 个结点](https://leetcode.cn/problems/remove-nth-node-from-end-of-list/)

### 中等

给你一个链表，删除链表的倒数第 `n` 个结点，并且返回链表的头结点。

**示例 1：**

<img alt="" src="https://assets.leetcode.com/uploads/2020/10/03/remove_ex1.jpg" style="width: 542px; height: 222px;">

<pre><strong>输入：</strong>head = [1,2,3,4,5], n = 2
<strong>输出：</strong>[1,2,3,5]
</pre>

---

## 题解：快慢指针的一次遍历定位法

### 1. 核心思路：双指针的“间距固定”法

要在一次遍历中找到倒数第 $n$ 个节点，最巧妙的方法是利用两个指针维护一个**固定距离**。

你的代码采用了 **“快慢指针 (Fast/Slow Pointers)”** 策略：

- **哑节点 (Dummy Node)**：设置一个虚拟头节点 `dummy` 指向 `head`。这不仅能简化删除头节点的逻辑（如链表只有 1 个节点或删除的是第一个节点），还能让 `pre` 指针最终停在待删除节点的前驱位置。

- **拉开间距**：让快指针 `last` 先走 $n$ 步。

- **同步移动**：当快指针 `last` 领先 $n$ 步后，慢指针 `pre` 开始从 `dummy` 出发。当 `last` 走到链表末尾（`None`）时，`pre` 恰好指向倒数第 $n$ 个节点的前一个位置。

---

### 2. 执行逻辑的详细拆解

#### A. 初始化与快指针先行

```python
dummy = ListNode(next=head)
pre, last = dummy, head
for _ in range(n):
    last = last.next
```

- `last` 先向后移动 $n$ 次。此时 `last` 与 `head` 之间的距离为 $n$，而相对于 `dummy` 的距离为 $n+1$。

#### B. 保持间距同步平移

```python
while last:
    pre = pre.next
    last = last.next
```

- 当 `last` 移动到链表末尾的 `None` 时，`pre` 移动了 `L - n` 次（$L$ 为链表长度）。

- 此时 `pre` 停留在正数第 `L - n` 个节点，即**倒数第 $n+1$ 个节点**（待删除节点的前驱）。

#### C. 删除操作

```python
pre.next = pre.next.next
```

- 直接跳过倒数第 $n$ 个节点，将其前驱与后继相连。由于 Python 的垃圾回收机制，被跳过的节点会被自动释放。

---

### 3. 算法可视化

以 `head = [1, 2, 3, 4, 5], n = 2` 为例：

| **步骤**  | **说明**                 | **指针位置**                      |
| ------- | ---------------------- | ----------------------------- |
| **初始化** | 建立 `dummy`             | `pre` 在 `dummy`, `last` 在 `1` |
| **先行步** | `last` 走 2 步           | `pre` 在 `dummy`, `last` 在 `3` |
| **同步移** | 移动直到 `last` 为空         | `pre` 停在 `3`, `last` 为 `None` |
| **删除**  | `3.next = 3.next.next` | 节点 `4` 被删除，`3` 连接 `5`         |

---

### 4. 复杂度分析

- **时间复杂度**：$O(L)$。其中 $L$ 为链表长度。虽然代码中有两个循环，但实质上每个节点只被访问了一次。

- **空间复杂度**：$O(1)$。只额外使用了 `dummy`, `pre`, `last` 常数个指针变量。

---

### 5. 代码回顾

```python
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 1. 哑节点处理边界（如删除头节点）
        dummy = ListNode(next=head)
        pre, last = dummy, head

        # 2. 快指针先走 n 步，建立宽度为 n 的窗口
        for _ in range(n):
            last = last.next

        # 3. 两个指针同时移动，直到快指针超出边界
        while last:
            pre = pre.next
            last = last.next

        # 4. 此时 pre 指向待删除节点的前驱，执行删除
        pre.next = pre.next.next

        return dummy.next
```