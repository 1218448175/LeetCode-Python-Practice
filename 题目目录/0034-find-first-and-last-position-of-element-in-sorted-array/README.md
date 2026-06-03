<h2><a href="https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array">34. 在排序数组中查找元素的第一个和最后一个位置</a></h2>
<h3>中等</h3>
<hr>
<p>给你一个按照非递减顺序排列的整数数组 <code>nums</code>，和一个目标值 <code>target</code>。请你找出给定目标值在数组中的开始位置和结束位置。</p>
<p>如果数组中不存在目标值 <code>target</code>，返回 <code>[-1, -1]</code>。</p>
<p>你必须设计并实现时间复杂度为 <code>O(log n)</code> 的算法解决此问题。</p>
<p>&nbsp;</p>
<p><strong>示例 1：</strong></p>
<pre><strong>输入：</strong>nums = [5,7,7,8,8,10], target = 8
<strong>输出：</strong>[3,4]
</pre>

<p><strong>示例 2：</strong></p>
<pre><strong>输入：</strong>nums = [5,7,7,8,8,10], target = 6
<strong>输出：</strong>[-1,-1]
</pre>

<p><strong>示例 3：</strong></p>
<pre><strong>输入：</strong>nums = [], target = 0
<strong>输出：</strong>[-1,-1]
</pre>

---

### 解题思路

题目要求 O(log n) 时间复杂度，必须使用**二分查找**。核心思路是通过两次二分查找分别定位目标值的**左边界**（第一个位置）和**右边界**（最后一个位置）。

这里使用一个巧妙的技巧：只实现一个 `lower_bound` 函数（找到第一个 `>= target` 的位置），就能同时求出左右边界：

- **左边界（start）**：调用 `lower_bound(nums, target)`，找到第一个 `>= target` 的位置。
- **右边界（end）**：调用 `lower_bound(nums, target + 1)`，找到第一个 `>= target + 1` 的位置，再减 1 就是 `target` 最后一次出现的位置。

最后，如果 `start` 越界或者 `nums[start] != target`，说明数组中不存在 `target`，返回 `[-1, -1]`。

### 算法步骤

- 定义 `lower_bound(nums, target)` 函数，返回第一个 `>= target` 的下标：
  - 初始化 `left = 0, right = len(nums) - 1`。
  - 当 `left <= right` 时：
    - 计算 `mid = left + (right - left) // 2`。
    - 若 `nums[mid] >= target`，收缩右边界 `right = mid - 1`（目标可能在更左侧）。
    - 否则 `nums[mid] < target`，收缩左边界 `left = mid + 1`。
  - 循环结束时，`left` 恰好指向第一个 `>= target` 的位置，返回 `left`。

- 在 `searchRange` 中：
  - `start = lower_bound(nums, target)`。
  - 若 `start == len(nums)` 或 `nums[start] != target`，返回 `[-1, -1]`。
  - `end = lower_bound(nums, target + 1) - 1`。
  - 返回 `[start, end]`。

### 复杂度分析

- **时间复杂度**：O(log n)，两次二分查找各 O(log n)。
- **空间复杂度**：O(1)，只使用了常量级额外空间。
