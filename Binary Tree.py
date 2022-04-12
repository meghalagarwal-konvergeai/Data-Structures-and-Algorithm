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

def back_to_tuple(node):
    if(node is None):
        return None
    if(node.left is None and node.right is None):
        return node.key
    return back_to_tuple(node.left), node.key, back_to_tuple(node.right)

if __name__ == "__main__":
    tree_tuple = ((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8)))
    tree = parse_tuple(tree_tuple)
    tu = back_to_tuple(tree)
    
    print(tree.key)
    print(tu)