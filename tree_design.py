from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

# =================================
# Composite Pattern
# =================================

class Node(ABC):
    @property
    def parent(self) -> Node:
        return self._parent

    @parent.setter
    def parent(self, parent: Node):
        self._parent = parent

    def add(self, component: Node):
        pass

    def remove(self, component: Node):
        pass

    def is_composite(self) -> bool:
        return False

    @abstractmethod
    def operation(self) -> str:
        pass

class LeafNode(Node):
    def __init__(self, category: str):
        super().__init__()
        self._category = category

    def operation(self):
        return f"Leaf: {self._category}"

class DecisionNode(Node):
    def __init__(self, threshold: float):
        super().__init__()
        self._children: List[Node] = []
        self._threshold = threshold

    def add(self, component: Node):
        self._children.append(component)
        component.parent = self

    def remove(self, component: Node):
        self._children.remove(component)
        component.parent = None

    def is_composite(self) -> bool:
        return True

    def operation(self, value: float):
        if value < self._threshold:
            return self._children[0].operation()
        else:
            return self._children[1].operation()

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
