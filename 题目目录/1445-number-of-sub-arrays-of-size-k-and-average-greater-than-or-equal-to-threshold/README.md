## [1445. 大小为 K 且平均值大于等于阈值的子数组数目](https://leetcode.cn/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/)

### 中等

给你一个整数数组 `arr` 和两个整数 `k` 和 `threshold`，请你返回长度为 `k` 且平均值大于等于 `threshold` 的子数组数目。

**示例 1：**
<pre><strong>输入：</strong>arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
<strong>输出：</strong>3
<strong>解释：</strong>子数组 [2,5,5]、[5,5,5] 和 [5,5,8] 的平均值分别为 4、5 和 6。
</pre>

**示例 2：**
<pre><strong>输入：</strong>arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5
<strong>输出：</strong>6
</pre>

---

## 题解：定长滑动窗口 + 等价转换

### 1. 问题分析

本题是**定长滑动窗口**的经典应用题。窗口长度固定为 `k`，需要统计所有满足"平均值 ≥ threshold"的窗口个数。

**关键等价转换**：平均值判断 `sum / k >= threshold` 等价于 `sum >= k * threshold`。通过将阈值乘以 `k`，避免了浮点数运算，只需比较整数和。

---

### 2. 核心思路：三步循环法

代码沿用了定长滑动窗口的"三步循环法"——在单层循环中同时完成：右端点进入 → 更新答案 → 左端点离开。但这里使用了一个更巧妙的状态维护方式：**用 `target` 变量动态追踪窗口和与目标之间的差距**。

```python
def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
    n = len(arr)
    target = k * threshold    # 所需的最小和
    ans = 0
    for i in range(n):        # 枚举窗口右端点 i
        left = i - k + 1      # 计算窗口左端点
        target -= arr[i]      # 1. 右端点进入窗口（消耗目标）
        if left < 0:          # 窗口长度不足 k → 继续扩展
            continue
        if target <= 0:       # 2. 窗口和 ≥ k*threshold → 平均值 ≥ threshold
            ans += 1          #    更新答案
        target += arr[left]   # 3. 左端点离开窗口（归还目标）
    return ans
```

**核心变量 `target` 的含义**：`target = k * threshold - sum(当前窗口)`。即"当前窗口和距离目标还差多少"。
- `target -= arr[i]`：新元素进入窗口，距离目标更近了（差减少）
- `target <= 0`：窗口和已经达到或超过目标 → 满足条件
- `target += arr[left]`：旧元素离开窗口，差距扩大（差增加）

**窗口滑动示意图（arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4, target 初值 = 12）：**

| 步 | i | arr[i] | left | 窗口内容 | target（进入后） | 判断 | ans | target（离开后） |
|----|---|--------|------|----------|-----------------|------|-----|-----------------|
| 0 | 0 | 2 | -2 | — | 10 | continue | 0 | 10 |
| 1 | 1 | 2 | -1 | — | 8 | continue | 0 | 8 |
| 2 | 2 | 2 | 0 | [2,2,2] | 6 | >0, 不计数 | 0 | 8 (+2) |
| 3 | 3 | 2 | 1 | [2,2,2] | 6 | >0, 不计数 | 0 | 8 (+2) |
| 4 | 4 | 5 | 2 | [2,2,5] | 3 | >0, 不计数 | 0 | 5 (+2) |
| 5 | 5 | 5 | 3 | [2,5,5] | 0 | **≤0, ans=1** | 1 | 2 (+2) |
| 6 | 6 | 5 | 4 | [5,5,5] | -3 | **≤0, ans=2** | 2 | 2 (+5) |
| 7 | 7 | 8 | 5 | [5,5,8] | -6 | **≤0, ans=3** | 3 | -1 (+5) |

最终答案：**3**。

---

### 3. 亮点分析

#### 3.1 `target` 变量的一鱼多吃

传统写法需要显式维护 `window_sum` 变量：

```python
# 传统写法
window_sum = sum(arr[:k])
if window_sum >= target:
    ans += 1
for i in range(k, n):
    window_sum += arr[i] - arr[i - k]
    if window_sum >= target:
        ans += 1
```

而本代码将 `target` 复用为"距离目标的差值"，省去了 `window_sum` 变量。`target -= arr[i]` 既是"将新元素纳入窗口"，也是"更新差值"。`target <= 0` 直接判断是否达标。

#### 3.2 统一单循环结构

与 [1456. 定长子串中元音的最大数目](./1456-maximum-number-of-vowels-in-a-substring-of-given-length) 的模板一致，本代码将所有逻辑统一在一个 `for` 循环中：

- **未形成窗口（left < 0）**：只让右端点进入，不判断、不移除 → `continue`
- **形成窗口后**：进入 → 判断 → 移除

避免了传统写法中"先单独初始化第一个窗口"的二次循环，代码更紧凑。

---

### 4. 复杂度分析

- **时间复杂度**：$O(n)$。每个元素被 `target -= arr[i]`（进入窗口）和 `target += arr[left]`（离开窗口）各处理一次，单次遍历完成。
- **空间复杂度**：$O(1)$，仅使用 `target`、`ans`、`left` 三个额外变量。

---

### 延伸思考

- 本题的核心技巧是**平均值比较转化为和比较**：`avg ≥ threshold` ⇔ `sum ≥ k × threshold`。这是处理"子数组平均值"类问题的标准手法，避免了浮点数精度问题。
- 代码中的 `target` 变量承担了双重角色——既是"目标值"又是"差值追踪器"，这种变量复用技巧在定长滑动窗口中十分优雅。
- 定长滑动窗口的统一模板（右进 → 判断 → 左出）同样适用于 [643. 子数组最大平均数 I](./0643-maximum-average-subarray-i) 和 [1456. 定长子串中元音的最大数目](./1456-maximum-number-of-vowels-in-a-substring-of-given-length)，建议对照练习。
