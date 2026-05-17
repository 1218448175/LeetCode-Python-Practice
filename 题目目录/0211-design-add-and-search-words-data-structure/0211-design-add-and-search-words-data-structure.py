class Node:
    def __init__(self):
        self.dict = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.dict:
                cur.dict[c] = Node()
            cur = cur.dict[c]
        cur.end = True

    def dfs(self, cur: str, word: str, i: int) -> bool:
        ans = False
        if i >= len(word):
            return cur.end
        c = word[i]
        if c == ".":
            for node in cur.dict.values():
                ans = ans or self.dfs(node, word, i + 1)
            return ans
        if c not in cur.dict:
            return False
        return self.dfs(cur.dict[c], word, i + 1)

    def search(self, word: str) -> bool:
        return self.dfs(self.root, word, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)