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
        # Append an item to the list.
        new_node = Node(data)  # Create a new node with the given data
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

    def delete(self, data):
        # Delete a node from the list.
        current = self.head  # Start from the head of the list
        node_deleted = False  # Flag to check if the node is deleted
        if current is None:  # List is empty
            print("List is empty")
        elif current.data == data:  # Item to be deleted is found at the start of the list
            self.head = current.next  # Update the head to the next node
            if self.head is not None:
                self.head.prev = None  # Set the previous pointer of the new head to None
            node_deleted = True
        elif self.tail.data == data:  # Item to be deleted is found at the end of the list
            self.tail = self.tail.prev  # Update the tail to the previous node
            if self.tail is not None:
                self.tail.next = None  # Set the next pointer of the new tail to None
            node_deleted = True
        else:
            while current:  # Search for the item to be deleted
                if current.data == data:
                    current.prev.next = current.next  # Bypass the current node
                    if current.next is not None:
                        current.next.prev = current.prev  # Update the previous pointer of the next node
                    node_deleted = True
                    break
                current = current.next
            if not node_deleted:  # Item to be deleted is not found in the list
                print("Item not found")
        if node_deleted:
            self.count -= 1  # Decrement the size of the list
        # Time Complexity: O(n) (where n is the number of nodes in the list)
        # Space Complexity: O(1)

# Code to create a doubly linked list
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

current = words.head
while current:
    print(current.data)
    current = current.next

words.delete('ham')

# Visual representation after deleting 'ham':
# +---------+------+     +---------+------+
# |   egg   |  o-------->|  spam   | None |
# +---------+------+     +---------+------+
# Head: egg
# Tail: spam

current = words.head
while current:
    print(current.data)
    current = current.next

words.delete('spam')

# Visual representation after deleting 'spam':
# +---------+------+
# |   egg   | None |
# +---------+------+
# Head: egg
# Tail: egg

current = words.head
while current:
    print(current.data)
    current = current.next
