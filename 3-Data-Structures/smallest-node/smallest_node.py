
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"{self.value}Left: ( {self.left}) {self.value} Right:({self.right})"


class BinaryTree:
    def __init__(self):
        self.root = None

    def __repr__(self):
        return f"The root is {self.root}"

    def insert(self, new_node):
        if self.root is None:
            self.root = new_node
        else:
            self.insert_node(self.root, new_node)

    def insert_node(self, current_node, new_node):
        if new_node.value <= current_node.value:
            if current_node.left:
                self.insert_node(current_node.left, new_node)
            else:
                current_node.left = new_node
        elif new_node.value > current_node.value:
            if current_node.right:
                self.insert_node(current_node.right, new_node)
            else:
                current_node.right = new_node

    # find_smallest goes here
    
# Instantiate the BinaryTree and call setUp() to set up the tree


# Call find_smallest_node() method to find the smallest node


























#    def print_node(self, node):
#         if node is not None:
#             self.print_node(node.left)
#             print(node.value)
#             self.print_node(node.right)

    # def find_smallest_node(self):
    #     current = self.root
    #     if current is None:
    #         return None
    #     while current.left:
    #         current = current.left
    #     return current.value
    
    # def print_tree(self):
    #     self.print_node(self.root)
