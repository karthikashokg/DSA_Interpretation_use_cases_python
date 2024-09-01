
class Queue:  
    def __init__(self):  
        self.Stack1 = []  # Initialize the first stack
        self.Stack2 = []  # Initialize the second stack
                
    def enqueue(self, data):  
        self.Stack1.append(data)  # Push the data onto Stack1
        
    def dequeue(self):   
        if not self.Stack2:  # If Stack2 is empty
            while self.Stack1:  # Transfer all elements from Stack1 to Stack2
                self.Stack2.append(self.Stack1.pop())  
        if not self.Stack2:  # If Stack2 is still empty after transfer
            print("No element to dequeue")  # Print a message if there are no elements to dequeue
            return
        return self.Stack2.pop()  # Pop the element from Stack2 and return it
      
# Create an instance of Queue
queue = Queue()  

# Enqueue elements into the queue
queue.enqueue(5)  
queue.enqueue(6)  
queue.enqueue(7)  
print(queue.Stack1)  # Print the current elements in Stack1
# Output: [5, 6, 7]

# Dequeue an element from the queue
queue.dequeue()  
print(queue.Stack1)  # Print the current elements in Stack1
# Output: []
print(queue.Stack2)  # Print the current elements in Stack2
# Output: [7, 6]

# Dequeue another element from the queue
queue.dequeue()  
print(queue.Stack2)  # Print the current elements in Stack2
# Output: [7]



###############################################################################################

# ### Time and Space Complexities

# - **`enqueue` function:**
#   - **Time Complexity:** O(1) for adding a new element to Stack1.
#   - **Space Complexity:** O(1) for the additional element added to Stack1.

# - **`dequeue` function:**
#   - **Time Complexity:** Amortized O(1). In the worst case, it is O(n) when transferring elements from Stack1 to Stack2, but this happens only when Stack2 is empty.
#   - **Space Complexity:** O(1) for the element removed from Stack2.

# ### Visual Representation

# Here's a visual representation of how the queue works using two stacks:

# 1. **Initial State:**
#    ```
#    Stack1: []
#    Stack2: []
#    ```

# 2. **After Enqueue 5:**
#    ```
#    Stack1: [5]
#    Stack2: []
#    ```

# 3. **After Enqueue 6:**
#    ```
#    Stack1: [5, 6]
#    Stack2: []
#    ```

# 4. **After Enqueue 7:**
#    ```
#    Stack1: [5, 6, 7]
#    Stack2: []
#    ```

# 5. **After Dequeue (transfers elements from Stack1 to Stack2 and removes 5):**
#    ```
#    Stack1: []
#    Stack2: [7, 6]
#    ```

# 6. **After Dequeue (removes 6):**
#    ```
#    Stack1: []
#    Stack2: [7]
#    ```

# If you have any more questions or need further clarification, feel free to ask!