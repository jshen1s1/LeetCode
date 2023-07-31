class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        t = self.root
        for c in word:
            if c not in t.children:
                t.children[c] = TrieNode()
            t = t.children[c]
        
        t.isEnd = True


    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        t = self.root            
        for c in word:
            if c not in t.children:
                return False
            t = t.children[c]

        return t.isEnd
        

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        t = self.root
        for c in prefix:
            if c not in t.children:
                return False
            t = t.children[c]
        
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)