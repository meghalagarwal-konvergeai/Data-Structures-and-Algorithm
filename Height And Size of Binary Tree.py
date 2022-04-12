class Tree_Node:
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

def height_of_tree(node):
    if node is None:
        return 0
    return (1 + max(height_of_tree(node.left), height_of_tree(node.right)))

def size_of_tree(node):
    if node is None:
        return 0
    return (1 + size_of_tree(node.left) + size_of_tree(node.right))

if __name__ == "__main__":
    tree_tuple = ((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8)))
    tree = parse_tuple(tree_tuple)
    ht = height_of_tree(tree)
    s = size_of_tree(tree)

    print("Height Of the Tree:", ht)
    print("Size of the Tree:", s)
