# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        list=[]
        self.traversal(root,list)
        return list
    def traversal(self,root,list):
        if root is None:
            return
        self.traversal(root.left,list)
        self.traversal(root.right,list)
        list.append(root.val)
        