<h2><a href="https://leetcode.cn/problems/kth-largest-element-in-an-array">215. 数组中的第K个最大元素</a></h2>
<h3>中等</h3>
<hr>
<p>给定整数数组 <code>nums</code> 和整数 <code>k</code>，请返回数组中第 <code>k</code> 个最大的元素。</p>
<p>请注意，你需要找的是数组排序后的第 <code>k</code> 个最大的元素，而不是第 <code>k</code> 个不同的元素。</p>
<p>你必须设计并实现时间复杂度为 <strong>O(n)</strong> 的算法解决此问题。</p>
<p>&nbsp;</p>
<p><strong>示例 1：</strong></p>
<pre><strong>输入:</strong> [3,2,1,5,6,4], k = 2
<strong>输出:</strong> 5
</pre>

<p><strong>示例 2：</strong></p>
<pre><strong>输入:</strong> [3,2,3,1,2,4,5,5,6], k = 4
<strong>输出:</strong> 4
</pre>

---

### 解题思路

本题是经典的 **Top-K 问题**，要求在未排序的数组中找到第 k 大的元素。常见解法有排序（O(n log n)）、小顶堆（O(n log k)）和**快速选择（Quick Select）**（平均 O(n)）。

本题解采用 **快速选择算法**，它是快速排序的变体。核心思想是：通过随机选取 pivot 将数组划分为三部分（大于、等于、小于 pivot），然后只递归搜索包含目标元素的那一部分，从而避免了对整个数组排序。

**三路划分（Three-way Partition）**：

- 随机选择一个 `pivot`，将数组分成三个桶：
  - `big`：所有大于 pivot 的元素
  - `equal`：所有等于 pivot 的元素
  - `small`：所有小于 pivot 的元素
- 根据 k 与各桶大小的关系，判断目标元素落在哪个桶：
  - 若 `k ≤ len(big)`：第 k 大的元素在 `big` 中，递归搜索 `big`
  - 若 `k > len(big) + len(equal)`：第 k 大的元素在 `small` 中，递归搜索 `small`，并调整 k 值（减去 big 和 equal 中的元素数量）
  - 否则：pivot 就是第 k 大的元素，直接返回

每次递归都会排除掉至少一个桶中的元素（small 或 big），期望每次排除约一半的元素，因此平均时间复杂度为 O(n)。

### 算法步骤

- 定义 `quick_select(nums, k)` 递归函数：
  - 从 `nums` 中随机选择一个元素作为 `pivot`
  - 遍历数组，将元素分别放入 `small`（< pivot）、`equal`（== pivot）、`big`（> pivot）三个列表
  - 判断 k 与各桶的关系：
    - 如果 `k <= len(big)`：第 k 大在 big 中，返回 `quick_select(big, k)`
    - 如果 `k > len(nums) - len(small)`（即 `k > len(big) + len(equal)`）：第 k 大在 small 中，返回 `quick_select(small, k + len(small) - len(nums))`（从 small 中找第 `k - len(big) - len(equal)` 大）
    - 否则：返回 `pivot`

- 主函数直接调用 `quick_select(nums, k)` 即可

### 复杂度分析

- **时间复杂度**：平均 O(n)，最坏 O(n²)。随机选择 pivot 使得期望每次递归排除约一半元素，总期望比较次数为 n + n/2 + n/4 + ... ≈ 2n。最坏情况下（如 pivot 每次都选到最小/最大值），退化为 O(n²)，但概率极低。
- **空间复杂度**：O(n)（递归栈 + 每层新建三个列表）。递归栈深度期望为 O(log n)，每层需要创建 small/equal/big 三个辅助列表，总空间 O(n)。
