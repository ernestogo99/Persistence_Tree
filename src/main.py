from tree.bintree import Tree
from sys import argv

input_file = argv[1]

class IOHandler:
    def __init__(self, input_file: str):
        self.input_file = input_file
        self.output_file = 'out.txt'
        self.tree = Tree()
    

    def proccess(self):
        out_text = []
        with open(self.input_file, 'r') as f:
            for line in f.readlines():
                out_line = self.read_line(line)
                if out_line is not None:
                    out_text.extend(out_line)
        print(out_text)
        with open(self.output_file, 'w') as f:
            for line in out_text:
                f.writelines(line)


    def read_line(self, line):
        if line[-1] != '\n':
            line += '\n'
        
        line_content = line.split(' ')
        operation = line_content[0]

        if operation == 'INC':
            value = int(line_content[1])
            self.tree.insert(value)
        elif operation == 'REM':
            value = int(line_content[1])
            self.tree.remove(value)
        elif operation == 'SUC':
            value = int(line_content[1])
            version = int(line_content[2]) if len(line_content) == 3 else None
            succ = self.tree.successor(value, version=version)
            return [line, str(succ)+'\n']
        elif operation == 'IMP':
            version = int(line_content[1]) if len(line_content) == 2 else None
            if version is None:
                return [line ,self.tree.print_tree()+'\n']
            return [line, self.tree.print_version(version=version)+'\n']


def main():
    handler = IOHandler(input_file)
    handler.proccess()

# O arquivo in.txt segue as mesmas operações daqui:
"""
    tree = Tree()

    print("Versão 0 (inicial):")
    print(tree.print_tree())

    tree.insert(10)
    print("\nVersão 1 (inserido 10):")
    print(tree.print_tree())

    tree.insert(5)
    print("\nVersão 2 (inserido 5):")
    print(tree.print_tree())

    tree.insert(15)
    print("\nVersão 3 (inserido 15):")
    print(tree.print_tree())

    tree.insert(13)
    print("\nVersão 4 (inserido 13):")
    tree.print_tree()

    print(tree.successor(10))
    print(tree.successor(10, 3))

    print("\nVersão 1 novamente (deveria mostrar apenas 10):")
    tree.print_version(1)

    print("\nVersão 2 novamente (deveria mostrar 10 com filho esquerdo 5):")
    tree.print_version(2)

    print("\nBuscando 5 na versão 1 (deve ser None):", tree.search(5, 1))
    print("Buscando 5 na versão 2 (deve ser 5):", tree.search(5, 2))
    print("Buscando 15 na versão 3 (deve ser 15):", tree.search(15, 3))

    tree.remove(5)  

    print("\nVersão 5 (remoção do 5):")
    tree.print_tree()

    print("\nVerificando se o 5 foi removido na versão 5 (espera None):", tree.search(5, 5))
    print("Verificando 10 na versão 5 (espera 10):", tree.search(10, 5))
    print("Verificando 15 na versão 5 (espera 15):", tree.search(15, 5))

    print("\nVersão 3 permanece intacta (espera 10 com 5 e 15):")
    tree.print_version(3)
"""


if __name__ == "__main__":
    main()
