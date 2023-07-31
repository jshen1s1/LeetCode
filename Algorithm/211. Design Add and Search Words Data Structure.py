class trieNode(object):
    def __init__(self):
        self.next = {}
        self.isEnd = False

class WordDictionary(object):
    def __init__(self):
        self.root = trieNode()

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        cur = self.root
        for c in word:
            if c not in cur.next:
                cur.next[c] = trieNode()
            cur = cur.next[c]
        cur.isEnd = True
        

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        def dfs(node, idx):
            if idx == len(word):
                return node.isEnd
            
            if word[idx] == '.':
                for n in node.next.values():
                    if dfs(n, idx+1):
                        return True
            else:
                if word[idx] in node.next:
                    return dfs(node.next[word[idx]], idx+1)
                
            return False

        return dfs(self.root, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)