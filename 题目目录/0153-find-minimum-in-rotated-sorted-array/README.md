<h2><a href="https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array">153. 寻找旋转排序数组中的最小值</a></h2>
<h3>中等</h3>
<hr>
<p>已知一个长度为 <code>n</code> 的数组，预先按照<strong>升序排列</strong>，经由 <code>1</code> 到 <code>n</code> 次 <strong>旋转</strong> 后，得到输入数组。例如，原数组 <code>nums = [0,1,2,4,5,6,7]</code> 在变化后可能得到：</p>
<ul>
<li>若旋转 <code>4</code> 次，则可以得到 <code>[4,5,6,7,0,1,2]</code></li>
<li>若旋转 <code>7</code> 次，则可以得到 <code>[0,1,2,4,5,6,7]</code></li>
</ul>
<p>注意，数组 <code>[a[0], a[1], a[2], ..., a[n-1]]</code> <strong>旋转一次</strong> 的结果为数组 <code>[a[n-1], a[0], a[1], a[2], ..., a[n-2]]</code>。</p>
<p>给你一个元素值 <strong>互不相同</strong> 的数组 <code>nums</code>，它原来是一个升序排列的数组，并按上述情形进行了多次旋转。请你找出并返回数组中的 <strong>最小元素</strong>。</p>
<p>你必须设计一个时间复杂度为 <code>O(log n)</code> 的算法解决此问题。</p>
<p>&nbsp;</p>
<p><strong>示例 1：</strong></p>
<pre><strong>输入：</strong>nums = [3,4,5,1,2]
<strong>输出：</strong>1
<strong>解释：</strong>原数组为 [1,2,3,4,5] ，旋转 3 次得到输入数组。
</pre>

<p><strong>示例 2：</strong></p>
<pre><strong>输入：</strong>nums = [4,5,6,7,0,1,2]
<strong>输出：</strong>0
<strong>解释：</strong>原数组为 [0,1,2,4,5,6,7] ，旋转 4 次得到输入数组。
</pre>

<p><strong>示例 3：</strong></p>
<pre><strong>输入：</strong>nums = [11,13,15,17]
<strong>输出：</strong>11
<strong>解释：</strong>原数组为 [11,13,15,17] ，旋转 4 次得到输入数组。
</pre>

---

### 解题思路

旋转排序数组有一个关键性质：**取中点 `mid`，比较 `nums[mid]` 与 `nums[l]`，可以判断左半部分是否有序**。由于数组元素互不相同，可以分两种情况递归：

- **若 `nums[mid] >= nums[l]`**：左半 `[l, mid]` 是升序的，`nums[l]` 是这一半的最小值。但最小值也可能在无序的右半 `[mid+1, r]` 中。因此返回 `min(nums[l], 递归搜索右半)`。
- **若 `nums[mid] < nums[l]`**：说明旋转点（最小值）落在左半。此时右半 `[mid, r]` 是升序的，最小值必然在左半 `[l, mid]` 中。递归搜索左半（含 `mid`）。

递归终止条件：当区间只剩一个元素时（`l == r`），该元素即所求。

### 算法步骤

- 定义递归函数 `binarySearch(nums)`：
  - 初始化 `l = 0, r = len(nums) - 1`。
  - 若 `l == r`，区间仅一个元素，返回 `nums[l]`。
  - 计算 `mid = (l + r) // 2`。
  - **情况一**：`nums[mid] >= nums[l]` → 左半有序，返回 `min(nums[l], binarySearch(nums[mid+1:]))`。
  - **情况二**（隐含 `nums[mid] < nums[l]`）：右半有序，最小值在左半，返回 `binarySearch(nums[:mid+1])`。

- 调用 `binarySearch(nums)` 返回结果。

### 复杂度分析

- **时间复杂度**：O(log n)，每次递归将搜索区间减半。
- **空间复杂度**：O(log n)，递归调用栈深度。若改为迭代实现可优化至 O(1)。
