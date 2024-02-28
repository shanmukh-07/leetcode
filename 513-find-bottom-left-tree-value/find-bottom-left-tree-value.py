# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        def fun(n,p):
            if n:
                q = max((0,3,n.val),fun(n.left,2),fun(n.right,1))
                return (q[0]+1,p,q[2])
            return (0,0,0)
        return fun(root,0)[2]