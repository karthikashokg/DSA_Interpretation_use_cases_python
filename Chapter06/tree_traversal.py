# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 20:07:16 2024

@author: AH25483
"""

class Node: 
    def __init__(self, data): 
        # Initialize the node with data and set left and right children to None
        self.data = data 
        self.right_child = None 
        self.left_child = None 
        # Time Complexity: O(1)
        # Space Complexity: O(1)

# Create nodes with data
n1 = Node("root node")  
n2 = Node("left child node") 
n3 = Node("right child node") 
n4 = Node("left grandchild node") 

# Link nodes to form the tree structure
n1.left_child = n2 
n1.right_child = n3 
n2.left_child = n4 

# Visual representation of the tree:
#         root node
#        /         \
# left child   right child
#     /
# left grandchild

# Traverse the tree starting from the root node and print each node's data
current = n1 
while current: 
    print(current.data) 
    current = current.left_child 
    # Time Complexity: O(h) (where h is the height of the tree)
    # Space Complexity: O(1)

print("\n")

# Define inorder traversal function
def inorder(root_node): 
    current = root_node 
    if current is None: 
        return 
    inorder(current.left_child) 
    print(current.data) 
    inorder(current.right_child) 
    # Time Complexity: O(n) (where n is the number of nodes in the tree)
    # Space Complexity: O(h) (due to the recursion stack, where h is the height of the tree)

# Define preorder traversal function
def preorder(root_node): 
    current = root_node 
    if current is None: 
        return 
    print(current.data) 
    preorder(current.left_child) 
    preorder(current.right_child) 
    # Time Complexity: O(n) (where n is the number of nodes in the tree)
    # Space Complexity: O(h) (due to the recursion stack, where h is the height of the tree)

# Define postorder traversal function
def postorder(root_node): 
    current = root_node 
    if current is None: 
        return 
    postorder(current.left_child) 
    postorder(current.right_child) 
    print(current.data)
    # Time Complexity: O(n) (where n is the number of nodes in the tree)
    # Space Complexity: O(h) (due to the recursion stack, where h is the height of the tree)

# Perform inorder traversal and print each node's data
inorder(n1)
print("\n")

# Perform preorder traversal and print each node's data
preorder(n1)
print("\n")

# Perform postorder traversal and print each node's data
postorder(n1)
