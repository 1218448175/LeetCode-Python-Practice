## [148. 排序链表](https://leetcode.cn/problems/sort-list/)

### 中等

给你链表的头结点 `head`，请将其按 **升序** 排列并返回排序后的链表。

在 $O(n \log n)$ 时间复杂度和常数级空间复杂度下，你可以对链表进行排序吗？

**示例 1：**

```
输入：head = [4,2,1,3]
输出：[1,2,3,4]
```

**示例 2：**

```
输入：head = [-1,5,3,4,0]
输出：[-1,0,3,4,5]
```

**示例 3：**

```
输入：head = []
输出：[]
```

---

## 题解：归并排序分治 + 快慢指针找中点

### 1. 核心思路：链表上的分治归并

数组归并排序的经典三步——**切分、递归排序、合并**——可以直接迁移到链表：

1. **找中点并切断**：快慢指针定位前半段末尾 `slow`，将 `slow.next` 作为右半段头，再 `slow.next = None` 断开左右子链表。
2. **分治递归**：`sortList(head)` 与 `sortList(mid)` 分别得到升序的左、右子链表。
3. **二路归并**：`mergeList` 用哑节点依次拼接较小结点，$O(n)$ 完成合并。

递归边界为 `head` 为空或仅一个结点，直接返回。

---

### 2. 执行逻辑拆解

#### A. 快慢指针找中点

```python
slow, fast = head, head.next
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
mid = slow.next
slow.next = None
```

- `fast` 从 `head.next` 起步、`slow` 从 `head` 起步，保证 **`slow` 停在前半段最后一个结点**（右半段从 `slow.next` 开始）。
- 切断后左右子链表互不相交，递归不会重复访问同一结点。

#### B. 分治与合并

```python
left = self.sortList(head)
right = self.sortList(mid)
return self.mergeList(left, right)
```

`mergeList` 维护 `dummy` 与 `cur`，双指针比较 `l.val` 与 `r.val`，某一侧耗尽后接上另一侧剩余链。

---

### 3. 算法可视化

以 `4 → 2 → 1 → 3` 为例：

1. 中点切分为 `[4,2]` 与 `[1,3]`；
2. 左半再分为 `[4]`、`[2]`，归并得 `[2,4]`；
3. 右半再分为 `[1]`、`[3]`，归并得 `[1,3]`；
4. 最终归并 `[2,4]` 与 `[1,3]` → `[1,2,3,4]`。

---

### 4. 复杂度分析

- **时间复杂度**：$O(n \log n)$。每层归并遍历全部结点，递归深度 $O(\log n)$。
- **空间复杂度**：$O(\log n)$ 递归栈；若不计栈则为合并过程的 $O(1)$ 指针操作。题目要求的「常数空间」通常指迭代自底向上归并；本解法为 **自顶向下分治归并**，思路清晰且满足 $O(n \log n)$ 时间。

---

### 5. 代码实现回顾

```python
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        left = self.sortList(head)
        right = self.sortList(mid)
        return self.mergeList(left, right)

    def mergeList(self, l, r):
        dummy = ListNode()
        cur = dummy
        while l and r:
            if l.val <= r.val:
                cur.next = l
                l = l.next
            else:
                cur.next = r
                r = r.next
            cur = cur.next
        cur.next = l if l else r
        return dummy.next
```

与 [108. 将有序数组转换为二叉搜索树](../0108-convert-sorted-array-to-binary-search-tree) 同属 **分治**：先拆成规模更小的子问题，再在合并阶段得到全局有序结果。
