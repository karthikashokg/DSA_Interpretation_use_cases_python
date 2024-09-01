
class Node:  
    def __init__(self, data=None):  
        self.data = data  # Initialize the node with data
        self.next = None  # Initialize the next pointer to None
       
class stack:  
    def __init__(self):  
        self.top = None  # Initialize the top pointer to None
        self.size = 0  # Initialize the size of the stack to 0
        
    def push(self, data):  
        # Create a new node 
        node = Node(data)  
        if self.top:  # If the stack is not empty
            node.next = self.top  # Point the new node's next to the current top
            self.top = node  # Update the top to the new node                  
        else:  
            self.top = node  # If the stack is empty, set the new node as the top
        self.size += 1  # Increment the size of the stack
            
    def pop(self):  
        if self.top:  # If the stack is not empty
            data = self.top.data  # Get the data from the top node
            self.size -= 1  # Decrement the size of the stack
            if self.top.next:  # Check if there is more than one node
                self.top = self.top.next  # Update the top to the next node
            else:  
                self.top = None  # If there is only one node, set top to None
            return data  # Return the data from the popped node
        else:  
            print("Stack is empty")  # Print a message if the stack is empty
        
    def peek(self):  
        if self.top:  # If the stack is not empty
            return self.top.data  # Return the data from the top node
        else:  
            print("Stack is empty")  # Print a message if the stack is empty
        
# Create an instance of stack
words = stack()

# Push elements onto the stack
words.push('4')
words.push('5')
words.push('6')
words.push('7')

# Print the stack elements
current = words.top
while current:
    print(current.data)  # Print the data of each node
    current = current.next  # Move to the next node

# Pop an element from the stack
words.pop()

# Print the stack elements again
current = words.top
while current:
    print(current.data)  # Print the data of each node
    current = current.next  # Move to the next node

# Peek at the top element of the stack
words.peek()

##############

# ### Time and Space Complexities

# - **`push` function:**
#   - **Time Complexity:** O(1) for adding a new node to the top of the stack.
#   - **Space Complexity:** O(1) for the additional node added to the stack.

# - **`pop` function:**
#   - **Time Complexity:** O(1) for removing the top node from the stack.
#   - **Space Complexity:** O(1) for the node removed from the stack.

# - **`peek` function:**
#   - **Time Complexity:** O(1) for accessing the top node's data.
#   - **Space Complexity:** O(1) as it does not modify the stack.

# ### Visual Representation

# Here's a visual representation of how the stack works:

# 1. **Initial State:**
#    ```
#    Stack: []
#    Top: None
#    ```

# 2. **After Push '4':**
#    ```
#    Stack: [4]
#    Top: 4
#    ```

# 3. **After Push '5':**
#    ```
#    Stack: [5, 4]
#    Top: 5
#    ```

# 4. **After Push '6':**
#    ```
#    Stack: [6, 5, 4]
#    Top: 6
#    ```

# 5. **After Push '7':**
#    ```
#    Stack: [7, 6, 5, 4]
#    Top: 7
#    ```

# 6. **After Pop (removes '7'):**
#    ```
#    Stack: [6, 5, 4]
#    Top: 6
#    ```

# If you have any more questions or need further clarification, feel free to ask!