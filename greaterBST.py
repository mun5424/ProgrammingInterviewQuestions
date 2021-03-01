# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.

# As a reminder, a binary search tree is a tree that satisfies these constraints:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        if root == None:
            return None
        
        if not root.left and not root.right: 
            return root
        if root.right:
            rightNode = self.convertBST(root.right)

        if root.left: 
            leftNode = self.convertBST(root.left)

        root.val += leftNode.val + rightNode.val

        return root 
