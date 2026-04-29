## [219. 存在重复元素 II](https://leetcode.cn/problems/contains-duplicate-ii/)

### 中等

给你一个整数数组 `nums` 和一个整数 `k` ，判断数组中是否存在两个 **不同的索引** `i` 和 `j` ，满足 `nums[i] == nums[j]` 且 `abs(i - j) <= k` 。如果存在，返回 `true` ；否则，返回 `false` 。

**示例 1：**

<pre><strong>输入：</strong>nums = [1,2,3,1], k<em> </em>= 3
<strong>输出：</strong>true</pre>

---

## 题解：动态哈希索引与“最近距离”校验策略

### 1. 核心思路：追踪元素的“最后目击位置”

本题是“重复元素”判断的进阶版，不仅要求数值相等，还附加了**空间距离**的限制。

- **记录位置**：我们使用一个哈希字典 `v_i_dict` 来存储每个数字及其对应的**最新索引**。

- **距离校验**：当我们第二次（或更多次）遇到同一个数字 `nums[i]` 时，我们只需要将当前的索引 `i` 与字典中记录的上一次索引进行对比。

- **贪心更新**：如果两者距离超过了 $k$，说明之前的那个索引已经“过期”了，不可能再与后续的数字组成满足条件的对。此时，我们用当前的 `i` 更新字典，因为**越靠后的索引越有可能与未来的数字满足距离约束**。

---

### 2. 执行逻辑的详细拆解

#### A. 哈希表映射关系

- **Key (键)**：数组中的数值。

- **Value (值)**：该数值在数组中最近一次出现的索引。

#### B. 遍历与条件分支

遍历数组 `nums`，对于每一个元素 `nums[i]`：

1. **初次见面或距离太远**：
   
   - 如果 `nums[i]` 不在字典中（`is None`），说明它是第一次出现。
   
   - 或者虽然出现过，但 `i - v_i_dict[nums[i]] > k`，说明距离不达标。
   
   - **处理**：更新（或插入）`v_i_dict[nums[i]] = i`。

2. **成功匹配**：
   
   - 如果发现 `nums[i]` 在字典中且当前距离 `i - last_index <= k`。
   
   - **处理**：找到符合条件的对，将 `ans` 设为 `True` 并立即 `break` 退出循环。

---

### 3. 逻辑亮点：贪心位置更新

你的代码中 `v_i_dict[nums[i]] = i` 的更新逻辑非常精妙。

对于同一个数字，如果旧的索引不满足条件，我们必须舍弃它并记录新的索引。因为对于后续可能出现的相同数字，新索引的距离一定更近，更容易满足 `abs(i - j) <= k`。这保证了算法始终在检测**当前元素与之前最近一个相同元素**的距离。

---

### 4. 复杂度分析

- **时间复杂度**：$O(N)$。只需对数组进行一次线性扫描，哈希表的查询与更新均为 $O(1)$。

- **空间复杂度**：$O(N)$。在最坏情况下（没有重复元素），我们需要在字典中存储所有 $N$ 个元素的索引。

---

### 代码回顾

```python
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        v_i_dict = {} # 记录 {数值: 最近一次出现的索引}
        n = len(nums)

        for i in range(n):
            num = nums[i]
            # 获取上一次该数字出现的位置
            last_idx = v_i_dict.get(num)

            # 逻辑：如果之前没出现过，或者虽然出现过但距离超过了 k
            if last_idx is None or (i - last_idx > k):
                # 更新为当前的最新位置
                v_i_dict[num] = i
            else:
                # 距离在 k 之内，满足条件
                return True

        return False
```

> **进阶思路**：这道题也可以使用**滑动窗口**结合 `set` 来解决。维护一个大小始终为 $k$ 的窗口，如果新进入窗口的数已经在 `set` 中，则直接返回 `True`。这种方式在空间上最多占用 $O(k)$。代码如下：

```python
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window_set = set()
        window_len = k
        n = len(nums)
        left = 0
        ans = False
        for right in range(n):
            if nums[right] not in window_set:
                window_set.add(nums[right])
                if right - left == window_len:
                    window_set.remove(nums[left])
                    left += 1
            else:
                ans = True
                break

        return ans
```