## [23. 合并 K 个升序链表](https://leetcode.cn/problems/merge-k-sorted-lists/)

### 困难

给你一个链表数组，每个链表都已按升序排列。请你将所有链表合并到一个升序链表中，并返回合并后的链表。

**示例 1：**

```
输入：lists = [[1,4,5],[1,3,4],[2,6]]
输出：[1,1,2,3,4,4,5,6]
```

**示例 2：**

```
输入：lists = []
输出：[]
```

**示例 3：**

```
输入：lists = [[]]
输出：[]
```

---

## 题解：分治两两归并（锦标赛合并）

### 1. 核心思路：每轮减半，两两合并

将 $k$ 条升序链表 **两两配对**，用 `merge2List` 合并为一条，得到至多 $\lceil k/2 \rceil$ 条新链表，再 **递归** 处理下一轮，直到只剩一条：

1. **递归基准**：`n == 0` 返回 `None`；`n == 1` 直接返回 `lists[0]`。
2. **分治一轮**：`for i in range(0, n, 2)`，合并 `lists[i]` 与 `lists[i+1]`，结果放入 `nxt_lists`。
3. **奇数条处理**：若 $k$ 为奇数，最后一条无配对，原样 `append(lists[-1])` 进入下一轮。
4. **递归合并**：`return self.mergeKLists(nxt_lists)`。

与 [148. 排序链表](../0148-sort-list) 同属 **分治归并**：148 在单链表内找中点拆半再归并；本题在 **多条链表** 上每轮两两归并，层数 $O(\log k)$。

---

### 2. 执行逻辑拆解

#### A. 二路归并 `merge2List`

```python
dummy = ListNode()
cur = dummy
while r and l:
    if r.val <= l.val:
        cur.next = r
        r = r.next
    else:
        cur.next = l
        l = l.next
    cur = cur.next
cur.next = r if r else l
return dummy.next
```

- 哑节点 `dummy` 简化头结点处理。
- 双指针比较 `r.val` 与 `l.val`，较小者接到 `cur.next`，某一侧耗尽后接上另一侧剩余链。

#### B. 分治一轮

```python
nxt_lists = []
for i in range(0, n, 2):
    if i + 1 == n:
        break
    nxt_lists.append(merge2List(lists[i], lists[i + 1]))
if n % 2 != 0:
    nxt_lists.append(lists[-1])
return self.mergeKLists(nxt_lists)
```

- 每轮链表条数约减半，总轮数 $O(\log k)$。
- 奇数条时最后一条直接进入下一轮，避免丢失。

---

### 3. 算法可视化

以 `lists = [1→4→5, 1→3→4, 2→6]` 为例：

1. **第一轮**：合并前两条得 `1→1→3→4→4→5`，第三条 `2→6` 因奇数直接保留 → `nxt_lists` 长度为 2。
2. **第二轮**：两路归并 → `1→1→2→3→4→4→5→6`。
3. **第三轮**：`n == 1`，返回结果。

---

### 4. 复杂度分析

- **时间复杂度**：$O(N \log k)$。$N$ 为所有结点总数，$k$ 为链表条数；每轮归并遍历当前全部结点，共 $O(\log k)$ 轮。
- **空间复杂度**：$O(\log k)$ 递归栈；归并过程仅使用指针，无额外数组。

---

### 5. 代码实现回顾

```python
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge2List(l, r):
            dummy = ListNode()
            cur = dummy
            while r and l:
                if r.val <= l.val:
                    cur.next = r
                    r = r.next
                else:
                    cur.next = l
                    l = l.next
                cur = cur.next
            cur.next = r if r else l
            return dummy.next

        n = len(lists)
        if n == 0:
            return None
        if n == 1:
            return lists[0]
        nxt_lists = []
        for i in range(0, n, 2):
            if i + 1 == n:
                break
            nxt_lists.append(merge2List(lists[i], lists[i + 1]))
        if n % 2 != 0:
            nxt_lists.append(lists[-1])
        return self.mergeKLists(nxt_lists)
```

也可使用 **小根堆** 每次取 $k$ 路最小头结点，时间同为 $O(N \log k)$；本解法 **分治结构清晰**，与 [148. 排序链表](../0148-sort-list) 的归并思想一脉相承。
