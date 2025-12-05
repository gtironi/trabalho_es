from __future__ import annotations
from abc import ABC, abstractmethod
from collections.abc import Iterable, Iterator
from typing import List

# =================================
# Composite Pattern
# =================================

class Node(ABC):
    def __init__(self, order: int):
        self.order = order

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
    def __init__(self, category: str, order: int):
        super().__init__(order)
        self._category = category

    def operation(self, value: float) -> str:
        return f"Leaf: {self._category}"

class DecisionNode(Node):
    def __init__(self, threshold: float, order: int):
        super().__init__(order)
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

    def get_children(self) -> List[Node]:
        return self._children

    def operation(self, value: float):
        if value < self._threshold:
            return self._children[0].operation(value)
        else:
            return self._children[1].operation(value)

# =================================
# State Pattern
# =================================

class Tree:
    def __init__(self, root: Node = None):
        self.root = root
        self.iterator = PreOrderIterator(self.root) if root else None

    def operation(self, value: float) -> str:
        return self.root.operation(value)

    def __iter__(self) -> Iterator[Node]:
        return self.iterator

    def change_iterator(self, iterator: Iterator[Node]):
        self.iterator = iterator

class TreeBuilder:
    _state: None

    def __init__(self, state: State) -> None:
        self.set_state(state)
        self._tree: Tree = Tree()

    def set_state(self, state: State):
        self._state = state
        self._context = self

    def execute(self):
        self._state.execute()

    @property
    def tree(self) -> Tree:
        return self._tree

    @tree.setter
    def tree(self, tree: Tree):
        self._tree = tree

class State(ABC):
    @property
    def context(self) -> TreeBuilder:
        return self._context

    @context.setter
    def context(self, tree: TreeBuilder):
        self._context = tree

    @abstractmethod
    def execute(self):
        pass


class SplitState(State):
    def execute(self):
        random.choice([0,1])
        self.context.tree.root.add(DecisionNode(random.random()))

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
    def __init__(self, root: Node):
        self._stack = [root] if root else []

    def __iter__(self):
        return self

    def __next__(self):
        if not self._stack:
            raise StopIteration

        node = self._stack.pop()
        print(f"[PreOrderIterator] Visitando: {node.order}")

        if node.is_composite() and hasattr(node, 'get_children'):
            children = node.get_children()
            # Adiciona na ordem inversa para processar esquerda primeiro (LIFO)
            for child in reversed(children):
                self._stack.append(child)

        return node

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
