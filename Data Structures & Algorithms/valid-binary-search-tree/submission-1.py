# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
    
        def dfs(node, minimum, maximum):
            if not node:
                return True
            isValid = False
            if node.val > minimum and node.val < maximum:
                isValid = True
            
            return isValid and dfs(node.left, minimum, node.val) and dfs(node.right, node.val, maximum)

        return dfs(root, -math.inf, math.inf)