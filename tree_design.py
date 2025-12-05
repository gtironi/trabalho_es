# =================================
# Composite Pattern
# =================================

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def remove_child(self, child_node):
        self.children.remove(child_node)

class DecisionNode(Node):
    def __init__(self, value, question):
        super().__init__(value)
        self.question = question

    def make_decision(self, answer):
        if answer == "yes":
            return self.children[0]
        else:
            return self.children[1]

class LeafNode(Node):
    def __init__(self, value, result):
        super().__init__(value)
        self.result = result

# =================================
# State Pattern
# =================================

class TreeBuilder:
    def __init__(self):
        self.root = None

    def build_tree(self):
        self.root = DecisionNode("root", "Is it a mammal?")
        self.root.add_child(LeafNode("dog", "Woof"))
        self.root.add_child(LeafNode("bird", "Tweet"))
        return self.root

    def get_root(self):
        return self.root

class State:
    def __init__(self, tree):
        self.tree = tree

class SplitState(State):
    def __init__(self, tree):
        super().__init__(tree)
        self.tree = tree


class StoppingState(State):
    def __init__(self, tree):
        super().__init__(tree)
        self.tree = tree

class PruningState(State):
    def __init__(self, tree):
        super().__init__(tree)
        self.tree = tree

# =================================
# Iterator Pattern
# =================================

class PreOrderIterator:
    def __init__(self, tree):
        self.tree = tree

    def __iter__(self):
        return self

    def __next__(self):
        return self.tree.make_decision(answer)

class BFSIterator:
    def __init__(self, tree):
        self.tree = tree

    def __iter__(self):
        return self

    def __next__(self):
        return self.tree.make_decision(answer)

# =================================
# Visitor Pattern
# =================================

class DeepVisitor:
    def __init__(self, tree):
        self.tree = tree

    def visit(self, node):
        return node.make_decision(answer)

class CountLeavesVisitor:
    def __init__(self, tree):
        self.tree = tree

    def visit(self, node):
        return node.make_decision(answer)

class CountNodesVisitor:
    def __init__(self, tree):
        self.tree = tree

    def visit(self, node):
        return node.make_decision(answer)
