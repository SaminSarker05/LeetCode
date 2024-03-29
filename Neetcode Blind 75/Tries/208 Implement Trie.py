class Trie:
    class TrieNode:
        def __init__(self):
            self.children = {}
            self.isEnd = False

    def __init__(self):
        self.root = Trie.TrieNode()
        

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = Trie.TrieNode()
            curr = curr.children[char]
        
        curr.isEnd = True

        
    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.isEnd
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return True
        