class Node(object):
    def __init__(self, data=None, next=None, prev=None):
        # Initialize the node with data, next pointer, and previous pointer
        self.data = data
        self.next = next
        self.prev = prev
        # Time Complexity: O(1)
        # Space Complexity: O(1)

class Queue: 
    def __init__(self): 
        # Initialize the queue with head and tail as None and count as 0
        self.head = None 
        self.tail = None 
        self.count = 0 
        # Time Complexity: O(1)
        # Space Complexity: O(1)

    def enqueue(self, data): 
        # Create a new node with the given data
        new_node = Node(data, None, None) 
        if self.head is None: 
            # If the queue is empty, set the new node as both head and tail
            self.head = new_node 
            self.tail = self.head 
        else: 
            # If the queue is not empty, add the new node to the end of the queue
            new_node.prev = self.tail 
            self.tail.next = new_node 
            self.tail = new_node 
        # Increment the count of elements in the queue
        self.count += 1 
        # Time Complexity: O(1)
        # Space Complexity: O(1)

    def dequeue(self): 
        if self.count == 1: 
            # If there is only one element in the queue, remove it and set head and tail to None
            self.count -= 1 
            self.head = None 
            self.tail = None 
        elif self.count > 1: 
            # If there are more than one elements in the queue, remove the head element
            self.head = self.head.next 
            self.head.prev = None 
        elif self.count < 1:
            # If the queue is empty, print a message
            print("Queue is empty")
        # Decrement the count of elements in the queue
        self.count -= 1 
        # Time Complexity: O(1)
        # Space Complexity: O(1)

# Create a new queue
q = Queue()
# Enqueue elements into the queue
q.enqueue(4)
# Visual representation after enqueueing 4:
# Head -> [4] <- Tail

q.enqueue('dog')
# Visual representation after enqueueing 'dog':
# Head -> [4] <-> ['dog'] <- Tail

q.enqueue('True')
# Visual representation after enqueueing 'True':
# Head -> [4] <-> ['dog'] <-> ['True'] <- Tail

# Print the count of elements in the queue
print(q.count)  # Output: 3

# Dequeue an element from the queue
q.dequeue()
# Visual representation after dequeueing:
# Head -> ['dog'] <-> ['True'] <- Tail

# Print the count of elements in the queue
print(q.count)  # Output: 2



# Sure! Let's go through the code step-by-step to understand what it does in detail, including the time and space complexities for each function. I'll also provide visual representations of the queue at different stages.

# ### Code with Comments and Visuals

# ```python
# class Node(object):
#     def __init__(self, data=None, next=None, prev=None):
#         # Initialize the node with data, next pointer, and previous pointer
#         self.data = data
#         self.next = next
#         self.prev = prev
#         # Time Complexity: O(1)
#         # Space Complexity: O(1)

# class Queue: 
#     def __init__(self): 
#         # Initialize the queue with head and tail as None and count as 0
#         self.head = None 
#         self.tail = None 
#         self.count = 0 
#         # Time Complexity: O(1)
#         # Space Complexity: O(1)

#     def enqueue(self, data): 
#         # Create a new node with the given data
#         new_node = Node(data, None, None) 
#         if self.head is None: 
#             # If the queue is empty, set the new node as both head and tail
#             self.head = new_node 
#             self.tail = self.head 
#         else: 
#             # If the queue is not empty, add the new node to the end of the queue
#             new_node.prev = self.tail 
#             self.tail.next = new_node 
#             self.tail = new_node 
#         # Increment the count of elements in the queue
#         self.count += 1 
#         # Time Complexity: O(1)
#         # Space Complexity: O(1)

#     def dequeue(self): 
#         if self.count == 1: 
#             # If there is only one element in the queue, remove it and set head and tail to None
#             self.count -= 1 
#             self.head = None 
#             self.tail = None 
#         elif self.count > 1: 
#             # If there are more than one elements in the queue, remove the head element
#             self.head = self.head.next 
#             self.head.prev = None 
#         elif self.count < 1:
#             # If the queue is empty, print a message
#             print("Queue is empty")
#         # Decrement the count of elements in the queue
#         self.count -= 1 
#         # Time Complexity: O(1)
#         # Space Complexity: O(1)

# # Create a new queue
# q = Queue()
# # Enqueue elements into the queue
# q.enqueue(4)
# # Visual representation after enqueueing 4:
# # Head -> [4] <- Tail

# q.enqueue('dog')
# # Visual representation after enqueueing 'dog':
# # Head -> [4] <-> ['dog'] <- Tail

# q.enqueue('True')
# # Visual representation after enqueueing 'True':
# # Head -> [4] <-> ['dog'] <-> ['True'] <- Tail

# # Print the count of elements in the queue
# print(q.count)  # Output: 3

# # Dequeue an element from the queue
# q.dequeue()
# # Visual representation after dequeueing:
# # Head -> ['dog'] <-> ['True'] <- Tail

# # Print the count of elements in the queue
# print(q.count)  # Output: 2
# ```

# ### Detailed Explanation

# #### Node Class

# The `Node` class represents a node in the doubly linked list used to implement the queue.

# - **`__init__`**: Initializes the node with data, and sets the next and previous pointers to `None`.

# #### Queue Class

# The `Queue` class implements a queue using a doubly linked list.

# - **`__init__`**: Initializes the queue with `head` and `tail` as `None` and `count` as `0`.

# - **`enqueue`**: Adds a new element to the end of the queue.
#   - Creates a new node with the given data.
#   - If the queue is empty, sets the new node as both `head` and `tail`.
#   - If the queue is not empty, adds the new node to the end of the queue and updates the `tail`.
#   - Increments the count of elements in the queue.

# - **`dequeue`**: Removes an element from the front of the queue.
#   - If there is only one element in the queue, removes it and sets `head` and `tail` to `None`.
#   - If there are more than one elements in the queue, removes the `head` element and updates the `head`.
#   - If the queue is empty, prints a message.
#   - Decrements the count of elements in the queue.

# ### Visual Representations

# 1. **After Enqueueing 4**:
# ```
# Head -> [4] <- Tail
# ```

# 2. **After Enqueueing 'dog'**:
# ```
# Head -> [4] <-> ['dog'] <- Tail
# ```

# 3. **After Enqueueing 'True'**:
# ```
# Head -> [4] <-> ['dog'] <-> ['True'] <- Tail
# ```

# 4. **After Dequeueing**:
# ```
# Head -> ['dog'] <-> ['True'] <- Tail
# ```

# ### Time and Space Complexities

# - **Node class**:
#   - `__init__`: 
#     - Time Complexity: \(O(1)\)
#     - Space Complexity: \(O(1)\)

# - **Queue class**:
#   - `__init__`: 
#     - Time Complexity: \(O(1)\)
#     - Space Complexity: \(O(1)\)
#   - `enqueue`: 
#     - Time Complexity: \(O(1)\)
#     - Space Complexity: \(O(1)\)
#   - `dequeue`: 
#     - Time Complexity: \(O(1)\)
#     - Space Complexity: \(O(1)\)

# This detailed explanation should help you understand how the queue is implemented and how it works. If you have any more questions or need further assistance, feel free to ask!