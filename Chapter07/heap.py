
class MinHeap:
    def __init__(self):
        self.heap = [0]  # Initialize the heap with a dummy element at index 0
        self.size = 0  # Initialize the size of the heap to 0

    def arrange(self, k):
        # Time Complexity: O(log n) - The while loop runs up to the height of the heap.
        # Space Complexity: O(1) - Only a constant amount of extra space is used.
        while k // 2 > 0:  # While the current node has a parent
            if self.heap[k] < self.heap[k // 2]:  # If the current node is smaller than its parent
                self.heap[k], self.heap[k // 2] = self.heap[k // 2], self.heap[k]  # Swap them
            k //= 2  # Move up to the parent node

    def insert(self, item):
        # Time Complexity: O(log n) - Due to the arrange function call.
        # Space Complexity: O(1) - Only a constant amount of extra space is used.
        self.heap.append(item)  # Add the new item to the end of the heap
        self.size += 1  # Increment the size of the heap
        self.arrange(self.size)  # Arrange the heap to maintain the min-heap property

        # Visual Representation:
        # After inserting 4, 8, 7, 2, 9, 10, 5, 1, 3, 6:
        #        1
        #       / \
        #      2   5
        #     / \  / \
        #    3   4 10 7
        #   / \  / \
        #  8   9 6

    def sink(self, k):
        # Time Complexity: O(log n) - The while loop runs up to the height of the heap.
        # Space Complexity: O(1) - Only a constant amount of extra space is used.
        while k * 2 <= self.size:  # While the current node has at least one child
            mc = self.minchild(k)  # Get the index of the minimum child
            if self.heap[k] > self.heap[mc]:  # If the current node is larger than its minimum child
                self.heap[k], self.heap[mc] = self.heap[mc], self.heap[k]  # Swap them
            k = mc  # Move down to the child node

    def minchild(self, k):
        # Time Complexity: O(1) - Only a few comparisons and arithmetic operations.
        # Space Complexity: O(1) - Only a constant amount of extra space is used.
        if k * 2 + 1 > self.size:  # If the current node has only one child
            return k * 2  # Return the index of the left child
        elif self.heap[k * 2] < self.heap[k * 2 + 1]:  # If the left child is smaller than the right child
            return k * 2  # Return the index of the left child
        else:
            return k * 2 + 1  # Return the index of the right child

    def delete_at_root(self):
        # Time Complexity: O(log n) - Due to the sink function call.
        # Space Complexity: O(1) - Only a constant amount of extra space is used.
        item = self.heap[1]  # Get the root item
        self.heap[1] = self.heap[self.size]  # Move the last item to the root
        self.size -= 1  # Decrement the size of the heap
        self.heap.pop()  # Remove the last item
        self.sink(1)  # Sink the new root to maintain the min-heap property
        return item  # Return the deleted root item

        # Visual Representation:
        # Before deletion:
        #        1
        #       / \
        #      2   5
        #     / \  / \
        #    3   4 10 7
        #   / \  / \
        #  8   9 6
        # After deletion:
        #        2
        #       / \
        #      3   5
        #     / \  / \
        #    6   4 10 7
        #   / \
        #  8   9

    def delete_at_location(self, location):
        # Time Complexity: O(log n) - Due to the sink function call.
        # Space Complexity: O(1) - Only a constant amount of extra space is used.
        item = self.heap[location]  # Get the item at the specified location
        self.heap[location] = self.heap[self.size]  # Move the last item to the specified location
        self.size -= 1  # Decrement the size of the heap
        self.heap.pop()  # Remove the last item
        self.sink(location)  # Sink the new item to maintain the min-heap property
        return item  # Return the deleted item

        # Visual Representation:
        # Before deletion at location 2:
        #        2
        #       / \
        #      3   5
        #     / \  / \
        #    6   4 10 7
        #   / \
        #  8   9
        # After deletion at location 2:
        #        2
        #       / \
        #      4   5
        #     / \  / \
        #    6   9 10 7
        #   /
        #  8

# Create an instance of MinHeap and insert elements
h = MinHeap()
for i in (4, 8, 7, 2, 9, 10, 5, 1, 3, 6):
    h.insert(i)
print(h.heap)  # Print the heap after all insertions

# Delete the root element
n = h.delete_at_root()
print(n)  # Print the deleted root element
print(h.heap)  # Print the heap after deletion

# Create another instance of MinHeap and insert elements
h = MinHeap()  
for i in (4, 8, 7, 2, 9, 10, 5, 1, 3, 6):  
    h.insert(i)    
print(h.heap)  # Print the heap after all insertions

# Delete the element at location 2
n = h.delete_at_location(2)
print(n)  # Print the deleted element
print(h.heap)  # Print the heap after deletion


