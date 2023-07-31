class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        def dfs(i, j, node):
            temp = board[i][j]
            cur = node[temp]
            word = cur.pop('#', False) # Check if the node has a word in it
            if word:
                res.append(word)

            if board[i][j] == '#':
                return

            board[i][j] = '#'
            for dx, dy in [(1,0), (0,1), (-1,0), (0, -1)]:
                newX, newY = i+dx, j+dy
                if 0 <= newX < m and 0 <= newY < n and board[newX][newY] in cur:
                    dfs(newX, newY, cur)
            board[i][j] = temp
            
            # If the current node has no children, remove it from the trie
            if not cur:
                node.pop(temp)

        trie = {}
        for word in words:
            cur = trie
            for letter in word:
                cur = cur.setdefault(letter, {})
            cur['#'] = word
        

        res = []
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] in trie:
                    dfs(i, j, trie)

        return res