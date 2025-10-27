from combination_with_replacement import combination_with_replacement

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


def DFS(root: tree, target: int = None):

    visited = []
    stack = [root]
    stop = False

    while stack and not stop:
        node = stack.pop()
        if node.value == target:
            stop = True
        visited.append(node)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return visited

if __name__ == "__main__":
    height = int(input())
    num = 1
    if height <= 0:
        exit()
    else:
        root = tree(num)
        num += 1
        for i in range(height - 1):
            channel = combination_with_replacement([".left", ".right"], i)
            for j in range(2**i):
                eval("root" + ''.join(list(channel[j])) + ".insert_left(" + str(num) + ")")
                num += 1
                eval("root" + ''.join(list(channel[j])) + ".insert_right(" + str(num) + ")")
                num += 1

    target = int(input())
    visited_nodes = DFS(root, target)
    for node in visited_nodes:
        print(node.value)