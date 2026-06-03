<h2><a href="https://leetcode.cn/problems/search-in-rotated-sorted-array">33. 搜索旋转排序数组</a></h2>
<h3>中等</h3>
<hr>
<p>整数数组 <code>nums</code> 按升序排列，数组中的值 <strong>互不相同</strong>。</p>
<p>在传递给函数之前，<code>nums</code> 在预先未知的某个下标 <code>k</code>（<code>0 <= k < nums.length</code>）上进行了 <strong>旋转</strong>，使数组变为 <code>[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]</code>（下标 <strong>从 0 开始</strong> 计数）。例如， <code>[0,1,2,4,5,6,7]</code> 在下标 <code>3</code> 处经旋转后可能变为 <code>[4,5,6,7,0,1,2]</code>。</p>
<p>给你 <strong>旋转后</strong> 的数组 <code>nums</code> 和一个整数 <code>target</code>，如果 <code>nums</code> 中存在这个目标值 <code>target</code>，则返回它的下标，否则返回 <code>-1</code>。</p>
<p>你必须设计一个时间复杂度为 <code>O(log n)</code> 的算法解决此问题。</p>
<p>&nbsp;</p>
<p><strong>示例 1：</strong></p>
<pre><strong>输入：</strong>nums = [4,5,6,7,0,1,2], target = 0
<strong>输出：</strong>4
</pre>

<p><strong>示例 2：</strong></p>
<pre><strong>输入：</strong>nums = [4,5,6,7,0,1,2], target = 3
<strong>输出：</strong>-1
</pre>

<p><strong>示例 3：</strong></p>
<pre><strong>输入：</strong>nums = [1], target = 0
<strong>输出：</strong>-1
</pre>

---

### 解题思路

旋转排序数组虽然整体不是有序的，但有一个关键性质：**任意取一个中点 `mid`，其左右两半中至少有一半是有序的**。利用这一性质，可以在 O(log n) 时间内完成搜索。

具体而言，每次取中点后：
- 判断哪一半是有序的（通过比较 `nums[mid]` 与两端边界值）
- 判断 `target` 是否落在有序的那一半中
- 若在有序一半中，则舍弃另一半；否则舍弃有序的那一半

### 算法步骤

- 定义递归二分搜索函数 `binarySearch(l, r)`：
  - 若 `l > r`，搜索区间为空，返回 `-1`。
  - 计算 `mid = (l + r) // 2`，若 `nums[mid] == target` 则命中，返回 `mid`。
  
- **情况一：`nums[mid] < nums[l]`**（旋转点落在左半区，右半区 `[mid, r]` 有序）：
  - 若 `target < nums[mid]` 或 `target > nums[r]`，说明 `target` 不在有序的右半区，搜索左半区 `[l, mid-1]`。
  - 否则搜索右半区 `[mid+1, r]`。
  
- **情况二：`nums[mid] > nums[r]`**（旋转点落在右半区，左半区 `[l, mid]` 有序）：
  - 若 `target > nums[mid]` 或 `target < nums[l]`，说明 `target` 不在有序的左半区，搜索右半区 `[mid+1, r]`。
  - 否则搜索左半区 `[l, mid-1]`。
  
- **情况三：其他**（当前区间 `[l, r]` 为正常有序数组）：
  - 标准二分查找：若 `target > nums[mid]` 则搜索右半区，否则搜索左半区。

- 调用 `binarySearch(0, len(nums) - 1)` 返回结果。

### 复杂度分析

- **时间复杂度**：O(log n)，每次递归将搜索区间减半。
- **空间复杂度**：O(log n)，递归调用栈深度为二分查找的递归深度。若改为迭代实现可优化至 O(1)。
