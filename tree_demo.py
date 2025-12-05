# =================================
# Composite Demo
# =================================

from tree_design import LeafNode, DecisionNode

tree = DecisionNode(50, 1)

branch1 = DecisionNode(25, 2)
branch2 = DecisionNode(75, 3)

leaf1 = LeafNode("Rosa", 4)
leaf2 = LeafNode("Rosa", 5)
leaf3 = LeafNode("Verde", 6)
leaf4 = LeafNode("Verde", 7)

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

# =================================
# Iterator Demo
# =================================

from tree_design import Tree, PreOrderIterator

# Cria uma árvore para teste
root = DecisionNode(50, 1)
left_branch = DecisionNode(25, 2)
right_branch = DecisionNode(75, 3)

left_leaf1 = LeafNode("Rosa", 4)
left_leaf2 = LeafNode("Rosa", 5)
right_leaf1 = LeafNode("Verde", 6)
right_leaf2 = LeafNode("Verde", 7)

left_branch.add(left_leaf1)
left_branch.add(left_leaf2)
right_branch.add(right_leaf1)
right_branch.add(right_leaf2)

root.add(left_branch)
root.add(right_branch)

tree_obj = Tree(root)

print("\n=== PreOrderIterator ===")
iterator = PreOrderIterator(root)
for node in iterator:
    pass  # Os prints já são feitos dentro do __next__
