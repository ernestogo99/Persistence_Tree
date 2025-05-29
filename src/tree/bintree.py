from .node import Node

class Tree:
    def __init__(self):
        self.root = None
        self.size = 0


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
        self.size += 1
        return node


    def insert(self, value):
        self.root = self._insert_rec(self.root, value)


    def _transplant(self, u: Node , v: Node):
        u_parent = u.parent

        if u_parent is None:
            self.root = v
        elif u is u_parent.left:
            u_parent.left = v
        else:
            u_parent.right = v
        
        if v:
            v.parent = u.parent


    def _remove_rec(self, node: Node, data):
        if data < node.value:
            self._remove_rec(node.left, data)
        elif data > node.value:
            self._remove_rec(node.right, data)
        else:
            if node.left is None:
                self._transplant(node, node.right)
            elif node.right is None:
                self._transplant(node, node.left)
            else:
                succ = self._sucessor(node)
                self._transplant(succ, succ.right)
                succ.left = node.left
                node.left.parent = succ
                succ.right = node.right
                node.right.parent = succ
                self._transplant(node, succ)
            
            self.size -= 1
            return node
    

    def remove(self, value):
        self._remove_rec(self.root, value)
        

    def _search_rec(self, node: Node, value):
        if node is None or node.value == value:
            return node
        if value < node.value:
            return self._search_rec(node.left, value)
        return self._search_rec(node.right, value)    
    

    def search(self, value):
        return self._search_rec(self.root, value)   
    

    def size(self):
        return self.size
    

    def minimum(self, node: Node):
        while node.left:
            node = node.left
        return node
    

    def maximum(self, node: Node):
        while node.right:
            node = node.right
        return node


    def _sucessor(self, node: Node):
        if node.right:
            return self.minimum(node.right)
        
        y = node.parent

        while (y and node is y.right):
            node = y
            y = node.parent
        
        return y

