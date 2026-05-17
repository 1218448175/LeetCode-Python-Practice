class Node:
    def __init__(self):
        self.dict = dict()
        self.end = False

class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.dict:
                cur.dict[c] = Node()
            cur = cur.dict[c]
        cur.end = True
    
    def find(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.dict:
                return 0    # 没有匹配的字符串
            cur = cur.dict[c]
        if cur.end:
            return 2    # 完全匹配
        return 1    # 匹配前缀

    def search(self, word: str) -> bool:
        return self.find(word) == 2

    def startsWith(self, prefix: str) -> bool:
        return self.find(prefix) != 0


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)