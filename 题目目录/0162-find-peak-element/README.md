<h2><a href="https://leetcode.cn/problems/find-peak-element">162. 寻找峰值</a></h2>
<h3>中等</h3>
<hr>
<p>峰值元素是指其值严格大于左右相邻值的元素。</p>
<p>给你一个整数数组&nbsp;<code>nums</code>，找到峰值元素并返回其索引。数组可能包含多个峰值，在这种情况下，返回 <strong>任何一个峰值</strong> 所在位置即可。</p>
<p>你可以假设&nbsp;<code>nums[-1] = nums[n] = -∞</code>。</p>
<p>你必须实现时间复杂度为 <code>O(log n)</code> 的算法来解决此问题。</p>
<p>&nbsp;</p>
<p><strong>示例 1：</strong></p>
<pre><strong>输入：</strong>nums = [1,2,3,1]
<strong>输出：</strong>2
<strong>解释：</strong>3 是峰值元素，你的函数应该返回其索引 2。</pre>

<p><strong>示例 2：</strong></p>
<pre><strong>输入：</strong>nums = [1,2,1,3,5,6,4]
<strong>输出：</strong>1 或 5
<strong>解释：</strong>你的函数可以返回索引 1（峰值元素 2），或者返回索引 5（峰值元素 6）。</pre>

---

### 解题思路

利用二分查找的"爬坡法"。核心洞察：比较 `nums[mid]` 与 `nums[mid + 1]` 即可确定峰值所在的方向——向递增的一侧搜索，一定能找到峰值（因为即使一路递增到边界，边界外的 -∞ 也会让最后一个元素成为峰值）。

为简化边界处理，在数组两端各添加一个哨兵 `-inf`，保证边界元素也能正确比较。

### 算法步骤

- 在数组两端添加哨兵：`nums = [-inf] + nums + [-inf]`。
- 定义递归二分搜索函数 `binarySearch(l, r)`：
  - 计算中点 `mid = (l + r) // 2`。
  - 若 `nums[mid] < nums[mid + 1]`，右侧为上坡，峰值在右半区，递归搜索 `[mid, r]`。
  - 若 `nums[mid] < nums[mid - 1]`，左侧为上坡，峰值在左半区，递归搜索 `[l, mid]`。
  - 否则 `nums[mid]` 同时大于等于两侧邻居，`mid` 即为峰值，返回 `mid`。
- 由于添加了哨兵导致索引右移一位，最终返回 `binarySearch(0, len(nums) - 1) - 1`。

### 复杂度分析

- 时间复杂度：O(log n)，每次递归将搜索区间缩小一半。
- 空间复杂度：O(log n)，递归调用栈深度为二分查找的递归深度。
