# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, maximum):
            res = 0
            if not node:
                return 0
            newMax = maximum
            if node.val >= maximum:
                newMax = node.val
                return 1 + dfs(node.left, newMax) + dfs(node.right, newMax)
            
            return res + dfs(node.left, newMax) + dfs(node.right, newMax)
        
        
        return dfs(root, -101)