from .node import Node
from .registry import Registry
from .fields import FieldEnum

class Tree:
    def __init__(self):
        self.roots = {}  
        self.current_version = 0
        self.size = 0
        self.roots[0] = None 

    def __repr__(self):
        return self._repr_aux(self.roots[self.current_version], 0, self.current_version)

    def _repr_aux(self, node: Node, level, version):
        if node is None:
            return ""
        spaces = " " * (level * 4)
        result = f"{spaces}{node.value}\n"
        result += self._repr_aux(self.get_field(node, FieldEnum.LEFT, version), level + 1, version)
        result += self._repr_aux(self.get_field(node, FieldEnum.RIGHT, version), level + 1, version)
        return result

    def _print_in_order(self, node: Node, version: int, level: int):
        if node:
            self._print_in_order(self.get_field(node, FieldEnum.LEFT, version), version, level + 1)
            print(f'Value: {node.value} level: {level}')  
            self._print_in_order(self.get_field(node, FieldEnum.RIGHT, version), version, level + 1)

    def print_tree_in_order(self, version: int):
        root = self.roots.get(version)
        if root is None:
            print(f"(versão {version} vazia)")
            return
        self._print_in_order(root, version, 0)

    def get_field(self, node: Node, field: FieldEnum, version):
        for i in range(node.modifications.size - 1, -1, -1):
            mod = node.modifications.elements[i]
            if mod and mod.field == field and mod.version <= version:
                return mod.new_value
        return getattr(node, field.value)

    def set_field(self, node: Node, field: FieldEnum, new_value, version):
        if not node.modifications.is_full():
            reg = Registry(field, new_value, version)
            node.modifications.add(reg)
            return node
        else:
            copied = self.copy_node(node, version)
            setattr(copied, field.value, new_value)
            return copied

    def copy_node(self, node: Node, version):
        copied = Node(node.value)

        copied.left = self.get_field(node, FieldEnum.LEFT, version)
        copied.right = self.get_field(node, FieldEnum.RIGHT, version)
        copied.parent = self.get_field(node, FieldEnum.PARENT, version)

        if copied.left:
            copied.left.return_pointers.add(copied)
        if copied.right:
            copied.right.return_pointers.add(copied)

        for i in range(node.return_pointers.size):
            parent = node.return_pointers.elements[i]
            if parent:
                if self.get_field(parent, FieldEnum.LEFT, version) == node:
                    updated_parent = self.set_field(parent, FieldEnum.LEFT, copied, version)
                    copied.parent = updated_parent
                    copied.return_pointers.add(updated_parent)
                elif self.get_field(parent, FieldEnum.RIGHT, version) == node:
                    updated_parent = self.set_field(parent, FieldEnum.RIGHT, copied, version)
                    copied.parent = updated_parent
                    copied.return_pointers.add(updated_parent)

        return copied

    def insert(self, value):
        new_version = self.current_version + 1
        old_root = self.roots[self.current_version]
        if old_root is None:
            new_root = Node(value)
        else:
            new_root = self._insert_rec(old_root, value, None, new_version)
        self.roots[new_version] = new_root
        self.current_version = new_version

    def _insert_rec(self, node: Node, value, parent, version):
        if node is None:
            new_node = Node(value)
            new_node.parent = parent
            if parent:
                new_node.return_pointers.add(parent)
            self.size += 1
            return new_node

        if value < node.value:
            left = self.get_field(node, FieldEnum.LEFT, version)
            new_left = self._insert_rec(left, value, node, version)
            updated_node = self.set_field(node, FieldEnum.LEFT, new_left, version)
            new_left.return_pointers.add(updated_node)
            return updated_node

        elif value > node.value:
            right = self.get_field(node, FieldEnum.RIGHT, version)
            new_right = self._insert_rec(right, value, node, version)
            updated_node = self.set_field(node, FieldEnum.RIGHT, new_right, version)
            new_right.return_pointers.add(updated_node)
            return updated_node

        return node

    def remove(self, value):
        new_version = self.current_version + 1
        old_root = self.roots[self.current_version]
        new_root = self._remove_rec(old_root, value, new_version)
        self.roots[new_version] = new_root
        self.current_version = new_version

    def _remove_rec(self, node: Node, value, version):
        if node is None:
            return None

        if value < node.value:
            left = self.get_field(node, FieldEnum.LEFT, version)
            new_left = self._remove_rec(left, value, version)
            return self.set_field(node, FieldEnum.LEFT, new_left, version)

        elif value > node.value:
            right = self.get_field(node, FieldEnum.RIGHT, version)
            new_right = self._remove_rec(right, value, version)
            return self.set_field(node, FieldEnum.RIGHT, new_right, version)

        else:
            left = self.get_field(node, FieldEnum.LEFT, version)
            right = self.get_field(node, FieldEnum.RIGHT, version)

            if left is None:
                return right
            elif right is None:
                return left

            successor = self.minimum(right, version)
            successor_copied = self.copy_node(successor, version)

            successor_right = self._remove_rec(right, successor.value, version)
            successor_copied = self.set_field(successor_copied, FieldEnum.RIGHT, successor_right, version)

            successor_copied = self.set_field(successor_copied, FieldEnum.LEFT, left, version)

            return successor_copied

    def minimum(self, node: Node, version):
        current = node
        while current:
            left = self.get_field(current, FieldEnum.LEFT, version)
            if left is None:
                break
            current = left
        return current

    def search(self, value, version):
        return self._search_rec(self.roots[version], value, version)

    def _search_rec(self, node: Node, value, version):
        if node is None or node.value == value:
            return node

        if value < node.value:
            return self._search_rec(self.get_field(node, FieldEnum.LEFT, version), value, version)
        else:
            return self._search_rec(self.get_field(node, FieldEnum.RIGHT, version), value, version)

    def print_version(self, version):
        print(self._repr_aux(self.roots[version], 0, version))

    def print_tree(self):
        self.print_version(self.current_version)
