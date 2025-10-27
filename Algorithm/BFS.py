from collections import deque
from data_structure import Tree
from combination_with_replacement import combination_with_replacement


def BFS(root: Tree, target=None):

    visited = []
    deq = deque()
    deq.append(root)
    stop = False

    while deq and not stop:
        node = deq.popleft()
        if node.value == target:
            stop = True
        if node.left:
            deq.append(node.left)
        if node.right:
            deq.append(node.right)
        visited.append(node)

    return visited

if __name__ == "__main__":
    height = int(input())
    num = 1

    if height <= 0:
        exit()
    else:
        root = Tree(num)
        num += 1
        for i in range(height - 1):
            channel = combination_with_replacement([".left", ".right"], i)
            for j in range(2**i):
                eval("root" + ''.join(list(channel[j])) + ".insert_left(" + str(num) + ")")
                num += 1
                eval("root" + ''.join(list(channel[j])) + ".insert_right(" + str(num) + ")")
                num += 1

    target = int(input())
    visited_nodes = BFS(root, target)
    for node in visited_nodes:
        print(node.value)