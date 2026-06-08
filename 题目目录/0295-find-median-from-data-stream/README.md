<h2><a href="https://leetcode.cn/problems/find-median-from-data-stream">295. 数据流的中位数</a></h2>
<h3>困难</h3>
<hr>
<p><strong>中位数</strong>是有序整数列表中的中间值。如果列表的大小是偶数，则没有中间值，此时中位数是两个中间值的平均数。</p>

<p>实现 <code>MedianFinder</code> 类：</p>
<ul>
  <li><code>MedianFinder()</code> 初始化 <code>MedianFinder</code> 对象。</li>
  <li><code>void addNum(int num)</code> 将数据流中的整数 <code>num</code> 添加到数据结构中。</li>
  <li><code>double findMedian()</code> 返回到目前为止所有元素的中位数。与实际答案的误差在 <code>10<sup>-5</sup></code> 以内的答案将被接受。</li>
</ul>

<p>&nbsp;</p>
<p><strong>示例 1：</strong></p>
<pre><strong>输入：</strong>
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
<strong>输出：</strong>
[null, null, null, 1.5, null, 2.0]
<strong>解释：</strong>
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // 返回 1.5 ((1 + 2) / 2)
medianFinder.addNum(3);    // arr = [1, 2, 3]
medianFinder.findMedian(); // 返回 2.0
</pre>

---

### 解题思路

本题的核心是 **对顶堆（Two Heaps）** 技巧，属于堆/优先队列中的经典设计题。

**核心思想**：维护两个堆，分别存储数据流中较小的一半和较大的一半：
- **左堆（max-heap，大根堆）**：存储数据流中**较小的一半**元素，堆顶是这部分的**最大值**。
- **右堆（min-heap，小根堆）**：存储数据流中**较大的一半**元素，堆顶是这部分的**最小值**。

**维护不变式**：
- `len(左堆) == len(右堆)` 或 `len(左堆) == len(右堆) + 1`（左堆可以多一个元素）
- 左堆中的所有元素 ≤ 右堆中的所有元素

这样一来，中位数就可以通过两个堆顶轻松得到：
- 若总数为奇数（左堆多一个），中位数就是左堆堆顶。
- 若总数为偶数，中位数为左堆堆顶与右堆堆顶的平均值。

**addNum 的核心操作**：

Python 标准库 `heapq` 只提供小根堆。为模拟大根堆，代码中用负数方式来实现左堆的大根堆行为。每次插入时：

- **若左右堆大小相同**（插入后总数为奇数）：
  1. 将 `num` 压入右堆（小根堆），同时弹出右堆最小值。
  2. 将弹出的值（取负）压入左堆（大根堆）。
  3. 这样左堆多一个元素，且左堆所有值 ≤ 右堆所有值。

- **若左右堆大小不同**（左堆多一个，插入后总数为偶数）：
  1. 将 `num`（取负）压入左堆（大根堆），同时弹出左堆最大值。
  2. 将弹出的值（取负恢复）压入右堆（小根堆）。
  3. 这样左右堆大小恢复相同，且不变式仍然成立。

**为什么这样能保证有序性**：每次插入都先把新元素放入"对侧"堆，然后弹出对侧堆的堆顶放入"本侧"堆。这确保了跨堆的元素顺序——较小的一半永远在左堆、较大的一半永远在右堆。

### 算法步骤

- 初始化左堆 `left`（大根堆，存储负数）和右堆 `right`（小根堆）。
- **addNum(num)**：
  - 若 `len(left) == len(right)`：`heappush_max(left, heappushpop(right, num))`
  - 否则（`len(left) > len(right)`）：`heappush(right, heappushpop_max(left, num))`
- **findMedian()**：
  - 若 `len(left) > len(right)`：返回 `left[0]`（大根堆堆顶，即较小一半的最大值）
  - 否则：返回 `(left[0] + right[0]) / 2`

### 关键点说明

- **heappush_max(heap, item)**：将 item 取负后压入堆，实现大根堆行为。
- **heappushpop(heap, item)**：压入新值并弹出堆顶（等价于 `heapq.heappushpop`）。
- **heappushpop_max(heap, item)**：将 item 取负压入大根堆，弹出堆顶后取负恢复。
- 本题是堆类问题的**模板级代码**，也是后续 **480. 滑动窗口中位数** 的前置知识。

### 复杂度分析

- **时间复杂度**：
  - `addNum`：O(log n)，每次涉及堆的插入和弹出操作。
  - `findMedian`：O(1)，直接取堆顶元素。
- **空间复杂度**：O(n)，两个堆共存储 n 个元素。
