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
    print("Buscando 5 na versão 2 (deve ser 5):", tree.search(5, 2))
    print("Buscando 15 na versão 3 (deve ser 15):", tree.search(15, 3))

    tree.remove(5)  

    print("\nVersão 4 (remoção do 5):")
    tree.print_tree()

    print("\nVerificando se o 5 foi removido na versão 4 (espera None):", tree.search(5, 4))
    print("Verificando 10 na versão 4 (espera 10):", tree.search(10, 4))
    print("Verificando 15 na versão 4 (espera 15):", tree.search(15, 4))

    print("\nVersão 3 permanece intacta (espera 10 com 5 e 15):")
    tree.print_version(3)


if __name__ == "__main__":
    main()
