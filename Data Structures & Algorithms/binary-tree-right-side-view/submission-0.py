# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        queue = collections.deque()
        queue.append(root)
        while queue:
            lvl = []
            for _ in range(len(queue)):
                cur = queue.popleft()
                if cur:
                    queue.append(cur.left), queue.append(cur.right)
                    lvl.append(cur.val)

            if lvl:
                res.append(lvl[-1])
            
        return res