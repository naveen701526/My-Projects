class TrieNode(object):
    def __init__(self, word=''):
        self.word = ''
        self.children = {}
        self.isComplete = False
        
class Trie:
    def __init__(self, word=''):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode('')
        
    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        if not word:
            return
        
        root = self.root
        
        for c in word:
            if c not in root.children:
                root.children[c] = TrieNode(c)
                
            root = root.children[c]
        root.isComplete = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        if not word:
            return
        
        root = self.root
        
        for c in word:
            if root.isComplete:
                return True
            
            if c not in root.children:
                return False
            
            root = root.children[c]
        return root.isComplete == True
    
from collections import deque

class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie('')
        for word in words:
            self.trie.insert(word[::-1])
        self.stream = deque([])

    def query(self, letter: str) -> bool:
        self.stream.appendleft(letter)
        
        return self.trie.search(self.stream)


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
