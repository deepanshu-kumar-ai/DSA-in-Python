class TreeNode:
    def __init__(self, data):
        self.data=data
        self.left = None
        self.right = None
 
def max_ele(root):
    if root is None:
        return float('-inf')  # base case

    lef_node = max_ele(root.left)     
    rig_node = max_ele(root.right)    
    max_val = root.data

    if lef_node > max_val:
        max_val = lef_node
    if rig_node > max_val:
        max_val = rig_node

    return max_val

# Building the tree
root = TreeNode(26)
nodeA = TreeNode(21)
nodeB = TreeNode(20)
nodeC = TreeNode(5)
nodeD = TreeNode(54)
nodeE = TreeNode(98)
nodeF = TreeNode(98)
nodeG = TreeNode(81)

# linking the nodes 
root.right = nodeA
root.left = nodeB

nodeA.right = nodeC
nodeA.left = nodeE

nodeB.left = nodeG

print("the max value is:", max_ele(root))
