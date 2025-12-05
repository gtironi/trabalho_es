# =================================
# Composite Demo
# =================================

from tree_design import LeafNode, DecisionNode

tree = DecisionNode(50)

branch1 = DecisionNode(25)
branch2 = DecisionNode(75)

leaf1 = LeafNode("Rosa")
leaf2 = LeafNode("Rosa")
leaf3 = LeafNode("Verde")
leaf4 = LeafNode("Verde")

branch1.add(leaf1)
branch1.add(leaf2)
branch2.add(leaf3)
branch2.add(leaf4)

tree.add(branch1)
tree.add(branch2)

print(tree.operation(25)) # Rosa
print(tree.operation(75)) # Verde
print(tree.operation(10)) # Rosa
print(tree.operation(30)) # Rosa
print(tree.operation(60)) # Verde
print(tree.operation(90)) # Verde
