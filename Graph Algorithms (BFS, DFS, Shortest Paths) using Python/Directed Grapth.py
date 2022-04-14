
class Graph:
    def __init__(self, num_nodes, edges, directed=False, weighted=False):
        self.num_nodes = num_nodes
        self.directed = directed
        self.weighted = weighted
        self.data = [[] for _ in range(num_nodes)]
        self.weight = [[] for _ in range(num_nodes)]
        for edge in edges:
            if self.weighted:
                node1, node2, weight = edge
                self.data[node1].append(node2)
                self.weight[node1].append(weight)
                if not directed:
                    self.data[node2].append(node1)
                    self.weight[node2].append(weight)
            else:
                node1, node2 = edge
                self.data[node1].append(node2)
                if not directed:
                    self.data[node2].append(node1)
    
    def __repr__(self):
        result = ""
        if self.weighted:
            for i, (nodes, weights) in enumerate(zip(self.data, self.weighted)):
                result += "{}: {}\n".format(i, list(zip(nodes, weights)))
        else:
            for i, nodes in enumerate(self.data):
                result += "{}: {}\n".format(i, nodes)
        
        return result

if __name__ == "__main__":
    num_nodes1 = 5
    edges1 = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0), (1, 4), (1, 3)]    

    num_nodes3 = 9
    edges3 = [(0, 1), (0, 3), (1, 2), (2, 3), (4, 5), (4, 6), (5, 6), (7, 8)]    

    num_nodes5 = 9
    edges5 = [(0, 1, 3), (0, 3, 2), (0, 8, 4), (1, 7, 4), (2, 7, 2), (2, 3, 6), 
            (2, 5, 1), (3, 4, 1), (4, 8, 8), (5, 6, 8)]

    num_nodes6 = 5
    edges6 = [(0, 1), (1, 2), (2, 3), (2, 4), (4, 2), (3, 0)]  

    num_nodes7 = 6
    edges7 = [(0, 1, 4), (0, 2, 2), (1, 2, 5), (1, 3, 10), (2, 4, 3), (4, 3, 4), (3, 5, 11)]

    grh = [(num_nodes1, edges1, False),(num_nodes3, edges3, False),(num_nodes5, edges5, False),(num_nodes6, edges6, True),(num_nodes7, edges7, False)]

    for att in grh:
        gr = Graph(att[0],att[1],att[2])
        print(gr)