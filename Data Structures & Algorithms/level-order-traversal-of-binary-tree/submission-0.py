# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = []
        queue.append(root)
        res = []
        while queue:
            lvl = []
            for _ in range(len(queue)):
                cur = queue.pop(0)
                if cur:
                    queue.append(cur.left), queue.append(cur.right)
                    lvl.append(cur.val)
            if lvl:
                res.append(lvl)
        
        return res