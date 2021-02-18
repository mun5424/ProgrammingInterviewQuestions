# invert a binary tree

#  5
# 2 1
#1 3 5

#  5
# 1 2
#5 3 1

class BinaryTree:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None 

# recursive dfs
def invertBinaryTree(tree):
    if tree == None:
        return None
    
    left = tree.left
    right = tree.right 
    tree.left = invertBinaryTree(right)
    tree.right = invertBinaryTree(left) 

    return tree