## [133. 克隆图](https://leetcode.cn/problems/clone-graph/)

### 中等

给你无向 [连通](https://baike.baidu.com/item/%E8%BF%9E%E9%80%9A%E5%9B%BE/6460995?fr=aladdin) 图中一个节点的引用，请你返回该图的 [**深拷贝**](https://baike.baidu.com/item/%E6%B7%B1%E6%8B%B7%E8%B4%9D/22785317?fr=aladdin)（克隆）。

图中的每个节点都包含它的值 `val`（`int`） 和其邻居的列表（`list[Node]`）。

> class Node {
>     public int val;
>     public List<Node> neighbors;
> }

**测试用例格式：**

简单起见，每个节点的值都和它的索引相同。例如，第一个节点值为 1（`val = 1`），第二个节点值为 2（`val = 2`），以此类推。该图在测试用例中使用邻接列表表示。

**邻接列表** 是用于表示有限图的无序列表的集合。每个列表都描述了图中节点的邻居集。

给定节点将始终是图中的第一个节点（值为 1）。你必须将 **给定节点的拷贝** 作为对克隆图的引用返回。

**示例 1：**

<p><img alt="" src="https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/02/01/133_clone_graph_question.png" style="height: 500px; width: 500px;"></p>

<pre><strong>输入：</strong>adjList = [[2,4],[1,3],[2,4],[1,3]]
<strong>输出：</strong>[[2,4],[1,3],[2,4],[1,3]]
<strong>解释：
</strong>图中有 4 个节点。
节点 1 的值是 1，它有两个邻居：节点 2 和 4 。
节点 2 的值是 2，它有两个邻居：节点 1 和 3 。
节点 3 的值是 3，它有两个邻居：节点 2 和 4 。
节点 4 的值是 4，它有两个邻居：节点 1 和 3 。
</pre>

---

## 题解：哈希表辅助的深度优先搜索（DFS）深拷贝

### 1. 核心思路：解决循环引用与重复访问

图的深拷贝与树的深拷贝最大的不同在于：图可能存在**环**，且同一个节点可能被多个节点指向。

你的代码采用了一种非常标准且高效的 **DFS + 哈希表** 策略：

- **哈希表的作用**：`visited` 哈希表用于建立“原节点”到“克隆节点”的映射。它有两个核心功能：
  
  1. **去重**：防止进入死循环（处理环）。
  
  2. **复用**：当再次遇到同一个原节点时，直接返回已经创建好的克隆节点。

- **递归逻辑**：先创建当前节点，将其存入哈希表，然后再递归地去克隆所有的邻居。

---

### 2. 执行逻辑的详细拆解

#### A. 缓存查找（防止死循环）

Python

```
if node in self.visited:
    return self.visited[node]
```

这是处理图结构的“生命线”。如果没有这一步，对于一个环状图（如 A-B-A），递归将永无止境。

#### B. 节点的“影子”创建

Python

```
clone_node = Node(node.val, [])
self.visited[node] = clone_node
```

- 注意这里**必须先存入哈希表，再进行递归**。因为在克隆邻居的过程中，邻居可能会反过来引用当前节点。如果先递归再存哈希表，依然会发生栈溢出。

#### C. 邻居的递归克隆

Python

```
clone_node.neighbors = [self.cloneGraph(n) for n in node.neighbors]
```

- 这一行代码优雅地利用了列表推导式。对于原节点的每一个邻居 `n`，调用 `cloneGraph(n)` 获取其对应的克隆节点。

---

### 3. 算法可视化

想象一个简单的三角形图：1-2, 2-3, 3-1。

1. **克隆 1**：创建克隆 1，存入哈希表 `{1: 克 1}`。开始克隆邻居 2。

2. **克隆 2**：创建克隆 2，存入哈希表 `{1: 克 1, 2: 克 2}`。开始克隆邻居 3。

3. **克隆 3**：创建克隆 3，存入哈希表 `{1: 克 1, 2: 克 2, 3: 克 3}`。
   
   - 克隆 3 的邻居有 1 和 2。
   
   - 访问 1 时，哈希表已有“克 1”，直接返回引用。
   
   - 访问 2 时，哈希表已有“克 2”，直接返回引用。

4. **回溯**：各层递归依次完成邻居列表的填充。

---

### 4. 复杂度分析

- **时间复杂度**：$O(N + E)$。其中 $N$ 是节点数，$E$ 是边数。每个节点和每条边都会被访问一次。

- **空间复杂度**：$O(N)$。哈希表需要存储 $N$ 个节点的映射，且递归栈在最坏情况下（图退化为链）深度为 $N$。

---

### 5. 代码回顾

```python
class Solution:
    def __init__(self):
        self.visited = {}

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        if node in self.visited:
            return self.visited[node]

        # 创建新节点并立即记录，解决循环引用
        clone_node = Node(node.val)
        self.visited[node] = clone_node

        # 递归处理邻居
        for neighbor in node.neighbors:
            clone_node.neighbors.append(self.cloneGraph(neighbor))

        return clone_node
```