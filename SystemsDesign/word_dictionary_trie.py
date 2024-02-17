class TrieNode:
    def __init__(self):
        self.trie = {} # a : TrieNode
        self.word = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.trie:
                cur.trie[c] = TrieNode()
            cur = cur.trie[c]
        cur.word = True

    def search(self, word: str) -> bool:
        def dfs(j, root) -> bool:
            cur = root

            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in cur.trie.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in cur.trie:
                        return False
                cur = cur.trie[c]
            return cur.word

        return dfs(0, self.root)
