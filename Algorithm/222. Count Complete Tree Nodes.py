# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        def getDepth(node):
            if not node:
                return  0
            height = 0
            while node:
                height += 1
                node = node.left
            return height

        res = 0
        while root:
            l = getDepth(root.left)
            r = getDepth(root.right)
            if l == r:
                res += 2 ** l
                root = root.right
            else:
                res += 2 ** r
                root = root.left

 
        return res