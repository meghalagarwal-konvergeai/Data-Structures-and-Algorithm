class Tree_Node:
    # Creating a Constructor Function
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def parse_tuple(data):
    if(isinstance(data, tuple) and len(data) == 3):
        node = Tree_Node(data[1])
        node.left = parse_tuple(data[0])
        node.right = parse_tuple(data[2])
    elif(data is None):
        node = None
    else:
        node = Tree_Node(data)
    return node

def in_order_traversal(node):
    if(node is None):
        return []
    return (in_order_traversal(node.left)+[node.key]+in_order_traversal(node.right))

if __name__ == "__main__":
    tree_tuple = ((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8)))
    tree = parse_tuple(tree_tuple)
    tr = in_order_traversal(tree)

    print(tr)