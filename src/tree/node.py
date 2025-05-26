class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent=None

    def __repr__(self):
        return f'Node({self.value})'
