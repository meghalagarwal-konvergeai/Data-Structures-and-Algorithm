'''
BFS can be applied to all the problem of graphs if there are not weights available.
Time Complexity of BFS is O(m+n)
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

# BFS Algorithm Starts Here
def bfs(graph, source):
    visited = [False] * len(graph.data)
    queue = []
    
    visited[source] = True    
    queue.append(source)
    i = 0
    
    while i < len(queue):
        for v in graph.data[queue[i]]:
            if not visited[v]:
                visited[v] = True
                queue.append(v)
        i += 1
        
    return queue

if __name__ == "__main__":
    num_nodes = 5
    graph = [(0,1),(0,4),(1,2),(1,3),(1,4),(2,3),(3,4)]

    g1 = Graph(num_nodes, graph)
    bf_search = bfs(g1, 3)
    print(g1)
    print(bf_search)