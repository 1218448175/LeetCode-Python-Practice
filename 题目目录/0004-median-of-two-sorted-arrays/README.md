<h2><a href="https://leetcode.cn/problems/median-of-two-sorted-arrays">4. 寻找两个正序数组的中位数</a></h2>
<h3>困难</h3>
<hr>
<p>给定两个大小分别为 <code>m</code> 和 <code>n</code> 的正序（从小到大）数组 <code>nums1</code> 和 <code>nums2</code>。请你找出并返回这两个正序数组的 <strong>中位数</strong>。</p>
<p>算法的时间复杂度应该为 <code>O(log (m+n))</code>。</p>
<p>&nbsp;</p>
<p><strong>示例 1：</strong></p>
<pre><strong>输入：</strong>nums1 = [1,3], nums2 = [2]
<strong>输出：</strong>2.00000
<strong>解释：</strong>合并数组 = [1,2,3]，中位数 2
</pre>

<p><strong>示例 2：</strong></p>
<pre><strong>输入：</strong>nums1 = [1,2], nums2 = [3,4]
<strong>输出：</strong>2.50000
<strong>解释：</strong>合并数组 = [1,2,3,4]，中位数 (2 + 3) / 2 = 2.5
</pre>

---

### 解题思路

求两个有序数组的中位数，本质是求这两个数组中**第 k 小的数**：

- 若总长度 `totalLen` 为奇数，中位数是第 `(totalLen + 1) / 2` 小的数。
- 若总长度 `totalLen` 为偶数，中位数是第 `totalLen / 2` 小和第 `totalLen / 2 + 1` 小的数的平均值。

问题转化为：**如何在 O(log(m+n)) 时间内找到两个有序数组中的第 k 小的数？**

核心思路是**二分排除法**。要找到第 k 小的元素，可以比较两个数组中第 `k/2` 个元素：

- 取 `pivot1 = nums1[index1 + k/2 - 1]`，`pivot2 = nums2[index2 + k/2 - 1]`（注意处理越界，即剩余元素不足 `k/2` 个的情况）。
- 如果 `pivot1 <= pivot2`，说明 `nums1` 中从 `index1` 到 `index1 + k/2 - 1` 这 `k/2` 个元素**一定不是**第 k 小的数（它们都比第 k 小的数更小），可以安全排除。排除后 `k` 减去排除的元素个数，`index1` 移动到排除位置之后。
- 如果 `pivot1 > pivot2`，同理排除 `nums2` 中的 `k/2` 个元素。

每次排除约 `k/2` 个元素，`k` 按指数速度减少，最终当 `k == 1` 时，返回两个指针所指元素的最小值即可。

**边界情况**：如果某个数组已经全部被排除（指针到达数组末尾），直接从另一个数组中返回第 k 个元素。

### 算法步骤

- 定义函数 `getBottomKItem(k)`，返回两个数组中第 k 小的元素：
  - 初始化两个指针 `index1 = 0`, `index2 = 0`，分别指向两个数组当前搜索起点。
  - 循环：
    - 若 `index1 == m`（`nums1` 已耗尽），返回 `nums2[index2 + k - 1]`。
    - 若 `index2 == n`（`nums2` 已耗尽），返回 `nums1[index1 + k - 1]`。
    - 若 `k == 1`，返回 `min(nums1[index1], nums2[index2])`。
    - 计算两个数组各自的新下标 `newIndex1 = min(index1 + k // 2 - 1, m - 1)`，`newIndex2 = min(index2 + k // 2 - 1, n - 1)`。
    - 比较 `nums1[newIndex1]` 和 `nums2[newIndex2]`：
      - 若 `pivot1 <= pivot2`：排除 `nums1` 中 `[index1, newIndex1]` 共 `newIndex1 - index1 + 1` 个元素，`k` 减去该数量，`index1` 移至 `newIndex1 + 1`。
      - 否则：排除 `nums2` 中对应元素，更新 `k` 和 `index2`。

- 计算总长度 `totalLen = m + n`：
  - 若为奇数，返回 `getBottomKItem((totalLen + 1) // 2)`。
  - 若为偶数，返回 `(getBottomKItem(totalLen // 2) + getBottomKItem(totalLen // 2 + 1)) / 2`。

### 复杂度分析

- **时间复杂度**：O(log(m+n))。每次循环 `k` 的值减少约一半（`k - k/2`），因此最多执行 O(log k) ≤ O(log(m+n)) 次循环。偶数情况调用两次 `getBottomKItem`，常数因子仍为 O(log(m+n))。
- **空间复杂度**：O(1)，仅使用常数个变量。
