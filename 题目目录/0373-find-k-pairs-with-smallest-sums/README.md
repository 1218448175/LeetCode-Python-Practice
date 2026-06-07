<h2><a href="https://leetcode.cn/problems/find-k-pairs-with-smallest-sums">373. 查找和最小的 K 对数字</a></h2>
<h3>中等</h3>
<hr>
<p>给定两个以 <strong>升序排列</strong> 的整数数组 <code>nums1</code> 和 <code>nums2</code>，以及一个整数 <code>k</code>。</p>
<p>定义一对值 <code>(u, v)</code>，其中第一个元素来自 <code>nums1</code>，第二个元素来自 <code>nums2</code>。</p>
<p>请找到<strong>和最小的 <code>k</code> 个数对</strong> <code>(u₁, v₁), (u₂, v₂) ... (uₖ, vₖ)</code>，按和值升序返回。</p>
<p>&nbsp;</p>
<p><strong>示例 1：</strong></p>
<pre><strong>输入：</strong>nums1 = [1,7,11], nums2 = [2,4,6], k = 3
<strong>输出：</strong>[1,2],[1,4],[1,6]
<strong>解释：</strong>返回序列中的前 3 对数：
     [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
</pre>

<p><strong>示例 2：</strong></p>
<pre><strong>输入：</strong>nums1 = [1,1,2], nums2 = [1,2,3], k = 2
<strong>输出：</strong>[1,1],[1,1]
<strong>解释：</strong>返回序列中的前 2 对数：
     [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
</pre>

<p><strong>示例 3：</strong></p>
<pre><strong>输入：</strong>nums1 = [1,2], nums2 = [3], k = 3
<strong>输出：</strong>[1,3],[2,3]
<strong>解释：</strong>也可能序列中所有的数对都被返回：[1,3],[2,3]
</pre>

---

### 解题思路

本题的核心是 **小根堆 + 多路归并**。

问题可以视为：将 `nums1` 的每个元素作为"行"，`nums2` 的每个元素作为"列"，形成一个隐式的二维矩阵，其中 `(i, j)` 位置的和为 `nums1[i] + nums2[j]`。由于两个数组都是升序排列，每一行从左到右递增，每一列从上到下递增。

我们的目标是从这个矩阵中找出和最小的 `k` 个数对——这本质上是一个 **多路归并** 问题。

**核心策略**：
1. 初始化小根堆，将每行的第一个元素 `(nums1[i] + nums2[0], i, 0)` 放入堆中（最多取 `min(len(nums1), k)` 个，因为只需要前 `k` 个结果）。
2. 循环 `k` 次，每次弹出堆顶（当前最小的数对），记录答案。
3. 弹出 `(sum, i, j)` 后，若该行还有下一个元素 `j + 1 < len(nums2)`，则将 `(nums1[i] + nums2[j+1], i, j+1)` 压入堆中。
4. 这样保证每次弹出一个最小和后，该行的下一个候选被立即加入堆中，维持堆中始终有当前最小的候选。

**为什么不用全矩阵**：矩阵最多可能有 `10^5 × 10^5 = 10^10` 个数对，无法全部构建。多路归并用堆只需维护 `O(min(n, k))` 大小的堆，每次弹出和压入都是 `O(log min(n, k))`。

### 算法步骤

- 初始化小根堆 `heap`，存储 `(nums1[i] + nums2[0], i, 0)`，`i` 从 `0` 到 `min(len(nums1), k) - 1`
- 初始化答案列表 `ans = []`
- 循环 `k` 次：
  - 从堆中弹出最小元组 `(sum, i, j)`
  - 将 `(nums1[i], nums2[j])` 加入答案
  - 若 `j + 1 < len(nums2)`，将 `(nums1[i] + nums2[j+1], i, j+1)` 压入堆
- 返回 `ans`

### 复杂度分析

- **时间复杂度**：O(k log min(n, k))。每次堆操作 O(log min(n, k))，共执行 k 次弹出和最多 k 次压入。
- **空间复杂度**：O(min(n, k))。堆中最多维护 min(n, k) 个元素。
