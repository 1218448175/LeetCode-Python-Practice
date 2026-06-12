# LeetCode-Python-Practice

记录leetcode刷题记录

## 🎯 精选题解 (Highly Recommended)

这里记录了我对核心高频面试题（top150）的解题和优化思路

### 🔗 数组与字符串

* [0088-合并两个有序数组](./题目目录/0088-merge-sorted-array) —— 重点：逆向双指针优化空间至 O(1)
* [0027-移除元素](./题目目录/0027-remove-element) —— 重点：双向双指针优化时间复杂度
* [0026-移除有序数组中的重复项](./题目目录/0026-remove-duplicates-from-sorted-array)
* [0080-移除有序数组中的重复项 II](./题目目录/0080-remove-duplicates-from-sorted-array-ii)
* [0169-多数元素](./题目目录/0169-majority-element) —— 重点：投票法（相异相消）优化空间至O(1)
* [0189-轮转数组](./题目目录/0169-majority-element)
* [0055-跳跃游戏](./题目目录/0055-jump-game)
* [0055-跳跃游戏 II](./题目目录/0055-jump-game-ii) —— 重点：贪心中的边界处理
* [0274-H 指数](./题目目录/0274-h-index) —— 重点：计数排序优化时间至O(n)
* [0380-O(1) 时间插入、删除和获取随机元素](./题目目录/0380-insert-delete-getrandom-o1) —— 重点：变长数组+HashMap
* [0238-除了自身以外数组的乘积](./题目目录/0238-product-of-array-except-self) —— 重点：动态构建右乘积列表优化空间为O(1)
* [0134-加油站](./题目目录/0134-gas-station)
* [0135-分发糖果](./题目目录/0135-candy) —— 重点：贪心算法实现 O(n) 一次遍历
* [0042-接雨水](./题目目录/0042-trapping-rain-water) —— 重点：双指针实现O(n)一次遍历
* [0013-罗马数字转整数](./题目目录/0013-roman-to-integer)
* [0012-整数转罗马数字](./题目目录/0012-integer-to-roman)
* [0058-最后一个单词的长度](./题目目录/0058-length-of-last-word)
* [0014-最长公共前缀](./题目目录/0014-longest-common-prefix)
* [0151-反转字符串中的单词](./题目目录/0151-reverse-words-in-a-string)
* [0006-Z 字形变换](./题目目录/0006-zigzag-conversion)
* [0028-找出字符串中第一个匹配项的下标](./题目目录/0028-find-the-index-of-the-first-occurrence-in-a-string) —— 重点：经典KMP算法
* [0035-搜索插入位置](./题目目录/0035-search-insert-position) —— 重点：二分查找定位插入位置
* [0033-搜索旋转排序数组](./题目目录/0033-search-in-rotated-sorted-array) —— 重点：旋转数组二分，判断哪半有序再决定搜索方向
* [0067-二进制求和](./题目目录/0067-add-binary) —— 重点：双指针模拟竖式加法，逢二进一
* [0068-文本左右对齐](./题目目录/0068-text-justification)

### 🔗 双指针

- [0125-验证回文串](./题目目录/0125-valid-palindrome)
- [0392-判断子序列](./题目目录/0392-is-subsequence)
- [0167-两数之和 II - 输入有序数组](./题目目录/0167-two-sum-ii-input-array-is-sorted)
- [0011-盛最多水的容器](./题目目录/0011-container-with-most-water)
- [0015-三数之和](./题目目录/0015-3sum)

### 🔗 滑动窗口

- [0209-长度最小的子数组](./题目目录/0209-minimum-size-subarray-sum)
- [0003-无重复字符的最长子串](./题目目录/0003-longest-substring-without-repeating-characters)
- [0030-串联所有单词的子串](./题目目录/0030-substring-with-concatenation-of-all-words) —— 重点：计数溢出监控策略
- [0076-最小覆盖子串](./题目目录/0076-minimum-window-substring)

### 🔗 矩阵

- [0036-有效的数独](./题目目录/0036-valid-sudoku)
- [0054-螺旋矩阵](./题目目录/0054-spiral-matrix) —— 重点：向量控制方向
- [0048-旋转矩阵](./题目目录/0048-rotate-image) —— 重点：矩阵分块处理
- [0073-矩阵置零](./题目目录/0048-rotate-image) —— 重点：首列复用与标志位
- [0074-搜索二维矩阵](./题目目录/0074-search-a-2d-matrix) —— 重点：二维矩阵转一维数组的二分查找
- [0289-生命游戏](./题目目录/0289-game-of-life) —— 重点：复合状态编码

### 🔗 哈希表

- [0383-赎金信](./题目目录/0383-ransom-note)
- [0205-同构字符串](./题目目录/0205-isomorphic-strings)
- [0290-单词规律](./题目目录/0290-word-pattern)
- [0242-有效的字母异位词](./题目目录/0242-valid-anagram)
- [0049-字母异位词分组](./题目目录/0049-group-anagrams)
- [0001-两数之和](./题目目录/0001-two-sum)
- [0201-快乐数](./题目目录/0202-happy-number) —— 重点：哈希表检测循环
- [0219-存在重复元素 II](./题目目录/0219-contains-duplicate-ii)
- [0128-最长连续序列](./题目目录/0128-longest-consecutive-sequence)
- [0056-合并区间](./题目目录/0056-merge-intervals)

### 🔗 区间

- [0228-汇总区间](./题目目录/0228-summary-ranges)
- [0056-合并区间](./题目目录/0056-merge-intervals)
- [0057-插入区间](./题目目录/0057-insert-interval)
- [0452-用最少数量的箭引爆气球](./题目目录/0452-minimum-number-of-arrows-to-burst-balloons)

### 🔗 栈

- [0020-有效的括号](./题目目录/0020-valid-parentheses)
- [0071-简化路径](./题目目录/0071-simplify-path)
- [0155-最小栈](./题目目录/0155-min-stack) —— 重点：使用辅助栈优化时间复杂度O(N)->O(1)
- [0150-逆波兰表达式求值](./题目目录/0150-evaluate-reverse-polish-notation) —— 重点：双栈法
- [0224-基本计算器](./题目目录/0224-basic-calculator) —— 重点：括号展开，避免双栈法的复杂逻辑

### 🔗 链表

- [0141-环形链表](./题目目录/0141-linked-list-cycle) —— 快慢指针法(Floy算法)优化空间至O(1)
- [0002-两数相加](./题目目录/0002-add-two-numbers)
- [0021-合并两个有序链表](./题目目录/0021-merge-two-sorted-lists)
- [0138-随机链表的复制](./题目目录/0138-copy-list-with-random-pointer) —— 重点：拆分链表优化空间至O(1)
- [0092-反转链表 II](./题目目录/0092-reverse-linked-list-ii)
- [0025-K 个一组翻转链表](./题目目录/0025-reverse-nodes-in-k-group)
- [0082-删除排序链表中的重复元素 II](./题目目录/0082-remove-duplicates-from-sorted-list-ii)
- [0061-翻转链表](./题目目录/0061-rotate-list)
- [0086-分隔链表](./题目目录/0086-partition-list)
- [0146-LRU缓存](./题目目录/0146-lru-cache)

### 🔗 二叉树

- [0104-二叉树的最大深度](./题目目录/0104-maximum-depth-of-binary-tree)
- [0100-相同的树](./题目目录/0100-same-tree)
- [0226-翻转二叉树](./题目目录/0226-invert-binary-tree)
- [0101-对称二叉树](./题目目录/0101-symmetric-tree)
- [0105-从前序与中序遍历序列构造二叉树](./题目目录/0105-construct-binary-tree-from-preorder-and-inorder-traversal) —— 重点：哈希表映射优化时间复杂度至O(1)
- [0106-从中序与后序遍历序列构造二叉树](./题目目录/0106-construct-binary-tree-from-inorder-and-postorder-traversal)
- [0117-填充每个节点的下一个右侧节点指针 II](./题目目录/0117-populating-next-right-pointers-in-each-node-ii)
- [0114-二叉树展开为链表](./题目目录/0114-flatten-binary-tree-to-linked-list)
- [0112-路径总和](./%E9%A2%98%E7%9B%AE%E7%9B%AE%E5%BD%95/0112-path-sum)
- [0129-求根节点到叶节点数字之和](./题目目录/0129-sum-root-to-leaf-numbers)
- [0124-二叉树中的最大路径和](./题目目录/0124-binary-tree-maximum-path-sum) —— 重点：后序 DFS，区分子树全局最优与可向上延伸的单链
- [0173-二叉搜索树迭代器](./题目目录/0173-binary-search-tree-iterator)
- [0222-完全二叉树的节点个数](./题目目录/0222-count-complete-tree-nodes) —— 重点：左右边界等高则满树 2^h-1，否则分治O(log²n)
- [0236-二叉树的最近公共祖先](./题目目录/0236-lowest-common-ancestor-of-a-binary-tree) —— 重点：后序 DFS，左右子树各找到一个目标则当前根为 LCA
- [0108-将有序数组转换为二叉搜索树](./题目目录/0108-convert-sorted-array-to-binary-search-tree) —— 重点：取中点作根的分治递归，天然高度平衡

### 🔗 二叉树的层次遍历

- [0199-二叉树的右视图](./题目目录/0199-binary-tree-right-side-view) —— 重点：先右后左 DFS，每层首次访问的节点即该层最右可见；亦可用 BFS 取每层最后一个
- [0637-二叉树的层平均值](./题目目录/0637-average-of-levels-in-binary-tree)
- [0102-二叉树的层序遍历](./题目目录/0102-binary-tree-level-order-traversal)
- [0103-二叉树的锯齿形层序遍历](./题目目录/0103-binary-tree-zigzag-level-order-traversal)

### 🔗 二叉树搜索树

- [0530-二叉搜索树的最小绝对差](./题目目录/0530-minimum-absolute-difference-in-bst)
- [0230-二叉搜索树中第 K 小的元素](./题目目录/0230-kth-smallest-element-in-a-bst)
- [0098-验证二叉搜索树](./题目目录/0098-validate-binary-search-tree)

### 🔗 图

- [0200-岛屿数量](./题目目录/0200-number-of-islands)
- [0207-课程表](./题目目录/0207-course-schedule) —— 重点：有向图环检测（三色 DFS）等价于拓扑排序可行性
- [0210-课程表 II](./题目目录/0210-course-schedule-ii) —— 重点：三色 DFS + 后序反转输出拓扑序；有环则返回空
- [0130-被围绕的区域](./题目目录/0130-surrounded-regions)
- [0133-克隆图](./题目目录/0133-clone-graph)
- [0399-除法求值](./题目目录/0399-evaluate-division) —— 重点：带权并查集维护变量间的除法关系

### 🔗 图的广度优先搜索

- [0909-蛇梯棋](./题目目录/0909-snakes-and-ladders) —— 重点：棋盘编号与锯齿坐标映射；掷骰+蛇梯构成隐式图，层序 BFS 求最短路
- [0433-最小基因变化](./题目目录/0433-minimum-genetic-mutation)
- [0127-单词接龙](./题目目录/0127-word-ladder) —— 重点：虚拟节点优化建图时间复杂度

### 🔗 字典树

- [0208-实现Trie(前缀树)](./题目目录/0208-implement-trie-prefix-tree)
- [0211-添加与搜索单词-数据结构设计](./题目目录/0211-design-add-and-search-words-data-structure)
- [0212-单词搜索 II](./题目目录/0212-word-search-ii) —— 重点：构建字典树+剪枝优化

### 🔗 回溯

- [0017-电话号码的字母组合](./题目目录/0017-letter-combinations-of-a-phone-number) —— 重点：按位枚举手机键字母；`append` → 递归 → `pop` 经典回溯模板
- [0077-组合](./题目目录/0077-combinations) —— 重点：倒序选数保证组合不重复；`d = k - len(path)` 剪枝，`path.copy()` 收集答案
- [0046-全排列](./题目目录/0046-permutations) —— 重点：固定前缀下标 `first`，与 `first..n-1` 交换后递归；回溯时换回复位
- [0039-组合总和](./题目目录/0039-combination-sum) —— 重点：排序后 `sum > target` 剪枝；`for i in range(index, n)` 防重复组合，递归传 `i` 允许同一数无限次选取
- [0052-N皇后 II](./题目目录/0052-n-queens-ii) —— 重点：位运算优化空间
- [0022-括号生成](./题目目录/0022-generate-parentheses) —— 重点：回溯中的选与不选
- [0079-单词搜索](./题目目录/0079-word-search)

### 🔗 分治

- [0108-将有序数组转换为二叉搜索树](./题目目录/0108-convert-sorted-array-to-binary-search-tree) —— 重点：取中点作根的分治递归，天然高度平衡
- [0148-排序链表](./题目目录/0148-sort-list) —— 重点：快慢指针找中点切断，分治归并排序链表 O(n log n)
- [0215-数组中的第K个最大元素](./题目目录/0215-kth-largest-element-in-an-array) —— 重点：快速选择算法（三路划分），随机 pivot 实现平均 O(n)
- [0772-建立四叉树](./题目目录/0772-construct-quad-tree) —— 重点：四象限 DFS 分治，四叶子同值则合并压缩
- [0023-合并 K 个升序链表](./题目目录/0023-merge-k-sorted-lists) —— 重点：分治两两归并，每轮链表数减半 O(N log k)

### 🔗 二分查找

- [0004-寻找两个正序数组的中位数](./题目目录/0004-median-of-two-sorted-arrays) —— 重点：二分排除法求第 k 小数，每次排除 k/2 个元素，O(log(m+n))
- [0033-搜索旋转排序数组](./题目目录/0033-search-in-rotated-sorted-array) —— 重点：旋转数组二分，判断哪半有序再决定搜索方向
- [0034-在排序数组中查找元素的第一个和最后一个位置](./题目目录/0034-find-first-and-last-position-of-element-in-sorted-array) —— 重点：lower_bound 一次函数求左右边界，二分定位 target 和 target+1
- [0153-寻找旋转排序数组中的最小值](./题目目录/0153-find-minimum-in-rotated-sorted-array) —— 重点：旋转数组二分，比较 mid 与左端判断哪半有序，递归缩小区间
- [0162-寻找峰值](./题目目录/0162-find-peak-element) —— 重点：二分搜索"爬坡法"，比较 mid 与 mid+1 决定搜索方向

### 🔗 堆（优先队列）

- [0295-数据流的中位数](./题目目录/0295-find-median-from-data-stream) —— 重点：对顶堆（大根堆+小根堆），动态维护数据流中位数，O(log n) 插入
- [0373-查找和最小的 K 对数字](./题目目录/0373-find-k-pairs-with-smallest-sums) —— 重点：小根堆 + 多路归并，隐式矩阵中逐行推进找前 k 小
- [0502-IPO](./题目目录/0502-ipo) —— 重点：贪心 + 大根堆，每轮从可启动项目中选利润最大者

### 🔗 贪心

### 🔗 数学

- [0009-回文数](./题目目录/0009-palindrome-number) —— 重点：字符串对称比较，进阶可用反转一半数字实现 O(1) 空间

### 🔗 位运算

- [0136-只出现一次的数字](./题目目录/0136-single-number) —— 重点：异或运算的自反性消除成对元素
- [0137-只出现一次的数字 II](./题目目录/0137-single-number-ii) —— 重点：两位状态机构建模 3 计数器，消除出现三次的元素
- [0190-颠倒二进制位](./题目目录/0190-reverse-bits) —— 重点：分治法二分翻转，掩码逐层交换位组
- [0191-位1的个数](./题目目录/0191-number-of-1-bits) —— 重点：n & (n - 1) 消除最低位 1
- [0201-数字范围按位与](./题目目录/0201-bitwise-and-of-numbers-range) —— 重点：异或定位差异位，公共前缀掩码一步清零

### 🔗 动态规划

- [0121-买卖股票的最佳时机](./题目目录/0121-best-time-to-buy-and-sell-stock)
- [0122-买卖股票的最佳时机 II](./题目目录/0122-best-time-to-buy-and-sell-stock-ii) —— 重点：贪心优化空间至O(1)
- [0019-删除链表的倒数第 N 个结点](./题目目录/0019-remove-nth-node-from-end-of-list)
- [0053-最大子数组和](./题目目录/0053-maximum-subarray) —— 重点：Kadane 算法，维护以当前位置结尾的最大和与全局最优
- [0954-环形子数组的最大和](./题目目录/0954-maximum-sum-circular-subarray) —— 重点：同时维护最大/最小子数组和，环形情况转化为总和减最小子数组

---

## 📅 全量索引 (Auto-generated by LeetHub)

<!---LeetCode Topics Start-->

# LeetCode Topics

## Array

| Problem Name                                                                                                         | Difficulty |
| -------------------------------------------------------------------------------------------------------------------- | ---------- |
| [0027-remove-element](https://github.com/1218448175/LeetCode-Python-Practice/tree/main/0027-remove-element/)         | undefined  |
| [0088-merge-sorted-array](https://github.com/1218448175/LeetCode-Python-Practice/tree/main/0088-merge-sorted-array/) | undefined  |

## Two Pointers

| Problem Name                                                                                                         | Difficulty |
| -------------------------------------------------------------------------------------------------------------------- | ---------- |
| [0027-remove-element](https://github.com/1218448175/LeetCode-Python-Practice/tree/main/0027-remove-element/)         | undefined  |
| [0088-merge-sorted-array](https://github.com/1218448175/LeetCode-Python-Practice/tree/main/0088-merge-sorted-array/) | undefined  |

## Sorting

| Problem Name                                                                                                         | Difficulty |
| -------------------------------------------------------------------------------------------------------------------- | ---------- |
| [0088-merge-sorted-array](https://github.com/1218448175/LeetCode-Python-Practice/tree/main/0088-merge-sorted-array/) | undefined  |
