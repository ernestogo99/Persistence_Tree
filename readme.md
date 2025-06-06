## Trabalho de estrutura de dados avançada

Este projeto é uma implementação de uma árvore binária com persistência parcial
feito em python.

## Equipe

Ernesto Dalva 
Diego Rabelo
Diogo Santiago


## Como rodar o projeto

Entre dentro da pasta src com seu terminal e execute o comando abaixo

```
python main.py in.txt
```

## Estrutura de pastas

```
src/
├── list/
│   └── lista.py         # Classe Lista com Lógica de persistência parcial  
├── tree/
│   ├── node.py                        # Classe Node da árvore binária com modificações
│   ├── fields.py                      # Enum ou constantes para campos modificáveis  
│   ├── bintree.py                     # Classe da árvore binária com persistência parcial
│   └── registry.py                    # Classe que Registra  versões da árvore
├── main.py                            # Execução/testes das funcionalidades
├── in.txt                             # Entrada de testes (valores a inserir, comandos)
└── out.txt                            # Saída esperada/gerada para comparação

```


## 📦 Funcionalidades da Classe `lista`


Atributos da Classe

- `max_size`: Define o número máximo de elementos permitidos na lista.
- `size`: Quantidade atual de elementos inseridos na lista.
- `elements`: Lista interna que armazena os objetos adicionados, iniciada com valores `None`.


Métodos da Classe

- `__init__(max_size: int)`: Construtor da classe. Inicializa os atributos `max_size`, `size` e preenche `elements` com `None`.
- `is_full()`: Retorna `True` se a lista estiver cheia (ou seja, quando `size == max_size`); caso contrário, retorna `False`.
- `add(obj)`: Insere um novo objeto `obj` na próxima posição disponível da lista, incrementando `size`.


## 📦 Funcionalidades da Classe `Registry`

Atributos da Classe

- `field`:  Campo do nó que foi alterado (`LEFT`, `RIGHT` ou `PARENT`), do tipo `FieldEnum`..
- `new_value`: Novo valor atribuído ao campo.
- `version`: Versão da árvore em que a modificação foi realizada. 




## 📦 Funcionalidades da Classe `Node`

Atributos da classe

- `value`: Valor armazenado no nó (por exemplo, um número inteiro).
- `left`: Ponteiro para o nó filho à esquerda.
- `right`: Ponteiro para o nó filho à direita.
- `parent`: Ponteiro para o nó pai.
- `return_pointers`: Lista de nós que apontam para este nó (instância de `Lista`).
- `modifications`: Lista que armazena modificações (instância de `Lista`) com versões diferentes — usada para a persistência parcial.


Métodos da classe

- `__init__(self, value, p=10)`: Construtor da classe. Inicializa o valor do nó, os ponteiros e as listas `return_pointers` e `modifications`.
- `__repr__(self)`: Retorna uma representação legível do nó, útil para debug (`Node(valor)`).



## 📦 Funcionalidades da Classe `Node`

Atributos da classe

- `roots`: Dicionário que mapeia versões para raízes da árvore. Exemplo: `roots[0]` é a versão inicial.
- `current_version`: Última versão criada da árvore.
- `size`: Contador de nós existentes na estrutura.


Métodos da classe

- `__init__()`: Inicializa a árvore com a versão 0 e raiz nula.
- `insert(value)`: Insere um valor na árvore e cria uma nova versão.
- `remove(value)`: Remove um valor da árvore e gera uma nova versão.
- `search(value, version)`: Busca um valor específico em uma versão da árvore.
- `print_tree()`: Retorna a representação da árvore na versão atual.
- `print_version(version)`: Retorna a representação da árvore na versão especificada.
- `print_tree_in_order(version)`: Imprime os valores da árvore em ordem crescente (in-order traversal).
- `successor(value, version)`: Retorna o sucessor do valor na versão especificada da árvore.


---

Métodos auxiliares


- `_insert_rec(node, value, parent, version)`: Função recursiva para inserir um valor respeitando a lógica da BST.
- `_remove_rec(node, value, version)`: Função recursiva para remover um nó.
- `minimum(node, version)`: Retorna o menor valor (mais à esquerda) da subárvore a partir de um nó.
- `_search_rec(node, value, version)`: Busca recursiva por um valor.
- `get_field(node, field, version)`: Recupera o valor de um campo (ex: `left`, `right`, `parent`) em uma versão específica, considerando a lista de modificações.
- `set_field(node, field, new_value, version)`: Define um novo valor para um campo do nó, criando uma modificação ou copiando o nó, se necessário.
- `copy_node(node, version)`: Copia um nó e atualiza os ponteiros e os pais mantendo a integridade da árvore.
- `_repr_aux(node, level, version)`: Representação textual da árvore (versão usada internamente).
- `_print_in_order(node, version, level)`: Impressão dos nós em ordem crescente.
- `_ceil(node, value, version)`: Encontra o menor valor maior ou igual ao valor dado (caso não exista o valor exato).
- `_find_ancestor_successor(node, value, version)`: Busca o menor ancestral que seja sucessor do nó atual.
