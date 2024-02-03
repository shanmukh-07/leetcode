# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        st = []
        def postorder(root,st):
            if not root:
                return None
            postorder(root.left,st)
            postorder(root.right,st)
            st.append(root.val)
        postorder(root,st)
        return st