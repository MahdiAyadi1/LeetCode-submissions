# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isUnivalTree(self, root):
        if root.left == None and root.right == None : 
            return True
        elif root.right != None and root.left != None :
            return root.val == root.right.val and root.val == root.left.val and self.isUnivalTree(root.right) and self.isUnivalTree(root.left)
        elif root.left != None :
            return root.val == root.left.val and self.isUnivalTree(root.left)
        elif root.right != None :
            return root.val == root.right.val and self.isUnivalTree(root.right)
        