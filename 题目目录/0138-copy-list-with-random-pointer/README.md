## [138. 随机链表的复制](https://leetcode.cn/problems/copy-list-with-random-pointer/)

### 中等

给你一个长度为 `n` 的链表，每个节点包含一个额外增加的随机指针 `random` ，该指针可以指向链表中的任何节点或空节点。

构造这个链表的 **[深拷贝](https://baike.baidu.com/item/%E6%B7%B1%E6%8B%B7%E8%B4%9D/22785317?fr=aladdin)**。 深拷贝应该正好由 `n` 个 **全新** 节点组成，其中每个新节点的值都设为其对应的原节点的值。新节点的 `next` 指针和 `random` 指针也都应指向复制链表中的新节点，并使原链表和复制链表中的这些指针能够表示相同的链表状态。**复制链表中的指针都不应指向原链表中的节点** 。

例如，如果原链表中有 `X` 和 `Y` 两个节点，其中 `X.random --> Y` 。那么在复制链表中对应的两个节点 `x` 和 `y` ，同样有 `x.random --> y` 。

返回复制链表的头节点。

用一个由 `n` 个节点组成的链表来表示输入/输出中的链表。每个节点用一个 `[val, random_index]` 表示：

- `val`：一个表示 `Node.val` 的整数。
- `random_index`：随机指针指向的节点索引（范围从 `0` 到 `n-1`）；如果不指向任何节点，则为  `null` 。

你的代码 **只** 接受原链表的头节点 `head` 作为传入参数。

**示例 1：**

<p><img alt="" src="https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/01/09/e1.png" style="height: 142px; width: 700px;"></p>

<pre><strong>输入：</strong>head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
<strong>输出：</strong>[[7,null],[13,0],[11,4],[10,2],[1,0]]
</pre>

---

## 题解：三步走原链表交织法（空间 $O(1)$ 深拷贝）

### 1. 核心思路：通过“交织”建立映射关系

深拷贝带 `random` 指针链表的难点在于：当你复制节点 A 时，它指向的 `random` 节点 B 可能还没有被创建。

你的代码采用了一种非常精妙的算法，不需要额外的哈希表（Hash Map）来存储原节点与新节点的映射关系，而是直接将新节点**插在原节点的后面**。这种“交织”法将空间复杂度从 $O(N)$ 降低到了 $O(1)$（不计结果链表）。

---

### 2. 执行逻辑拆解：三步走策略

#### 第一步：复制节点并交织

Python

```
while q:
    copy_node = Node(q.val, q.next)
    q.next = copy_node
    q = copy_node.next
```

- **动作**：遍历原链表，为每个节点 A 创建一个拷贝 A'，并将 A' 插入 A 和 A.next 之间。

- **状态**：链表变成了 `A -> A' -> B -> B' -> C -> C' -> None`。

#### 第二步：设置拷贝节点的 `random` 指针

Python

```
while q:
    q.next.random = q.random.next if q.random else None
    q = q.next.next
```

- **核心逻辑**：由于新节点 A' 紧跟在原节点 A 后面，那么 A' 应该指向的 `random` 节点（即 A.random 的拷贝），一定也紧跟在 A.random 的后面。

- **即**：`A.next.random = A.random.next`。

- 这是整个算法最聪明的地方，它利用物理位置关系取代了哈希表的查找。

#### 第三步：拆分链表

Python

```
while q:
    p.next = q.next
    p = p.next
    q = q.next.next
```

- **动作**：将“交织”在一起的链表拆开，恢复原链表的结构，并提取出拷贝链表。

- **注意**：虽然你的代码在逻辑上提取了 `p`，但在严谨的面试场景下，最好也把原链表的 `q.next` 重新接好（即 `q.next = q.next.next`），以保证不破坏输入的原始数据。

---

### 3. 复杂度分析

- **时间复杂度**：$O(N)$。我们一共对链表进行了三次线性扫描（复制、赋 `random`、拆分）。

- **空间复杂度**：$O(1)$。除了存储拷贝结果所需的节点外，我们只使用了常数个指针变量。

---

### 4. 代码回顾

```python
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        q = head
        while q:
            copy_node = Node(q.val, q.next)
            q.next = copy_node
            q = copy_node.next
        q = head
        while q:
            q.next.random = q.random.next if q.random else None
            q = q.next.next
        dummy = Node(0)
        p = dummy
        q = head
        while q:
            p.next = q.next
            p = p.next
            q = q.next.next
        return dummy.next
```