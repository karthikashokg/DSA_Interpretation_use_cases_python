# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 20:02:47 2024

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

class Tree:
    def __init__(self):
        # Initialize the tree with root_node as None
        self.root_node = None
        # Time Complexity: O(1)
        # Space Complexity: O(1)

    def insert(self, data):
        # Create a new node with the given data
        node = Node(data)
        # Time Complexity: O(1)
        # Space Complexity: O(1)
        if self.root_node is None:
            # If the tree is empty, set the new node as the root node
            self.root_node = node
            return self.root_node
            # Time Complexity: O(1)
            # Space Complexity: O(1)
        else:
            # Traverse the tree to find the correct position for the new node
            current = self.root_node
            parent = None
            while True:
                parent = current
                if node.data < parent.data:
                    # Move to the left child if the new node's data is less than the current node's data
                    current = current.left_child
                    if current is None:
                        # If the left child is None, insert the new node here
                        parent.left_child = node
                        return self.root_node
                        # Time Complexity: O(h)
                        # Space Complexity: O(1)
                else:
                    # Move to the right child if the new node's data is greater than or equal to the current node's data
                    current = current.right_child
                    if current is None:
                        # If the right child is None, insert the new node here
                        parent.right_child = node
                        return self.root_node
                        # Time Complexity: O(h)
                        # Space Complexity: O(1)

    def inorder(self, root_node): 
        # Perform an inorder traversal of the tree and print each node's data
        current = root_node 
        if current is None: 
            return 
        self.inorder(current.left_child) 
        print(current.data) 
        self.inorder(current.right_child)
        # Time Complexity: O(n)
        # Space Complexity: O(h)
        
                    
    def get_node_with_parent(self, data): 
        # Find a node with the given data and return it along with its parent
        parent = None 
        current = self.root_node 
        if current is None: 
            return (parent, None) 
        while True: 
            if current.data == data: 
                return (parent, current) 
            elif current.data > data: 
                parent = current 
                current = current.left_child 
            else: 
                parent = current 
                current = current.right_child 
        return (parent, current) 
        # Time Complexity: O(h)
        # Space Complexity: O(1)
   

    def remove(self, data):  
        # Remove a node with the given data from the tree
        parent, node = self.get_node_with_parent(data)  
 
        if parent is None and node is None:  
            return False  
 
        # Get children count  
        children_count = 0  
 
        if node.left_child and node.right_child:  
            children_count = 2  
        elif (node.left_child is None) and (node.right_child is None):  
            children_count = 0  
        else:  
            children_count = 1  
        
        if children_count == 0:  
            # If the node has no children, simply remove it
            if parent:  
                if parent.right_child is node:  
                    parent.right_child = None  
                else:  
                    parent.left_child = None  
            else:  
                self.root_node = None 
        elif children_count == 1:  
            # If the node has one child, replace it with its child
            next_node = None  
            if node.left_child:  
                next_node = node.left_child  
            else:  
                next_node = node.right_child  
 
            if parent:  
                if parent.left_child is node:  
                    parent.left_child = next_node  
                else:  
                    parent.right_child = next_node  
            else:  
                self.root_node = next_node  
        else:  
            # If the node has two children, find its in-order successor and replace it with that value
            parent_of_leftmost_node = node  
            leftmost_node = node.right_child  
            while leftmost_node.left_child:  
                parent_of_leftmost_node = leftmost_node  
                leftmost_node = leftmost_node.left_child  
            node.data = leftmost_node.data       
    
            if parent_of_leftmost_node.left_child == leftmost_node:  
                parent_of_leftmost_node.left_child = leftmost_node.right_child  
            else:  
                parent_of_leftmost_node.right_child = leftmost_node.right_child             
        # Time Complexity: O(h)
        # Space Complexity: O(1)
            
    
    def search(self, data):
        # Search for a node with the given data in the tree
        current = self.root_node
        while True:
            if current is None:
                print("Item not found")
                return None
            elif current.data == data:
                print("Item found", data)
                return data
            elif current.data > data:
                current = current.left_child
            else:
                current = current.right_child
        # Time Complexity: O(h)
        # Space Complexity: O(1)

                
    def find_min(self):  
        # Find the minimum value in the tree by traversing to the leftmost leaf
        current = self.root_node  
        while current.left_child:  
            current = current.left_child  
        return current.data          
        # Time Complexity: O(h)
        # Space Complexity: O(1)
    
    
    def find_max(self):  
        # Find the maximum value in the tree by traversing to the rightmost leaf
        current = self.root_node  
        while current.right_child:  
            current = current.right_child  
        return current.data  
        # Time Complexity: O(h)
        # Space Complexity: O(1)
      
      
# Create a new binary search tree      
tree = Tree()
# Insert nodes into the tree      
r = tree.insert(5)
# Visual representation after inserting 5 (root)
print("Tree after inserting 5:")
print("    5")
print()

r = tree.insert(2)
# Visual representation after inserting 2 (left child of 5)
print("Tree after inserting 2:")
print("    5")
print("   /")
print("  2")
print()

r = tree.insert(7)
# Visual representation after inserting 7 (right child of 5)
print("Tree after inserting 7:")
print("    5")
print("   / \\")
print("  2   7")
print()

r = tree.insert(9)
# Visual representation after inserting 9 (right child of 7)
print("Tree after inserting 9:")
print("    5")
print("   / \\")
print("  2   7")
print("       \\")
print("        9")
print()

r = tree.insert(1)
# Visual representation after inserting 1 (left child of 2)
print("Tree after inserting 1:")
print("    5")
print("   / \\")
print("  2   7")
print(" /     \\")
print("1       9")
print()

# Perform an inorder traversal of the tree and print each element      
tree.inorder(r)

# Search for a specific value in the tree      
tree.search(9)      

# Remove a specific value from the tree      
tree.remove(9)  

# Visual representation after removing 9 (right child of 7)
print("Tree after removing 9:")
print("    5")
print("   / \\")
print("  2   7")
print(" /")
print("1")
print()

# Search for a specific value in the tree after removal      
tree.search(9)

# Create a new binary search tree      
tree = Tree()
tree.insert(5)
tree.insert(2)
tree.insert(7)
tree.insert(9)
tree.insert(1)

# Find and print the minimum value in the tree      
print(tree.find_min()) 

# Find and print the maximum value in the tree      
print(tree.find_max()) 
