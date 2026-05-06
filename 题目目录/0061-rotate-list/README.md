## [61. 旋转链表](https://leetcode.cn/problems/rotate-list/)

### 中等

给你一个链表的头节点 `head` ，旋转链表，将链表每个节点向右移动 `k` 个位置。

**示例 1：**

<img alt="" src="https://assets.leetcode.com/uploads/2020/11/13/rotate1.jpg" style="width: 450px;">

<pre><strong>输入：</strong>head = [1,2,3,4,5], k = 2
<strong>输出：</strong>[4,5,1,2,3]
</pre>

---

## 题解：成环与断开 —— 链表旋转的闭环策略

### 1. 核心思路：将链表连成环

“旋转链表”实质上是改变链表的**头尾位置**。将每个节点向右移动 $k$ 个位置，等价于将链表的后 $k \pmod n$ 个节点移到前面。

你的代码采用了非常直观且高效的 **“成环断开法”**：

- **计算长度并找尾部**：首先遍历一遍链表，统计长度 `list_len`，同时让指针 `q` 停在最后一个节点上。

- **闭合成环**：让原尾节点的 `next` 指向原头节点 `head`。此时链表变成了一个环。

- **寻找新断点**：旋转 $k$ 次后，新的头节点应该是原链表的第 `list_len - (k % list_len)` 个节点。

- **断开环**：找到新的尾节点，将其 `next` 置为空，并返回新的头节点。

---

### 2. 执行逻辑拆解

#### A. 统计长度与初步成环

Python

```
while q.next:
    q = q.next
    list_len += 1
q.next = head
```

- 这部分逻辑不仅拿到了链表的总长度，还让 `q` 引用了最后一个节点。

- `q.next = head` 直接将线性链表构造成了一个循环链表。

#### B. 处理旋转步数

Python

```
if list_len == 0: return head
step = k % list_len
```

- **取模运算**：旋转次数 $k$ 可能远大于链表长度。$k \pmod{list\_len}$ 才是实际需要移动的有效步数。

- **边界处理**：如果链表为空（`list_len == 0`），直接返回。

#### C. 寻找新位并断开

Python

```
for _ in range(list_len - step):
    head = head.next
    q = q.next
q.next = None
```

- **同步移动**：在循环链表中，`head` 和 `q`（尾指针）同时向前移动。

- 当移动 `list_len - step` 次后，`head` 恰好落在了新链表的起始位置，而 `q` 落在了新链表的末尾。

- `q.next = None` 斩断循环，恢复线性结构。

---

### 3. 算法可视化

假设链表为 `1 -> 2 -> 3 -> 4 -> 5`，`k = 2`：

1. **初始长度**：`list_len = 5`，`q` 指向 `5`。

2. **连成环**：`5.next = 1`，形成 `1->2->3->4->5->(回到1)`。

3. **计算位移**：实际移动步数 $5 - (2 \pmod 5) = 3$ 步。

4. **寻找新断点**：
   
   - `head` 和 `q` 从初始位置移动 3 步。
   
   - `head` 最终指向 `4`（新头）。
   
   - `q` 最终指向 `3`（新尾）。

5. **断开**：`3.next = None`。结果为 `4 -> 5 -> 1 -> 2 -> 3`。

---

### 4. 复杂度分析

- **时间复杂度**：$O(N)$。第一次遍历获取长度 $O(N)$，第二次寻找断点最多 $O(N)$。

- **空间复杂度**：$O(1)$。只修改了指针指向，没有开辟新空间。

---

### 5. 代码回顾

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        q = dummy
        list_len = 0
        while q.next:
            q = q.next
            list_len += 1
        q.next = head
        if list_len == 0:
            return head
        step = k % list_len
        for _ in range(list_len - step):
            head = head.next
            q = q.next
        q.next = None
        return head
        
```

# 