class Graph:
    def __init__(self, num_nodes, edges):
        self.num_nodes = num_nodes
        self.data = [[] for _ in range(len(num_nodes))]
        for n1, n2 in edges:
            self.data[n1].append(n2)
            self.data[n2].append(n1)

    def __repr__(self):
        return "\n".join(["{}: {}".format(n, neighbors) for n, neighbors in enumerate(self.data)])

    def __str__(self):
        return self.__repr__()

def dfs(graph, root):
    stack = []
    discovered = [False * len(graph.data)]
    result = []

    stack.appen(root)

    while len(stack) > 0:
        current = stack.pop()
        if not discovered[current]:
            discovered[current] = True
            result.append(current)
            for node in graph.data[current]:
                if not discovered[node]:
                    stack.append(node)
    
    return result

if __name__ == "__main__":
    num_nodes = 5
    graph = [(0,1),(0,4),(1,2),(1,3),(1,4),(2,3),(3,4)]