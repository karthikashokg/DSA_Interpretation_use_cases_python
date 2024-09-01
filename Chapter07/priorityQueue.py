
# Class for Node with data and priority
class Node:
    def __init__(self, info, priority):
        self.info = info  # Initialize the node with data
        self.priority = priority  # Initialize the node with priority

# Class for Priority Queue
class PriorityQueue:
    def __init__(self):
        self.queue = []  # Initialize an empty list to store the queue elements
    
    def size(self):
        # Time Complexity: O(1) - Getting the length of the list is a constant time operation.
        # Space Complexity: O(1) - No additional space is used.
        return len(self.queue)  # Return the size of the queue
 
    def show(self):
        # Time Complexity: O(n) - Iterating through the list takes linear time.
        # Space Complexity: O(1) - No additional space is used.
        for x in self.queue:
            print(str(x.info) + " - " + str(x.priority))  # Print each element's info and priority

    def insert(self, node):
        # Time Complexity: O(n) - In the worst case, we may need to traverse the entire list.
        # Space Complexity: O(1) - No additional space is used except for the new node.
        if len(self.queue) == 0:
            # Add the new node if the queue is empty
            self.queue.append(node)
        else:
            # Traverse the queue to find the right place for the new node
            for x in range(0, len(self.queue)):
                # If the priority of the new node is greater
                if node.priority >= self.queue[x].priority:
                    # If we have traversed the complete queue
                    if x == (len(self.queue) - 1):
                        # Add the new node at the end
                        self.queue.insert(x + 1, node)
                    else:
                        continue
                else:
                    # Insert the new node at the correct position
                    self.queue.insert(x, node)
                    return True
    
    def delete(self):
        # Time Complexity: O(1) - Removing the first element is a constant time operation.
        # Space Complexity: O(1) - No additional space is used.
        # Remove the first node from the queue
        x = self.queue.pop(0)
        print("Deleted data with the given priority -", x.info, x.priority)
        return x

# Create an instance of PriorityQueue and insert elements
p = PriorityQueue()
p.insert(Node("Cat", 13))
p.insert(Node("Bat", 2))
p.insert(Node("Rat", 1))
p.insert(Node("Ant", 26))
p.insert(Node("Lion", 25))
p.show()

# Visual Representation after insertions:
# Ant - 26
# Lion - 25
# Cat - 13
# Bat - 2
# Rat - 1

# Delete the highest priority element
p.delete()
p.show()

# Visual Representation after deletion:
# Lion - 25
# Cat - 13
# Bat - 2
# Rat - 1




######################################################################################################
### Visual Representation of PriorityQueue

# 1. **Initial State:**
#    ```
#    Queue: []
#    ```

# 2. **After Insertions:**
#    ```
#    Insert "Cat" with priority 13:
#    Queue: [Cat - 13]

#    Insert "Bat" with priority 2:
#    Queue: [Cat - 13, Bat - 2]

#    Insert "Rat" with priority 1:
#    Queue: [Cat - 13, Bat - 2, Rat - 1]

#    Insert "Ant" with priority 26:
#    Queue: [Ant - 26, Cat - 13, Bat - 2, Rat - 1]

#    Insert "Lion" with priority 25:
#    Queue: [Ant - 26, Lion - 25, Cat - 13, Bat - 2, Rat - 1]
#    ```

# 3. **After Deletion:**
#    ```
#    Delete highest priority element (Ant - 26):
#    Queue: [Lion - 25, Cat - 13, Bat - 2, Rat - 1]
#    ```

# This code includes detailed comments explaining each line, the time and space complexities for each method, and visual representations of the queue structure before and after key operations. If you have any more questions or need further clarification, feel free to ask!