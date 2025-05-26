from .node import Node

class Tree:
    def __init__(self):
        self.root = None

    def __repr__(self):
        return self._repr_aux(self.root, 0)

    def _repr_aux(self, node: Node, level):
        if node is None:
            return ""
        spaces = " " * (level * 4)
        result = f"{spaces}{node.value}\n"
        result += self._repr_aux(node.left, level + 1)
        result += self._repr_aux(node.right, level + 1)
        return result

    def _print_in_order(self, node: Node):
        if node:
            self._print_in_order(node.left)
            print(f'Value: {node.value} ')
            self._print_in_order(node.right)
            
    def print_tree(self):
        self._print_in_order(self.root)

    def _insert_rec(self, node: Node, data,parent=None):
        if node is None:
            new_node=Node(data)
            new_node.parent=parent
            return new_node
        if data < node.value:
            node.left = self._insert_rec(node.left, data,node)
        elif data > node.value:
            node.right = self._insert_rec(node.right, data,node)
        return node

    def insert(self, value):
        self.root = self._insert_rec(self.root, value)

    def _search_rec(self, node: Node, value):
        if node is None or node.value == value:
            return node
        if value < node.value:
            return self._search_rec(node.left, value)
        return self._search_rec(node.right, value)    
    
    def search(self, value):
        return self._search_rec(self.root, value)   
    
    def _size(self, node: Node):
        if node is None:
            return 0
        return 1 + self._size(node.left) + self._size(node.right)
    
    def size(self):
        return self._size(self.root)
    


