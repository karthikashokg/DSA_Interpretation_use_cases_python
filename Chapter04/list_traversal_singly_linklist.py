class Node:
    """ A singly-linked node. """
    def __init__(self, data=None):
        # Initialize the node with data and set the next pointer to None
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__ (self):
        # Initialize the linked list with head as None and size as 0
        self.head = None
        self.size = 0
        
    def append(self, data):
        # Encapsulate the data in a Node 
        node = Node(data)
        if self.head is None:
            # If the list is empty, set the new node as the head
            self.head = node    
        else: 
            # Traverse to the end of the list and add the new node
            current = self.head 
            while current.next:
                current = current.next 
            current.next = node
    
    def iter(self):
        # Initialize current to head of the list
        current = self.head 
        while current:
            # Yield the data of the current node and move to the next node
            val = current.data 
            current = current.next 
            yield val

            
# Create a new singly linked list
words = SinglyLinkedList()
# Append 'egg' to the list
words.append('egg')
# Append 'ham' to the list
words.append('ham')
# Append 'spam' to the list
words.append('spam')

# Iterate through the list and print each element
for word in words.iter():
    print(word)
