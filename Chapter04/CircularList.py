class Node:
    """ A Circular linked node. """
    def __init__(self, data=None):
        self.data = data  # Initialize the node with data
        self.next = None  # Initialize the next pointer to None
        # Time Complexity: O(1)
        # Space Complexity: O(1)

class CircularList:
    def __init__(self):
        self.tail = None  # Initialize the tail of the list
        self.head = None  # Initialize the head of the list
        self.size = 0     # Initialize the size of the list
        # Time Complexity: O(1)
        # Space Complexity: O(1)

    def append(self, data):
        node = Node(data)  # Create a new node with the given data
        if self.tail:
            self.tail.next = node  # Link the new node to the current tail
            self.tail = node       # Update the tail to the new node
            node.next = self.head  # Make the list circular by linking new tail to head
            # Visual:
            # +---------+------+     +---------+------+
            # |  eggs   |  o-------->|   ham   |  o---+
            # +---------+------+     +---------+------+
        else:
            self.head = node       # If the list is empty, set head to the new node
            self.tail = node       # Set tail to the new node as well
            self.tail.next = self.tail  # Link the tail to itself
            # Visual:
            # +---------+------+
            # |  eggs   |  o---+
            # +---------+------+
        self.size += 1  # Increment the size of the list
        # Time Complexity: O(1)
        # Space Complexity: O(1)

    def delete(self, data):
        current = self.head  # Start from the head of the list
        prev = self.head     # Keep track of the previous node
        flag = False         # Flag to check if the item is found
        while prev == current or prev != self.tail:
            if current.data == data:
                if current == self.head:
                    # Item to be deleted is the head node
                    self.head = current.next
                    self.tail.next = self.head
                    # Visual:
                    # +---------+------+     +---------+------+
                    # |  eggs   |  o-------->|  spam   |  o----+
                    # +---------+------+     +---------+------+
                    #      ^                          |
                    #      |--------------------------+
                elif current == self.tail:
                    # Item to be deleted is the tail node
                    self.tail = prev
                    prev.next = self.head
                    # Visual:
                    # +---------+------+     +---------+------+
                    # |  eggs   |  o-------->|  spam   |  o----+
                    # +---------+------+     +---------+------+
                    #      ^                          |
                    #      |--------------------------+
                else:
                    # Item to be deleted is an intermediate node
                    prev.next = current.next
                    # Visual:
                    # +---------+------+     +---------+------+
                    # |  eggs   |  o-------->|  spam   |  o----+
                    # +---------+------+     +---------+------+
                    #      ^                          |
                    #      |--------------------------+
                self.size -= 1  # Decrement the size of the list
                return
            prev = current  # Move to the next node
            current = current.next
        if flag is False:
            print("Item not present in the list")
        # Time Complexity: O(n) in the worst case (where n is the number of nodes in the list)
        # Space Complexity: O(1)

    def iter(self):
        current = self.head  # Start from the head of the list
        while current:
            val = current.data  # Get the data of the current node
            current = current.next  # Move to the next node
            yield val  # Yield the data
            if current == self.head:
                break
        # Time Complexity: O(n) (where n is the number of nodes in the list)
        # Space Complexity: O(1)

# Create a CircularList instance
words = CircularList()
words.append('eggs')
words.append('ham')
words.append('spam')

# Iterate through the list
counter = 0
for word in words.iter():
    print(word)
    counter += 1
    if counter > 2:
        break

words.append('foo')
words.append('bar')
words.append('bim')
words.append('baz')
words.append('quux')
words.append('duux')

print("Done iterating. Now we try to delete something that isn't there.")
words.delete('socks')
print('back to iterating')
counter = 0
for item in words.iter():
    print(item)
    counter += 1
    if counter > 2:
        break

print('Let us delete something that is there.')
words.delete('foo')
print('back to iterating')
counter = 0
for item in words.iter():
    print(item)
    counter += 1
    if counter > 2:
        break
