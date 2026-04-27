<h2><a href="https://leetcode.cn/problems/insert-delete-getrandom-o1">380. O(1) 时间插入、删除和获取随机元素</a></h2>
<h3>中等</h3>
<hr>

<p>实现<code>RandomizedSet</code> 类：</p>
<ul>
    <li><code>RandomizedSet()</code> 初始化 <code>RandomizedSet</code> 对象</li>
    <li><code>bool insert(int val)</code> 当元素 <code>val</code> 不存在时，向集合中插入该项，并返回 <code>true</code> ；否则，返回 <code>false</code> 。</li>
    <li><code>bool remove(int val)</code> 当元素 <code>val</code> 存在时，从集合中移除该项，并返回 <code>true</code> ；否则，返回 <code>false</code> 。</li>
    <li><code>int getRandom()</code> 随机返回现有集合中的一项（测试用例保证调用此方法时集合中至少存在一个元素）。每个元素应该有 <strong>相同的概率</strong> 被返回。</li>
</ul> 
<p>你必须实现类的所有函数，并满足每个函数的 <strong>平均</strong> 时间复杂度为 <code>O(1)</code> 。</p>
<p> </p>
<p><strong>示例：</strong></p>
<pre><strong>输入</strong>
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
<strong>输出</strong>
[null, true, false, true, 2, true, false, 2]

<strong>解释</strong>
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // 向集合中插入 1 。返回 true 表示 1 被成功地插入。
randomizedSet.remove(2); // 返回 false ，表示集合中不存在 2 。
randomizedSet.insert(2); // 向集合中插入 2 。返回 true 。集合现在包含 [1,2] 。
randomizedSet.getRandom(); // getRandom 应随机返回 1 或 2 。
randomizedSet.remove(1); // 从集合中移除 1 ，返回 true 。集合现在包含 [2] 。
randomizedSet.insert(2); // 2 已在集合中，所以返回 false 。
randomizedSet.getRandom(); // 由于 2 是集合中唯一的数字，getRandom 总是返回 2 。
</pre>

## 题解：哈希表 + 动态数组实现 $O(1)$ 随机访问

### 设计思路

要在 **$O(1)$** 时间内实现插入、删除和随机获取，我们需要结合两种数据结构的优势：

1. **动态数组 (`self.nums`)**：
   
   - 支持 $O(1)$ 的末尾插入和末尾删除。
   
   - 支持 $O(1)$ 的下标随机访问。这是实现 `getRandom` 的核心。

2. **哈希表 (`self.indices`)**：
   
   - 存储 `val -> index` 的映射。
   
   - 支持 $O(1)$ 的查找，用于判断元素是否存在以及获取其在数组中的位置。

---

## 核心逻辑

### 1. 插入 (Insert)

- 检查 `val` 是否已在哈希表中。

- 若不在，将 `val` 添加到数组末尾，并在哈希表中记录其下标为 `len(self.nums) - 1`。

### 2. 删除 (Remove) —— “交换删除”技巧

数组删除非末尾元素通常需要 $O(n)$ 时间移动后续数据。为了维持 $O(1)$，我们采用以下策略：

- 通过哈希表获取 `val` 的下标 `index`。

- 将数组中 **最后一个元素** `last_val` 移动到 `index` 的位置（即覆盖掉要删除的 `val`）。

- 在哈希表中更新 `last_val` 的对应下标为 `index`。

- 弹出（`pop`）数组末尾元素，并从哈希表中删除 `val`。

### 3. 随机获取 (GetRandom)

- 由于数组是紧凑存储的，直接在 `[0, len(self.nums) - 1]` 范围内随机生成一个下标，返回该位置的元素即可。

---

## 复杂度分析

| **操作**        | **平均时间复杂度** | **原因**                    |
| ------------- | ----------- | ------------------------- |
| **insert**    | $O(1)$      | 哈希表查找与数组末尾插入均为 $O(1)$。    |
| **remove**    | $O(1)$      | 通过哈希表精确定位，交换末尾元素后弹出，无需平移。 |
| **getRandom** | $O(1)$      | 数组支持根据下标进行常数时间的随机访问。      |

- **空间复杂度**：$O(n)$，需要存储 $n$ 个元素的哈希表映射和动态数组。