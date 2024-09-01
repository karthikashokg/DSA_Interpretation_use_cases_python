class ListQueue:  
    def __init__(self):  
        self.items = []  # Initialize an empty list to store queue elements
        self.front = self.rear = 0  # Initialize front and rear pointers to 0
        self.size = 3  # Set the maximum capacity of the queue to 3
        
    def enqueue(self, data):  
        if self.size == self.rear:  # Check if the queue is full
            print("\nQueue is full")  # Print a message if the queue is full
        else:   
            self.items.append(data)  # Add the new element to the end of the list
            self.rear += 1  # Increment the rear pointer
            
    def dequeue(self):
        if self.front == self.rear:  # Check if the queue is empty
            print("Queue is empty")  # Print a message if the queue is empty
        else:
            data = self.items.pop(0)  # Remove the element from the front of the list
            self.rear -= 1  # Decrement the rear pointer
            return data  # Return the removed element

# Create an instance of ListQueue
q = ListQueue()

# Enqueue elements into the queue
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)  # This will print "Queue is full" because the queue can only hold 3 elements

print(q.items)  # Print the current elements in the queue
# Output: [20, 30, 40]

# Dequeue an element from the queue
data = q.dequeue()
print(data)  # Print the dequeued element
# Output: 20

print(q.items)  # Print the current elements in the queue
# Output: [30, 40]

# Attempt to call a non-existent method size1() (this will raise an AttributeError)
a = q.size1()
print(a)

###############################################################
Sure, let's break down the code with comments and analyze the time and space complexities. I'll also create a visual representation of how the queue works.



### Time and Space Complexities

- **`enqueue` function:**
  - **Time Complexity:** O(1) for the append operation.
  - **Space Complexity:** O(1) for the additional element added to the list.

- **`dequeue` function:**
  - **Time Complexity:** O(n) because removing the first element from a list requires shifting all other elements.
  - **Space Complexity:** O(1) for the element removed from the list.

### Visual Representation

# Here's a visual representation of how the queue works:

# 1. **Initial State:**
#    ```
#    Queue: []
#    Front: 0
#    Rear: 0
#    ```

# 2. **After Enqueue 20:**
#    ```
#    Queue: [20]
#    Front: 0
#    Rear: 1
#    ```

# 3. **After Enqueue 30:**
#    ```
#    Queue: [20, 30]
#    Front: 0
#    Rear: 2
#    ```

# 4. **After Enqueue 40:**
#    ```
#    Queue: [20, 30, 40]
#    Front: 0
#    Rear: 3
#    ```

# 5. **Attempt to Enqueue 50 (Queue is full):**
#    ```
#    Queue: [20, 30, 40]
#    Front: 0
#    Rear: 3
#    ```

# 6. **After Dequeue (removes 20):**
#    ```
#    Queue: [30, 40]
#    Front: 0
#    Rear: 2
#    ```

# If you have any more questions or need further clarification, feel free to ask!
