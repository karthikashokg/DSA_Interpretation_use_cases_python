
class MinHeap:
    def __init__(self):
        self.heap = [0]  # Initialize the heap with a dummy element at index 0
        self.size = 0  # Initialize the size of the heap to 0

    def arrange(self, k):
        while k // 2 > 0:  # While the current node has a parent
            if self.heap[k] < self.heap[k // 2]:  # If the current node is smaller than its parent
                self.heap[k], self.heap[k // 2] = self.heap[k // 2], self.heap[k]  # Swap them
            k //= 2  # Move up to the parent node

    def insert(self, item):
        self.heap.append(item)  # Add the new item to the end of the heap
        self.size += 1  # Increment the size of the heap
        self.arrange(self.size)  # Arrange the heap to maintain the min-heap property

    def sink(self, k):
        while k * 2 <= self.size:  # While the current node has at least one child
            mc = self.minchild(k)  # Get the index of the minimum child
            if self.heap[k] > self.heap[mc]:  # If the current node is larger than its minimum child
                self.heap[k], self.heap[mc] = self.heap[mc], self.heap[k]  # Swap them
            k = mc  # Move down to the child node

    def minchild(self, k):
        if k * 2 + 1 > self.size:  # If the current node has only one child
            return k * 2  # Return the index of the left child
        elif self.heap[k * 2] < self.heap[k * 2 + 1]:  # If the left child is smaller than the right child
            return k * 2  # Return the index of the left child
        else:
            return k * 2 + 1  # Return the index of the right child

    def delete_at_root(self):
        item = self.heap[1]  # Get the root item
        self.heap[1] = self.heap[self.size]  # Move the last item to the root
        self.size -= 1  # Decrement the size of the heap
        self.heap.pop()  # Remove the last item
        self.sink(1)  # Sink the new root to maintain the min-heap property
        return item  # Return the deleted root item

    def delete_at_location(self, location):
        item = self.heap[location]  # Get the item at the specified location
        self.heap[location] = self.heap[self.size]  # Move the last item to the specified location
        self.size -= 1  # Decrement the size of the heap
        self.heap.pop()  # Remove the last item
        self.sink(location)  # Sink the new item to maintain the min-heap property
        return item  # Return the deleted item
        
    def heap_sort(self):  
        sorted_list = []  
        for node in range(self.size):  
            n = self.delete_at_root()  # Pop the root item
            sorted_list.append(n)  # Append it to the sorted list
        return sorted_list  # Return the sorted list
      
# Create an instance of MinHeap and insert elements
h = MinHeap()
for i in (4, 8, 7, 2, 9, 10, 5, 1, 3, 6):
    h.insert(i)
print(h.heap)  # Print the heap after all insertions

# Create another instance of MinHeap and insert elements from an unsorted list
h = MinHeap()  
unsorted_list = [4, 8, 7, 2, 9, 10, 5, 1, 3, 6]  
for i in unsorted_list:  
    h.insert(i)  
print("Unsorted list: {}".format(unsorted_list))  # Print the unsorted list

# Print the sorted list using heap sort
print("Sorted list: {}".format(h.heap_sort()))  


#######################################################################################

# ### Time and Space Complexities

# - **`__init__` function:**
#   - **Time Complexity:** O(1) because it initializes the heap and size.
#   - **Space Complexity:** O(1) for the initial heap list and size variable.

# - **`arrange` function:**
#   - **Time Complexity:** O(log n) because it may need to traverse up the height of the heap, which is logarithmic in terms of the number of elements.
#   - **Space Complexity:** O(1) because it only uses a constant amount of extra space for swapping elements.

# - **`insert` function:**
#   - **Time Complexity:** O(log n) due to the `arrange` function call.
#   - **Space Complexity:** O(1) for the additional element added to the heap.

# - **`sink` function:**
#   - **Time Complexity:** O(log n) because it may need to traverse down the height of the heap.
#   - **Space Complexity:** O(1) because it only uses a constant amount of extra space for swapping elements.

# - **`minchild` function:**
#   - **Time Complexity:** O(1) because it only involves a few comparisons and arithmetic operations.
#   - **Space Complexity:** O(1) because it only uses a constant amount of extra space.

# - **`delete_at_root` function:**
#   - **Time Complexity:** O(log n) due to the `sink` function call.
#   - **Space Complexity:** O(1) for the element removed from the heap.

# - **`delete_at_location` function:**
#   - **Time Complexity:** O(log n) due to the `sink` function call.
#   - **Space Complexity:** O(1) for the element removed from the heap.

# - **`heap_sort` function:**
#   - **Time Complexity:** O(n log n) because it repeatedly calls `delete_at_root`, which is O(log n), for each of the n elements.
#   - **Space Complexity:** O(n) for the sorted list that stores the elements.



### Visual Representation of MinHeap

# 1. **Initial State:**
#    ```
#    Heap: [0]
#    ```

# 2. **After Insert 4:**
#    ```
#        4
#    Heap: [0, 4]
#    ```

# 3. **After Insert 8:**
#    ```
#        4
#       / 
#      8
#    Heap: [0, 4, 8]
#    ```

# 4. **After Insert 7:**
#    ```
#        4
#       / \
#      8   7
#    Heap: [0, 4, 8, 7]
#    ```

# 5. **After Insert 2:**
#    ```
#        2
#       / \
#      4   7
#     /
#    8
#    Heap: [0, 2, 4, 7, 8]
#    ```

# 6. **After Insert 9:**
#    ```
#        2
#       / \
#      4   7
#     / \
#    8   9
#    Heap: [0, 2, 4, 7, 8, 9]
#    ```

# 7. **After Insert 10:**
#    ```
#        2
#       / \
#      4   7
#     / \  /
#    8   9 10
#    Heap: [0, 2, 4, 7, 8, 9, 10]
#    ```

# 8. **After Insert 5:**
#    ```
#        2
#       / \
#      4   5
#     / \  / \
#    8   9 10 7
#    Heap: [0, 2, 4, 5, 8, 9, 10, 7]
#    ```

# 9. **After Insert 1:**
#    ```
#        1
#       / \
#      2   5
#     / \  / \
#    4   9 10 7
#   /
#  8
#    Heap: [0, 1, 2, 5, 4, 9, 10, 7, 8]
#    ```

# 10. **After Insert 3:**
#     ```
#        1
#       / \
#      2   5
#     / \  / \
#    4   3 10 7
#   / \
#  8   9
#     Heap: [0, 1, 2, 5, 4, 3, 10, 7, 8, 9]
#     ```

# 11. **After Insert 6:**
#     ```
#        1
#       / \
#      2   5
#     / \  / \
#    4   3 10 7
#   / \  /
#  8   9 6
#     Heap: [0, 1, 2, 5, 4, 3, 10, 7, 8, 9, 6]
#     ```

# This visual representation helps to understand how the MinHeap maintains its properties after each insertion.


# ### Visual Representation of MinHeap Deletion

# 1. **Initial Heap:**
#    ```
#        1
#       / \
#      2   5
#     / \  / \
#    4   3 10 7
#   / \  /
#  8   9 6
#    Heap: [0, 1, 2, 5, 4, 3, 10, 7, 8, 9, 6]
#    ```

# 2. **After Deleting Root (1):**
#    - Move the last element (6) to the root.
#    - Sink the new root to maintain the min-heap property.
#    ```
#        2
#       / \
#      4   5
#     / \  / \
#    6   3 10 7
#   / \
#  8   9
#    Heap: [0, 2, 4, 5, 6, 3, 10, 7, 8, 9]
#    ```

# 3. **After Deleting Root (2):**
#    - Move the last element (9) to the root.
#    - Sink the new root to maintain the min-heap property.
#    ```
#        3
#       / \
#      4   5
#     / \  / \
#    6   9 10 7
#   / \
#  8
#    Heap: [0, 3, 4, 5, 6, 9, 10, 7, 8]
#    ```

# 4. **After Deleting Root (3):**
#    - Move the last element (8) to the root.
#    - Sink the new root to maintain the min-heap property.
#    ```
#        4
#       / \
#      6   5
#     / \  / \
#    8   9 10 7
#    Heap: [0, 4, 6, 5, 8, 9, 10, 7]
#    ```

# 5. **After Deleting Root (4):**
#    - Move the last element (7) to the root.
#    - Sink the new root to maintain the min-heap property.
#    ```
#        5
#       / \
#      6   7
#     / \  /
#    8   9 10
#    Heap: [0, 5, 6, 7, 8, 9, 10]
#    ```

# 6. **After Deleting Root (5):**
#    - Move the last element (10) to the root.
#    - Sink the new root to maintain the min-heap property.
#    ```
#        6
#       / \
#      8   7
#     / \
#    10  9
#    Heap: [0, 6, 8, 7, 10, 9]
#    ```

# 7. **After Deleting Root (6):**
#    - Move the last element (9) to the root.
#    - Sink the new root to maintain the min-heap property.
#    ```
#        7
#       / \
#      8   9
#     /
#    10
#    Heap: [0, 7, 8, 9, 10]
#    ```

# 8. **After Deleting Root (7):**
#    - Move the last element (10) to the root.
#    - Sink the new root to maintain the min-heap property.
#    ```
#        8
#       / \
#      10  9
#    Heap: [0, 8, 10, 9]
#    ```

# 9. **After Deleting Root (8):**
#    - Move the last element (9) to the root.
#    - Sink the new root to maintain the min-heap property.
#    ```
#        9
#       /
#      10
#    Heap: [0, 9, 10]
#    ```

# 10. **After Deleting Root (9):**
#     - Move the last element (10) to the root.
#     - Sink the new root to maintain the min-heap property.
#     ```
#        10
#    Heap: [0, 10]
#     ```

# 11. **After Deleting Root (10):**
#     - The heap is now empty.
#     ```
#    Heap: [0]
