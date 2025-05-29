class Lista:
    def __init__(self, max_size: int):
        self.max_size = max_size
        self.size = 0
        self.elements = [None for _ in range(max_size)]


    def is_full(self):
        return True if self.size == self.max_size else False
    

    def add(self, obj):
        self.elements[self.size] = obj
        self.size += 1

