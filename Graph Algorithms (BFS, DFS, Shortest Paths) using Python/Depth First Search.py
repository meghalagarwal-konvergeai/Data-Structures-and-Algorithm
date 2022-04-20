'''
Time Complexity of DFS is O(m+n)
'''

# Defines and Creates a Graph
class Graph:
    def __init__(self, num_nodes, edges):
        self.num_nodes = num_nodes
        self.data = [[] for _ in range(num_nodes)]
        # Creating Adjusent nodes whichh are linked to them 
        for n1, n2 in edges:
            self.data[n1].append(n2)
            self.data[n2].append(n1)

    def __repr__(self):
        # Printing the Nodes through which other nodes are conneted and the list of nodes which are connected
        return "\n".join(["{}: {}".format(n, neighbors) for n, neighbors in enumerate(self.data)])

    def __str__(self):
        return self.__repr__()

# DFS Algorigm Starts here
def dfs(graph, source):
    visited = [False] * len(graph.data)
    stack = [source]
    result = []
    
    while len(stack) > 0:
        current = stack.pop()
        if not visited[current]:
            result.append(current)
            visited[current] = True
            for v in graph.data[current]:
                stack.append(v)
                
    return result

if __name__ == "__main__":
    num_nodes = 5
    graph = [(0,1),(0,4),(1,2),(1,3),(1,4),(2,3),(3,4)]

    g1 = Graph(num_nodes, graph)
    bf_search = dfs(g1, 0)
    print(g1)
    print(bf_search)