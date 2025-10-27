from data_structure import Graph

def graph_search(graph: Graph, start, target):
    stack = [start]
    visited = set()
    stop = False
    channel = []

    while stack and not stop:
        node = stack.pop()
        if node == target:
            stop = True
        visited.add(node)
        for neighbor in graph.get_neighbors(node):
            if neighbor not in visited:
                stack.append(neighbor)
        channel.append(node)

    return channel

if __name__ == "__main__":
    g = Graph()
    edges = [
        (1, 2), (1, 3), (2, 4), (2, 5),
        (3, 5), (3, 6), (5, 7), (5, 8)
    ]
    for u, v in edges:
        g.add_node(u)
        g.add_node(v)
        g.add_edge(u, v)
    result = graph_search(g, 1, 4)
    print(result)