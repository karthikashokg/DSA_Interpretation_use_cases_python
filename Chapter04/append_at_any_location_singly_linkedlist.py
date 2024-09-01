class Node:
    """ A singly-linked node. """
    def __init__(self, data=None):
        self.data = data  # Initialize the node with data
        self.next = None  # Initialize the next pointer to None
        # Time Complexity: O(1)
        # Space Complexity: O(1)

class SinglyLinkedList:
    def __init__(self):
        self.tail = None  # Initialize the tail of the list
        self.head = None  # Initialize the head of the list
        self.size = 0     # Initialize the size of the list
        # Time Complexity: O(1)
        # Space Complexity: O(1)

    def append(self, data):
        # Encapsulate the data in a Node
        node = Node(data)
        if self.head is None:
            self.head = node  # If the list is empty, set head to the new node
        else:
            current = self.head
            while current.next:
                current = current.next  # Traverse to the end of the list
            current.next = node  # Link the last node to the new node
        self.size += 1  # Increment the size of the list
        # Time Complexity: O(n) (where n is the number of nodes in the list)
        # Space Complexity: O(1)

    def append_at_a_location(self, data, index):
        if index < 1 or index > self.size + 1:
            print("Index out of bounds")
            return
        node = Node(data)
        if index == 1:
            node.next = self.head  # Insert at the head
            self.head = node
        else:
            current = self.head
            for _ in range(index - 2):
                current = current.next  # Traverse to the node before the insertion point
            node.next = current.next  # Link the new node to the next node
            current.next = node  # Link the previous node to the new node
        self.size += 1  # Increment the size of the list
        # Time Complexity: O(n) (where n is the number of nodes in the list)
        # Space Complexity: O(1)

# Create a SinglyLinkedList instance
words = SinglyLinkedList()
words.append('egg')
words.append('ham')
words.append('spam')

# Visual representation after appending 'egg', 'ham', 'spam':
# +---------+------+     +---------+------+     +---------+------+
# |   egg   |  o-------->|   ham   |  o-------->|  spam   | None |
# +---------+------+     +---------+------+     +---------+------+

# Print the list
current = words.head
while current:
    print(current.data)
    current = current.next

# Append 'new' at index 2
words.append_at_a_location('new', 2)

# Visual representation after appending 'new' at index 2:
# +---------+------+     +---------+------+     +---------+------+     +---------+------+
# |   egg   |  o-------->|   new   |  o-------->|   ham   |  o-------->|  spam   | None |
# +---------+------+     +---------+------+     +---------+------+     +---------+------+

# Print the list again
current = words.head
while current:
    print(current.data)
    current = current.next
