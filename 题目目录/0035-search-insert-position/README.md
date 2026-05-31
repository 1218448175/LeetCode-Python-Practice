<h2><a href="https://leetcode.cn/problems/search-insert-position">35. 搜索插入位置</a></h2>
<h3>简单</h3>
<hr>
<p>给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。</p>
<p>请必须使用时间复杂度为 <code>O(log n)</code> 的算法。</p>
<p>&nbsp;</p>
<p><strong>示例 1：</strong></p>
<pre><strong>输入：</strong>nums = [1,3,5,6], target = 5
<strong>输出：</strong>2
</pre>

<p><strong>示例 2：</strong></p>
<pre><strong>输入：</strong>nums = [1,3,5,6], target = 2
<strong>输出：</strong>1
</pre>

<p><strong>示例 3：</strong></p>
<pre><strong>输入：</strong>nums = [1,3,5,6], target = 7
<strong>输出：</strong>4
</pre>

---

### 解题思路

基于二分查找，在有序数组中定位目标值或其插入位置。递归地在左右子区间中搜索，当未找到目标值时，利用二分搜索的边界信息确定插入位置。

### 算法步骤

- 定义递归二分搜索函数 `binarySearch(left, right)`：
  - 若 `left > right`，说明已越过搜索边界，返回 `-1` 表示未找到。
  - 计算中点 `mid = (left + right) // 2`。
  - 若 `nums[mid] == target`，命中目标，返回 `mid`。
  - 若 `nums[mid] > target`，在左半区 `[left, mid-1]` 递归搜索：
    - 若左半区找到目标，返回其索引；
    - 否则（返回 `-1`），说明 target 应插入在当前 `left` 位置（因为 target 小于 `nums[mid]` 且大于左半区所有元素）。
  - 若 `nums[mid] < target`，在右半区 `[mid+1, right]` 递归搜索：
    - 若右半区找到目标，返回其索引；
    - 否则，说明 target 应插入在 `right + 1` 位置（target 大于右半区所有元素）。

- 调用 `binarySearch(0, len(nums) - 1)` 返回结果。

### 复杂度分析

- 时间复杂度：O(log n)，标准二分查找每次将搜索区间减半。
- 空间复杂度：O(log n)，递归调用栈深度为二分查找的递归深度。
