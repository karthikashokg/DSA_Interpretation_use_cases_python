from collections import deque 

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

def level_order_traversal(root_node): 
    # Initialize an empty list to store the nodes in level order
    list_of_nodes = [] 
    # Initialize a queue with the root node for level order traversal
    traversal_queue = deque([root_node]) 
    while len(traversal_queue) > 0:
        # Pop the first node from the queue
        node = traversal_queue.popleft() 
        # Append the data of the node to the list_of_nodes
        list_of_nodes.append(node.data) 
        # If the node has a left child, append it to the queue
        if node.left_child: 
            traversal_queue.append(node.left_child) 
            # If the node has a right child, append it to the queue
            if node.right_child: 
                traversal_queue.append(node.right_child) 
    return list_of_nodes 
    # Time Complexity: O(n) (where n is the number of nodes in the tree)
    # Space Complexity: O(n) (due to the queue and list_of_nodes)

# Perform level order traversal and print each node's data
print(level_order_traversal(n1))

# Visual representation of level order traversal:
# root node -> left child -> right child -> left grandchild
