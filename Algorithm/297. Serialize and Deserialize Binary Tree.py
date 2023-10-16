import collections
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        if not root:
            return ''

        queue = collections.deque([root])
        while queue:
            cur = queue.popleft()
            if cur:
                res.append(str(cur.val))
                queue.append(cur.left)
                queue.append(cur.right)
            else:
                res.append('N')

        return ','.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None

        data = data.split(',')
        
        root = TreeNode(int(data[0]))
        queue = collections.deque([root])

        i = 1
        while queue:
            cur = queue.popleft()

            if i < len(data) and data[i] != 'N':
                cur.left = TreeNode(int(data[i]))
                queue.append(cur.left)
            i += 1

            if i < len(data) and data[i] != 'N':
                cur.right = TreeNode(int(data[i]))
                queue.append(cur.right)
            i += 1

        return root
        


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))