from __future__ import annotations
from abc import ABC, abstractmethod
from collections.abc import Iterable, Iterator
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
    def operation(self, value: float) -> str:
        pass

class LeafNode(Node):
    def __init__(self, category: str):
        super().__init__()
        self._category = category

    def operation(self, value: float) -> str:
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
            return self._children[0].operation(value)
        else:
            return self._children[1].operation(value)

# =================================
# State Pattern
# =================================

class Tree:
    def __init__(self, root: Node):
        self.root = root
        self.iterator = PreOrderIterator(self.root)

    def operation(self, value: float) -> str:
        return self.root.operation(value)

    def __iter__(self) -> Iterator[Node]:
        return self.iterator

    def change_iterator(self, iterator: Iterator[Node]):
        self.iterator = iterator

class TreeBuilder:
    def __init__(self):
        self.state = None
        self.tree = None

    def set_state(self, state: State):
        self.state = state
        state.construct_tree = self.tree

    def execute(self):
        self.state.execute()


class State(ABC):
    @property
    def construct_tree(self) -> Tree:
        return self._context

    @construct_tree.setter
    def construct_tree(self, tree: Tree):
        self._context = tree

    @abstractmethod
    def execute(self):
        pass


class SplitState(State):
    def execute(self):
        pass

class StoppingState(State):
    def execute(self):
        pass

class PruningState(State):
    def execute(self):
        pass

# =================================
# Iterator Pattern
# =================================

class PreOrderIterator(Iterator):
    def __init__(self, tree):
        self.tree = tree
        self._current = tree

    def __iter__(self):
        return self

    def __next__(self):
        pass

class BFSIterator(Iterator):
    def __init__(self, tree):
        self.tree = tree

    def __iter__(self):
        return self

    def __next__(self):
        pass


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
