# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return
            
        root = preorder[0]
        pos = inorder.index(root)
        leftin = inorder[:pos]
        rightin = inorder[pos+1:]
        leftpre = preorder[1:pos+1]
        rightpre = preorder[pos+1:]

        tree = TreeNode(root)
        tree.left = self.buildTree(leftpre, leftin)
        tree.right = self.buildTree(rightpre, rightin)

        return tree