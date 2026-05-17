class Node:
    def __init__(self):
        self.dict = {}
        # 直接存储单词，既能当 end 标志，又免去了字符串拼接
        self.word = None  

class Trie:
    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.dict:
                cur.dict[c] = Node()
            cur = cur.dict[c]
        cur.word = word  # 存入完整单词

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # 1. 构建 Trie 树
        trie = Trie()
        for word in words:
            trie.addWord(word)
        
        root = trie.root
        ans = []
        m, n = len(board), len(board[0])

        # 2. 定义内置 DFS 函数，减少 self 调用开销
        def dfs(r: int, c: int, parent_node: Node):
            char = board[r][c]
            cur_node = parent_node.dict[char]

            # 如果找到了一个单词
            if cur_node.word:
                ans.append(cur_node.word)
                cur_node.word = None  # 置空防止重复添加，代替了原先的 flag 逻辑

            # 原地标记已访问
            board[r][c] = '#'

            # 探索四个方向
            for x, y in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if 0 <= x < m and 0 <= y < n and board[x][y] in cur_node.dict:
                    dfs(x, y, cur_node)

            # 回溯恢复现场
            board[r][c] = char

            # 【核心优化：剪枝】如果当前节点没有任何子节点了，说明这个分支已经搜干榨净，从父节点中剔除它
            if not cur_node.dict:
                parent_node.dict.pop(char)

        # 3. 遍历网格
        for r in range(m):
            for c in range(n):
                if board[r][c] in root.dict:
                    dfs(r, c, root)

        return ans