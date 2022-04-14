'''
BFS can be applied to all the problem of graphs if there are not weights available.
Time Complexity of BFS is O(m+n)
'''
# Defines and Creates a Graph
class Graph:
    def __init__(self, num_nodes, edges):
        self.num_nodes = num_nodes
        self.data = [[] for _ in range(len(num_nodes))]
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
def bfs(graph, root):
    queue = []
    discovered = [False] * len(graph.data)
    distance = [None] * len(graph.data)
    parent = [None] * len(graph.data)
    discovered[root] = True
    queue.append(root)
    distance[root] = 0
    idx = 0

    while idx < len(queue):
        #Dequeuing
        current = queue[idx]
        idx += 1

        # check all the edges of current
        for node in graph.data[current]:
            if not discovered[node]:
                # Distance from the Parent Node
                distance[node] = 1 + distance[current]
                # Returns the Parent
                parent[node] = current
                discovered[node] = True
                queue.append(node)

    return queue, distance, parent

if __name__ == "__main__":
    num_nodes = 5
    graph = [(0,1),(0,4),(1,2),(1,3),(1,4),(2,3),(3,4)]
