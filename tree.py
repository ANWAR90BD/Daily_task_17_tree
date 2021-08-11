
# Implementing a Tree
"""
            5
         /     \
        2       4
       / \       \
      10  7       8
         / \     / \
        9  12   1   6
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_left(self, node):
        self.left = node

    def add_right(self, node):
        self.right = node

def create_tree():
    five = Node(5)
    two = Node(2)
    four = Node(4)
    five.add_left(two)
    five.add_right(four)

    ten = Node(10)
    seven = Node(7)
    two.add_left(ten)
    two.add_right(seven)

    nine = Node(9)
    twelve = Node(12)
    seven.add_left(nine)
    seven.add_right(twelve)

    eight = Node(8)
    four.add_right(eight)

    one = Node(1)
    six = Node(6)
    eight.add_left(one)
    eight.add_right(six)

    return five


def pre_order(node):
    print(node.data, end=' ')
    if node.left:
        pre_order(node.left)
    if node.right:
        pre_order(node.right) 

def post_order(node):
    if node.left:
        post_order(node.left)
    if node.right:
        post_order(node.right)
    print(node.data, end=' ')    

def in_order(node):
    if node.left:
        in_order(node.left)
    print(node.data, end=' ')
    if node.right:
        in_order(node.right)


if __name__ == '__main__':
    tree = create_tree()
    print(tree.data)
    print("Pre_order list")
    pre_order(tree)
    print('\n')
    print("Post_order list")
    post_order(tree)
    print('\n')
    print("In_order list")
    in_order(tree)
    print("\n")