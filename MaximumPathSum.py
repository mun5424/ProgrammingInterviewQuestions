# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        # placeholder for result
        res = float("-inf")

        if root == None:
            return 0

        l = self.maxPathSum(root.left)
        r = self.maxPathSum(root.right)

        max_single  = max(max(l,r) + root.val, root.val)

        max_top = max(max_single, l + r + root.val)

        res = max(res, max_top); 

        print("res is " , res)

        return res

  
testNodeC = TreeNode(1, None, None) 
testNodeD = TreeNode(2, None, None)
testNodeE = TreeNode(3, None, None)
testNodeA = TreeNode(2, testNodeC, testNodeD)
testNodeB = TreeNode(1, testNodeE, testNodeA) 

s = Solution()
#       1(B)
#   3(E)       2(A)
#             1(C) 2(D)
# Maxpath should be 8=3+1+2+3
print(s.maxPathSum(testNodeB)); 
