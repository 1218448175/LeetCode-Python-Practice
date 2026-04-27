<h2><a href="https://leetcode.cn/problems/merge-sorted-array">88. 合并两个有序数组</a></h2>
<h3>简单</h3>
<hr>
<p>给你两个按 <strong>非递减顺序</strong> 排列的整数数组 <code>nums1</code><em> </em>和 <code>nums2</code>，另有两个整数 <code>m</code> 和 <code>n</code> ，分别表示 <code>nums1</code> 和 <code>nums2</code> 中的元素数目。</p>
<p>请你 <strong>合并</strong> <code>nums2</code><em> </em>到 <code>nums1</code><em> </em>中，使合并后的数组同样按 <strong>非递减顺序</strong> 排列。</p>

---

### 解题思路

1. **双指针法（从后往前）**：由于 `nums1` 后部有足够的空位，为了避免覆盖掉 `nums1` 前面的元素，我们从两个数组的末尾开始比较。
2. **比较与放置**：设置三个指针，分别指向 `nums1` 的有效数据末尾、`nums2` 的末尾以及 `nums1` 的最终位置末尾。
3. **处理剩余**：如果 `nums2` 还有剩余，将其全部拷贝至 `nums1` 前部。

### 复杂度分析

* 时间复杂度：O(m + n)
* 空间复杂度：O(1)，直接在原数组上操作。
