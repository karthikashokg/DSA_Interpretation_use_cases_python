class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data  # Initialize the node with data
        self.next = next  # Initialize the next pointer to None
        self.prev = prev  # Initialize the prev pointer to None
        # Time Complexity: O(1)
        # Space Complexity: O(1)

class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the list
        self.tail = None  # Initialize the tail of the list
        self.count = 0    # Initialize the size of the list
        # Time Complexity: O(1)
        # Space Complexity: O(1)

    def append(self, data):
        # Append an item at the end of the list.
        new_node = Node(data)
        if self.head is None:
            self.head = new_node  # If the list is empty, set head to the new node
            self.tail = self.head  # Set tail to the new node as well
        else:
            new_node.prev = self.tail  # Link the new node to the current tail
            self.tail.next = new_node  # Link the current tail to the new node
            self.tail = new_node  # Update the tail to the new node
        self.count += 1  # Increment the size of the list
        # Time Complexity: O(1)
        # Space Complexity: O(1)

    def append_at_start(self, data):
        # Append an item at the beginning of the list.
        new_node = Node(data)
        if self.head is None:
            self.head = new_node  # If the list is empty, set head to the new node
            self.tail = self.head  # Set tail to the new node as well
        else:
            new_node.next = self.head  # Link the new node to the current head
            self.head.prev = new_node  # Link the current head to the new node
            self.head = new_node  # Update the head to the new node
        self.count += 1  # Increment the size of the list
        # Time Complexity: O(1)
        # Space Complexity: O(1)

    def append_at_a_location(self, data):
        # Append an item after a specific data item in the list.
        current = self.head
        prev = self.head
        new_node = Node(data)
        while current:
            if current.data == data:
                new_node.prev = prev  # Link the new node to the previous node
                new_node.next = current  # Link the new node to the current node
                prev.next = new_node  # Link the previous node to the new node
                current.prev = new_node  # Link the current node to the new node
                self.count += 1  # Increment the size of the list
                return
            prev = current  # Move to the next node
            current = current.next
        print("Data item not found in the list.")
        # Time Complexity: O(n) (where n is the number of nodes in the list)
        # Space Complexity: O(1)

    def iter(self):
        current = self.head  # Start from the head of the list
        while current:
            val = current.data  # Get the data of the current node
            current = current.next  # Move to the next node
            yield val  # Yield the data
        # Time Complexity: O(n) (where n is the number of nodes in the list)
        # Space Complexity: O(1)

    def contains(self, data):
        for node_data in self.iter():
            if data == node_data:
                print("Data item is present in the list.")
                return
        print("Data item is not present in the list.")
        return
        # Time Complexity: O(n) (where n is the number of nodes in the list)
        # Space Complexity: O(1)

# Create a DoublyLinkedList instance
words = DoublyLinkedList()
words.append('egg')
words.append('ham')
words.append('spam')

# Visual representation after appending 'egg', 'ham', 'spam':
# +---------+------+     +---------+------+     +---------+------+
# |   egg   |  o-------->|   ham   |  o-------->|  spam   | None |
# +---------+------+     +---------+------+     +---------+------+
# Head: egg
# Tail: spam

print("Items in doubly linked list before append at start:")
current = words.head
while current:
    print(current.data)
    current = current.next

words.append_at_start('book')

# Visual representation after appending 'book' at start:
# +---------+------+     +---------+------+     +---------+------+     +---------+------+
# |  book   |  o-------->|   egg   |  o-------->|   ham   |  o-------->|  spam   | None |
# +---------+------+     +---------+------+     +---------+------+     +---------+------+
# Head: book
# Tail: spam

print("Items in doubly linked list after append at start:")
current = words.head
while current:
    print(current.data)
    current = current.next

words.append('book')

# Visual representation after appending 'book' at end:
# +---------+------+     +---------+------+     +---------+------+     +---------+------+     +---------+------+
# |  book   |  o-------->|   egg   |  o-------->|   ham   |  o-------->|  spam   |  o-------->|  book   | None |
# +---------+------+     +---------+------+     +---------+------+     +---------+------+     +---------+------+
# Head: book
# Tail: book

print("Items in doubly linked list after adding element at end:")
current = words.head
while current:
    print(current.data)
    current = current.next

words.append_at_a_location('ham')

# Visual representation after appending 'ham' after 'ham':
# +---------+------+     +---------+------+     +---------+------+     +---------+------+     +---------+------+     +---------+------+
# |  book   |  o-------->|   egg   |  o-------->|   ham   |  o-------->|   ham   |  o-------->|  spam   |  o-------->|  book   | None |
# +---------+------+     +---------+------+     +---------+------+     +---------+------+     +---------+------+     +---------+------+
# Head: book
# Tail: book

print("Doubly linked list after adding an element after word 'ham' in the list:")
current = words.head
while current:
    print(current.data)
    current = current.next

words = DoublyLinkedList()
words.append('egg')
words.append('ham')
words.append('spam')

words.contains("ham")
words.contains("ham2")
