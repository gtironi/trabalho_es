from __future__ import annotations
from abc import ABC, abstractmethod
from collections.abc import Iterator
from typing import List
import random

# =================================
# Composite Pattern
# =================================

class Node(ABC):
    def __init__(self, order: int):
        self.order = order
        self._parent = None

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

    @abstractmethod
    def accept(self, visitor):
        pass

class LeafNode(Node):
    def __init__(self, category: str, order: int):
        super().__init__(order)
        self._category = category

    def operation(self, value: float) -> str:
        return f"Leaf: {self._category}"

    def accept(self, visitor):
        visitor.visit_leaf_node(self)

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

    def accept(self, visitor):
        visitor.visit_decision_node(self)

# =================================
# State Pattern
# =================================

class Tree:


    def __init__(self, root: Node):
        self.root = root
        self.set_state(SplittingState())
        self.iterator = None

    def operation(self, value: float) -> str:
        return self.root.operation(value)

    def __iter__(self) -> Iterator[Node]:
        return self.iterator

    def set_iterator(self, iterator: Iterator[Node]):
        self.iterator = iterator

    def set_state(self, state: State):
        self._state = state
        state.context = self

class TreeBuilder:
    @property
    def tree(self) -> Tree:
        return self._tree

    @tree.setter
    def tree(self, tree: Tree):
        self._tree = tree

    def construct(self):
        index = [0]  # Lista para poder modificar dentro dos estados
        root = DecisionNode(50, index[0])
        self.tree = Tree(root)
        iterator = BFSIterator(root)

        try:
            for node in iterator:
                # Sempre executa o estado atual
                self.tree._state.execute(node, index, self.tree)

                # Adiciona filhos à fila do iterator
                if node.is_composite():
                    for filho in node.get_children():
                        iterator._queue.append(filho)
        except StopIteration:
            pass  # StoppingState termina o loop

class State(ABC):
    @property
    def context(self) -> Tree:
        return self._context

    @context.setter
    def context(self, tree: Tree):
        self._context = tree

    @abstractmethod
    def execute(self, node: Node, index: List[int], tree: Tree):
        pass


class SplittingState(State):
    def execute(self, node: Node, index: List[int], tree: Tree):
        print(f"[SplittingState] Executando: {node.order}")
        # Split: divide o nó se for composite sem filhos
        if node.is_composite() and len(node.get_children()) == 0:
            index[0] += 1
            left_branch = DecisionNode(25, index[0])
            index[0] += 1
            right_branch = DecisionNode(75, index[0])
            node.add(left_branch)
            node.add(right_branch)

        # Verifica mudança de estado
        if random.random() > 0.8:
            tree.set_state(PruningState())
            print(f"Mudando para PruningState")

class PruningState(State):
    def execute(self, node: Node, index: List[int], tree: Tree):
        print(f"[PruningState] Executando: {node.order}")
        # Prune: remove nós sem filhos
        if len(node.get_children()) == 0:
            parent = node._parent if hasattr(node, '_parent') else None
            if parent is not None and isinstance(parent, DecisionNode):
                if random.random() < 0.5:
                    print(f"[PruningState] Removendo nó: {node.order}")
                    parent.remove(node)

            # Verifica mudança de estado
            if random.random() < 0.4:
                tree.set_state(StoppingState())
                print(f"Mudando para StoppingState")

class StoppingState(State):
    def execute(self, node: Node, index: List[int], tree: Tree):
        print(f"[StoppingState] Executando...")
        # Stop: adiciona folhas em todos os nós sem filhos
        iterator = BFSIterator(tree.root)
        for n in iterator:
            if n.is_composite() and len(n.get_children()) == 0:
                index[0] += 1
                n.add(LeafNode("Rosa", index[0]))
                index[0] += 1
                n.add(LeafNode("Verde", index[0]))
        # Para o loop quando chega no StoppingState
        raise StopIteration


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

        if node.is_composite() and hasattr(node, 'get_children'):
            children = node.get_children()
            # Adiciona na ordem inversa para processar esquerda primeiro (LIFO)
            for child in reversed(children):
                self._stack.append(child)

        return node

class BFSIterator(Iterator):
    def __init__(self, root: Node):
        self._queue = [root] if root else []

    def __iter__(self):
        return self

    def __next__(self):
        if not self._queue:
            raise StopIteration

        node = self._queue.pop(0)

        if node.is_composite() and hasattr(node, 'get_children'):
            children = node.get_children()
            # Adiciona os filhos no final da fila
            for child in children:
                self._queue.append(child)

        return node


# =================================
# Visitor Pattern
# =================================

class Visitor(ABC):
    """Interface do Visitor"""

    @abstractmethod
    def visit_decision_node(self, element: DecisionNode) -> None:
        pass

    @abstractmethod
    def visit_leaf_node(self, element: LeafNode) -> None:
        pass

class DepthVisitor(Visitor):
    def __init__(self, root: Node):
        self.root = root
        self.max_depth = 0

    def visit_decision_node(self, element: DecisionNode) -> None:
        """Visita DecisionNode"""
        depth = self._calculate_depth(element)
        if depth > self.max_depth:
            self.max_depth = depth
        # print(f"[DepthVisitor] Visitando DecisionNode {element.order} na profundidade {depth}")

    def visit_leaf_node(self, element: LeafNode) -> None:
        """Visita LeafNode"""
        depth = self._calculate_depth(element)
        if depth > self.max_depth:
            self.max_depth = depth
        # print(f"[DepthVisitor] Visitando LeafNode {element.order} na profundidade {depth}")

    def _calculate_depth(self, node: Node) -> int:
        """Calcula profundidade de um nó"""
        depth = 0
        current = node
        while current is not None and hasattr(current, '_parent'):
            if hasattr(current, '_parent') and current._parent is not None:
                depth += 1
                current = current._parent
            else:
                break
        return depth

    def get_result(self) -> int:
        return self.max_depth

class CountLeavesVisitor(Visitor):
    def __init__(self, root: Node):
        self.root = root
        self.count = 0

    def visit_decision_node(self, element: DecisionNode) -> None:
        """Visita DecisionNode """
        # print(f"[CountLeavesVisitor] Visitando DecisionNode {element.order}")

    def visit_leaf_node(self, element: LeafNode) -> None:
        """Visita LeafNode """
        self.count += 1
        # print(f"[CountLeavesVisitor] Encontrada folha: nó {element.order}")

    def get_result(self) -> int:
        return self.count
