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
        # Increment the size of the list
        self.size += 1
            
    def delete_first_node (self): 
        current = self.head  
        if self.head is None:
            # If the list is empty, print a message
            print("No data element to delete")
        elif current == self.head:
            # If the list is not empty, set the head to the next node
            self.head = current.next
            
          
    def delete_last_node (self): 
        current = self.head 
        prev = self.head
        while current:
            if current.next is None:
                # If it's the last node, set the previous node's next to None
                prev.next = current.next 
                self.size -= 1
            prev = current
            current = current.next
            

    def delete(self, data): 
        current = self.head 
        prev = self.head 
        while current:
            if current.data == data:
                if current == self.head:
                    # If the node to be deleted is the head, set head to next node
                    self.head = current.next 
                else:
                    # Otherwise, set the previous node's next to current's next
                    prev.next = current.next 
                self.size -= 1
                return
            prev = current
            current = current.next
            
            
# Create a new singly linked list
words = SinglyLinkedList()
# Append 'egg' to the list
words.append('egg')
# Append 'ham' to the list
words.append('ham')
# Append 'spam' to the list
words.append('spam')

# Delete the first node from the list
words.delete_first_node()

# Print all elements in the list after deleting first node
current = words.head
while current:
    print(current.data)
    current = current.next


# Delete the last node from the list    
words.delete_last_node()

# Print all elements in the list after deleting last node
current = words.head
while current:
    print(current.data)
    current = current.next
    
    
# Delete 'ham' from the list    
words.delete('ham')

# Print all elements in the list after deleting 'ham'
current = words.head
while current:
    print(current.data)
    current = current.next
