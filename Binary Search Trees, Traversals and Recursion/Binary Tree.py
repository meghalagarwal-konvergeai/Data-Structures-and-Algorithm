'''
Binary Tree:
The left subtree of any node only contains nodes with keys that are lexicographically smaller than the node's key,
and the right subtree of any node only contains nodes with keys that lexicographically larger than the node's key.
A tree that satisfies this property is called a binary search trees,
and it's easy to locate a specific key by traversing a single path down from the root note.
'''
# Defines a Tree
class Tree_Node:
    # Creating a Constructor Function
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# Create a Tree with Recursive Function Technique
def parse_tuple(data):
    # Checks whether the input data is a Tuple and with a length of 3
    if(isinstance(data, tuple) and len(data) == 3):
        node = Tree_Node(data[1])
        node.left = parse_tuple(data[0])
        node.right = parse_tuple(data[2])
    elif(data is None):
        node = None
    else:
        node = Tree_Node(data)
    return node

# Displays the Tree
def display_keys(node, space='\t', level=0):    
    # If the node is empty
    if node is None:
        print(space*level + '∅')
        return   
    
    # If the node is a leaf 
    if node.left is None and node.right is None:
        print(space*level + str(node.key))
        return
    
    # If the node has children
    display_keys(node.right, space, level+1)
    print(space*level + str(node.key))
    display_keys(node.left,space, level+1)   

# Converts the Tree back to tuple with Recursive Function
def back_to_tuple(node):
    if(node is None):
        return None
    if(node.left is None and node.right is None):
        return node.key
    return back_to_tuple(node.left), node.key, back_to_tuple(node.right)

# Program Starts here
if __name__ == "__main__":
    tree_tuple = ((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8)))
    tree = parse_tuple(tree_tuple)
    tu = back_to_tuple(tree)
    
    print(tree.key)
    print(tu)