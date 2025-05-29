from list.lista import Lista

class Node:
    def __init__(self, value, p=10):
        self.value = value
        self.left = None
        self.right = None
        self.parent=None

        self.return_pointers = Lista(p)
        self.modifications = Lista(2*p)

    def __repr__(self):
        return f'Node({self.value})'
