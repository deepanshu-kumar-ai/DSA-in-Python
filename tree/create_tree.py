# Binary tree creation

# scalaten of the node
class TreeNode:
    def __init__(self, data):
        self.data=data
        self.left = None
        self.right = None

# making individual node and insering the data
root = TreeNode("R")

nodeA = TreeNode("A")
nodeB = TreeNode("B")
nodeC = TreeNode("C")
nodeD = TreeNode("D")
nodeE = TreeNode("E")
nodeF = TreeNode("F")
nodeG = TreeNode("G")

# linking the nodes 
root.right= nodeA
root.left = nodeB

nodeA.right = nodeC
nodeA.left = nodeE

nodeB.left = nodeG


# print(nodeA)
print("root.right.left.data:", root.right.left.data)