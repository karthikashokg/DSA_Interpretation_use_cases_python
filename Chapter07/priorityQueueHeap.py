
class PriorityQueueHeap:
    def __init__(self):
        self.heap = [()]  # Initialize the heap with a dummy element at index 0
        self.size = 0  # Initialize the size of the heap to 0

    def arrange(self, k):
        # Time Complexity: O(log n) - The while loop runs up to the height of the heap.
        # Space Complexity: O(1) - Only a constant amount of extra space is used.
        while k // 2 > 0:  # While the current node has a parent
            if self.heap[k][0] < self.heap[k // 2][0]:  # If the current node's priority is less than its parent's priority
                self.heap[k], self.heap[k // 2] = self.heap[k // 2], self.heap[k]  # Swap them
            k //= 2  # Move up to the parent node

    def insert(self, priority, item):
        # Time Complexity: O(log n) - Due to the arrange function call.
        # Space Complexity: O(1) - Only a constant amount of extra space is used.
        self.heap.append((priority, item))  # Add the new item with its priority to the end of the heap
        self.size += 1  # Increment the size of the heap
        self.arrange(self.size)  # Arrange the heap to maintain the min-heap property

        # Visual Representation:
        # After inserting (2, "Bat"), (13, "Cat"), (18, "Rat"), (26, "Ant"), (3, "Lion"), (4, "Bear"):
        #        (2, "Bat")
        #       /         \
        # (3, "Lion")  (4, "Bear")
        #    /    \       /    \
        # (13, "Cat") (18, "Rat") (26, "Ant")

    def sink(self, k):
        # Time Complexity: O(log n) - The while loop runs up to the height of the heap.
        # Space Complexity: O(1) - Only a constant amount of extra space is used.
        while k * 2 <= self.size:  # While the current node has at least one child
            mc = self.minchild(k)  # Get the index of the minimum child
            if self.heap[k][0] > self.heap[mc][0]:  # If the current node's priority is greater than its minimum child's priority
                self.heap[k], self.heap[mc] = self.heap[mc], self.heap[k]  # Swap them
            k = mc  # Move down to the child node

    def minchild(self, k):
        # Time Complexity: O(1) - Only a few comparisons and arithmetic operations.
        # Space Complexity: O(1) - Only a constant amount of extra space is used.
        if k * 2 + 1 > self.size:  # If the current node has only one child
            return k * 2  # Return the index of the left child
        elif self.heap[k * 2][0] < self.heap[k * 2 + 1][0]:  # If the left child's priority is less than the right child's priority
            return k * 2  # Return the index of the left child
        else:
            return k * 2 + 1  # Return the index of the right child

    def delete_at_root(self):
        # Time Complexity: O(log n) - Due to the sink function call.
        # Space Complexity: O(1) - Only a constant amount of extra space is used.
        item = self.heap[1][1]  # Get the root item
        self.heap[1] = self.heap[self.size]  # Move the last item to the root
        self.size -= 1  # Decrement the size of the heap
        self.heap.pop()  # Remove the last item
        self.sink(1)  # Sink the new root to maintain the min-heap property
        return item  # Return the deleted root item

        # Visual Representation:
        # Before deletion:
        #        (2, "Bat")
        #       /         \
        # (3, "Lion")  (4, "Bear")
        #    /    \       /    \
        # (13, "Cat") (18, "Rat") (26, "Ant")
        # After deletion:
        #        (3, "Lion")
        #       /         \
        # (13, "Cat")  (4, "Bear")
        #    /    \       /    \
        # (26, "Ant") (18, "Rat")

# Create an instance of PriorityQueueHeap and insert elements
h = PriorityQueueHeap()
h.insert(2, "Bat")
h.insert(13, "Cat")
h.insert(18, "Rat")
h.insert(26, "Ant")
h.insert(3, "Lion")
h.insert(4, "Bear")

print(h.heap)  # Print the heap after all insertions

# Delete the root element and print the heap after each deletion
for i in range(h.size):
    n = h.delete_at_root()
    print(n)
    print(h.heap)


##############################################################################################

# ### Visual Representation of PriorityQueueHeap

# 1. **Initial State:**
#    ```
#    Heap: [()]
#    ```

# 2. **After Insertions:**
#    ```
#    Insert (2, "Bat"):
#    Heap: [(), (2, "Bat")]

#    Insert (13, "Cat"):
#    Heap: [(), (2, "Bat"), (13, "Cat")]

#    Insert (18, "Rat"):
#    Heap: [(), (2, "Bat"), (13, "Cat"), (18, "Rat")]

#    Insert (26, "Ant"):
#    Heap: [(), (2, "Bat"), (13, "Cat"), (18, "Rat"), (26, "Ant")]

#    Insert (3, "Lion"):
#    Heap: [(), (2, "Bat"), (3, "Lion"), (18, "Rat"), (26, "Ant"), (13, "Cat")]

#    Insert (4, "Bear"):
#    Heap: [(), (2, "Bat"), (3, "Lion"), (4, "Bear"), (26, "Ant"), (13, "Cat"), (18, "Rat")]
#    ```

# 3. **After Deletions:**
#    ```
#    Delete (2, "Bat"):
#    Heap: [(), (3, "Lion"), (13, "Cat"), (4, "Bear"), (26, "Ant"), (18, "Rat")]

#    Delete (3, "Lion"):
#    Heap: [(), (4, "Bear"), (13, "Cat"), (18, "Rat"), (26, "Ant")]

#    Delete (4, "Bear"):
#    Heap: [(), (13, "Cat"), (26, "Ant"), (18, "Rat")]

#    Delete (13, "Cat"):
#    Heap: [(), (18, "Rat"), (26, "Ant")]

#    Delete (18, "Rat"):
#    Heap: [(), (26, "Ant")]

#    Delete (26, "Ant"):
#    Heap: [()]
#    ```

