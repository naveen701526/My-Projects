class WordDictionary:

    def __init__(self):
        self.d = dict()

    def addWord(self, word: str) -> None:
        if len(word) not in self.d:
            self.d[len(word)] = set()
        self.d[len(word)].add(word)

    def search(self, word: str) -> bool:
        if len(word) not in self.d:
            return False
        
        if '.' in word:
            for w in self.d[len(word)]:
                res = True
                for i in range(len(w)):
                    if word[i] != '.' and word[i] != w[i]:
                        res = False
                        break
                if res:
                    return res
            return False
        else:
            if word in self.d[len(word)]:
                return True
            return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
