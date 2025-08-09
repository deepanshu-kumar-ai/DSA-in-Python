from collections import deque

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# making individual node and inserting the data
root = TreeNode("R")

nodeA = TreeNode("A")
nodeB = TreeNode("B")
nodeC = TreeNode("C")
nodeD = TreeNode("D")
nodeE = TreeNode("E")
nodeF = TreeNode("F")
nodeG = TreeNode("G")

# linking the nodes 
root.right = nodeA
root.left = nodeB

nodeA.right = nodeC
nodeA.left = nodeE

nodeB.left = nodeG

# tree traversal

# inorder traversal
def inorder_tra(TreeNode):
    if TreeNode is None:
        return
    inorder_tra(TreeNode.left)
    print(TreeNode.data, end=" ")
    inorder_tra(TreeNode.right)

# preorder traversal
def preorder_tra(TreeNode):
    if TreeNode is None:
        return
    print(TreeNode.data, end=" ")
    preorder_tra(TreeNode.left)
    preorder_tra(TreeNode.right)

# postorder traversal
def postorder_tra(TreeNode):
    if TreeNode is None:
        return
    postorder_tra(TreeNode.left)
    postorder_tra(TreeNode.right)
    print(TreeNode.data, end=" ")

# breadth search first
def breadth_search_first(TreeNode):
    if TreeNode is None:
        return
    
    queue = deque()
    queue.append(TreeNode)
    
    while queue:
        current = queue.popleft()
        print(current.data, end=" ")
        
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

# run all traversals
print("Inorder Traversal:")
inorder_tra(root)
print("\nPreorder Traversal:")
preorder_tra(root)
print("\nPostorder Traversal:")
postorder_tra(root)
print("\nBreadth Search First Traversal:")
breadth_search_first(root)
