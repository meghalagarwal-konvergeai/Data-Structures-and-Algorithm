class BSTNode():
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

def insert(node, key, value):
    if node is None:
        node = BSTNode(key, value)
    elif(key < node.key):
        node.left = insert(node.left, key, value)
        node.left.parent = node
    elif(key > node.key):
        node.right = insert(node.right, key, value)
        node.right.parent = node
    return node

def find(node, key):
    if node is None:
        return None
    if(key == node.key):
        return node
    if(key < node.key):
        return find(node.left, key)
    if(key > node.key):
        return find(node.right, key)

def update(node, key, value):
    target = find(node, key)
    if target is not None:
        target.value = value
    else:
        print("Node Does not Exists")

def list_all(node):
    if node is None:
        return []
    return list_all(node.left) + [(node.key, node.value)] + list_all(node.right)

def is_balanced(node):
    if node is None:
        return True, 0

    balanced_l, height_l = is_balanced(node.left)
    balanced_r, height_r = is_balanced(node.right)
    balanced = (balanced_l and balanced_r and abs(height_l-height_r) <= 1)
    height = 1 + max(height_l, height_r)

    return balanced, height

'''
The below function is to make a Balanced tree based on Binary Search Algorithm but it waork with the Sorted Array/list
'''
def make_balanced_bst(data, low = 0, high = None, parent = None):
    if high is None:
        high = len(data)-1
    if(low > high):
        return None
    
    mid = (low+high)//2
    key, value = data[mid]

    root = BSTNode(key, value)
    root.parent = parent
    root.left = make_balanced_bst(data, low, mid-1, root)
    root.right = make_balanced_bst(data, mid+1, high, root)

    return root

'''
To Balanace an Un-balanced tree using Binary Search Tree
'''
def balanced_tree(node):
    return make_balanced_bst(list_all(node))

if __name__ == "__main__":
    tree = insert(None, "Jadhesh", "Jadhesh")
    list = [(tree, "Biraj", "Biraj"),(tree, "Sonaksh", "Sonaksh"),(tree, "Aakash", "Aakash"),(tree, "Hemanth", "Hemanth"),(tree, "Siddhant", "Siddhant"),(tree, "Vishal", "Vishal")]

    for tup in list:
        insert(tup[0], tup[1], tup[2])

    finding_node = find(tree, "Hemanth")
    print(finding_node.key, finding_node.value)