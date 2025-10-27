class tree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert_left(self, value):
        if self.left is None:
            self.left = tree(value)
        else:
            new_tree = tree(value)
            new_tree.left = self.left
            self.left = new_tree

    def insert_right(self, value):
        if self.right is None:
            self.right = tree(value)
        else:
            new_tree = tree(value)
            new_tree.right = self.right
            self.right = new_tree

class graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, value):
        if value not in self.nodes:
            self.nodes[value] = []

    def add_edge(self, from_node, to_node):
        if from_node in self.nodes and to_node in self.nodes:
            self.nodes[from_node].append(to_node)
            self.nodes[to_node].append(from_node)
