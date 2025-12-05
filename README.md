# Projeto Individual de Modelagem – Árvore de Decisão

Este projeto implementa uma árvore de decisão simplificada utilizando quatro padrões de projeto fundamentais:

- **Composite**: DecisionNode contém threshold e filhos, enquanto LeafNode armazena categoria. A operação percorre recursivamente comparando valores com thresholds até encontrar uma folha que retorna a categoria. Implementado através da classe abstrata Node com métodos add/remove, onde DecisionNode gerencia filhos e LeafNode é terminal.

- **Iterator**: PreOrderIterator utiliza pilha (LIFO) para percorrer em pré-ordem, BFSIterator usa fila (FIFO) para percorrer em largura. Ambos são utilizados pelo TreeBuilder durante a construção e nas demonstrações. Implementados como iteradores Python que seguem o protocolo Iterator, permitindo uso com for loops.

- **Visitor**: DepthVisitor calcula a profundidade máxima da árvore, CountLeavesVisitor conta o total de folhas. Cada nó aceita o visitor através do método accept, que chama visit_decision_node ou visit_leaf_node conforme o tipo. Implementado com interface Visitor abstrata e dupla despacho através do método accept em cada nó.

- **State**: TreeBuilder gerencia três estados: SplittingState divide nós sem filhos, PruningState remove nós vazios e StoppingState adiciona folhas e finaliza a construção. As transições entre estados ocorrem aleatoriamente durante o processo. Implementado com classe State abstrata onde cada estado possui método execute que modifica a árvore e pode alterar o estado do contexto.

## Estrutura

- `tree_design.py`: Implementação dos padrões de projeto
- `tree_demo.py`: Exemplos de uso e demonstrações

## Como executar

```bash
python tree_demo.py
```

## Funcionalidades

- Criação de árvores de decisão com nós compostos e folhas
- Iteração em pré-ordem e em largura (BFS)
- Cálculo de profundidade máxima e contagem de folhas
- Construção dinâmica da árvore com estados de divisão, poda e parada

## Colaboradores

- Gustavo Tironi ([@gtironi](https://github.com/gtironi))
