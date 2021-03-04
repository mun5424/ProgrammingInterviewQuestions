
class BinaryTree:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None 

# recursive dfs
def invertBinaryTree(tree: BinaryTree):
    if tree == None: 
        return 0
    if tree.right:

    return max(invertBinaryTree(tree.left), invertBinaryTree(tree.right))