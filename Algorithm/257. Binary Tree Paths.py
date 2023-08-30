# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        def dfs(node, path, res):
            if not node.left and not node.right:
                res.append(path + str(node.val))
            if node.left:
                dfs(node.left, path + str(node.val) + '->', res)
            if node.right:
                dfs(node.right, path + str(node.val) + '->', res)

        res = []
        dfs(root, "", res)
        return res