from tree.bintree import Tree

def main():
    tree = Tree()

    print("Versão 0 (inicial):")
    tree.print_tree()
 

    tree.insert(10)
    print("\nVersão 1 (inserido 10):")
    tree.print_tree()

    tree.insert(5)
    print("\nVersão 2 (inserido 5):")
    tree.print_tree()

    tree.insert(15)
    print("\nVersão 3 (inserido 15):")
    tree.print_tree()

    print("\nVersão 1 novamente (deveria mostrar apenas 10):")
    tree.print_version(1)

    print("\nVersão 2 novamente (deveria mostrar 10 com filho esquerdo 5):")
    tree.print_version(2)

    print("\nBuscando 5 na versão 1 (deve ser None):", tree.search(5, 1))
    print("\nBuscando 15 na versão 1 (deve ser None):", tree.search(15, 1))
    print("Buscando 5 na versão 2 (deve ser 5):", tree.search(5, 2))
    print("Buscando 15 na versão 2 (deve ser None):", tree.search(15, 2))
    print("Buscando 15 na versão 3 (deve ser 15):", tree.search(15, 3))
    tree.print_tree_in_order(3)


if __name__ == "__main__":
    main()
