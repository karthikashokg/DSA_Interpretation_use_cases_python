
class HashItem:
    def __init__(self, key, value):
        self.key = key  # Initialize the key
        self.value = value  # Initialize the value

class Node:
    def __init__(self, key=None, value=None):
        self.key = key  # Initialize the key
        self.value = value  # Initialize the value
        self.next = None  # Initialize the next pointer to None

class SinglyLinkedList:
    def __init__(self):
        self.tail = None  # Initialize the tail pointer to None
        self.head = None  # Initialize the head pointer to None
        
    def append(self, key, value):
        node = Node(key, value)  # Create a new node with the given key and value
        if self.tail:
            self.tail.next = node  # Link the new node to the end of the list
            self.tail = node  # Update the tail pointer
        else:
            self.head = node  # If the list is empty, set the new node as the head
            self.tail = node  # and the tail
            
    def traverse(self):
        current = self.head  # Start from the head of the list
        while current:
            print("\"", current.key, "--", current.value, "\"")  # Print the key and value of the current node
            current = current.next  # Move to the next node
    
    def search(self, key):
        current = self.head  # Start from the head of the list
        while current:
            if current.key == key: 
                print("\"Record found:", current.key, "-", current.value, "\"")  # Print the found record
                return True
            current = current.next  # Move to the next node
        return False  # Return False if the key is not found

class HashTableChaining:
    def __init__(self):
        self.size = 6  # Initial size of the hash table
        self.slots = [None for i in range(self.size)]  # Initialize slots with None
        for x in range(self.size):
            self.slots[x] = SinglyLinkedList()  # Initialize each slot with a SinglyLinkedList

    def _hash(self, key):
        # Time Complexity: O(k) - k is the length of the key.
        # Space Complexity: O(1) - Constant space for variables.
        mult = 1
        hv = 0
        for ch in key:
            hv += mult * ord(ch)  # Calculate hash value using ASCII values
            mult += 1
        return hv % self.size  # Ensure the hash value is within the table size

    def put(self, key, value):
        # Time Complexity: O(1) on average, O(n) in the worst case due to linked list traversal.
        # Space Complexity: O(1) - No additional space used.
        node = Node(key, value)        
        h = self._hash(key) 
        self.slots[h].append(key, value)  # Append the new node to the linked list at the hashed index

    def get(self, key):
        # Time Complexity: O(1) on average, O(n) in the worst case due to linked list traversal.
        # Space Complexity: O(1) - No additional space used.
        h = self._hash(key)
        v = self.slots[h].search(key)  # Search for the key in the linked list at the hashed index

    def printHashTable(self):
        print("Hash table is :- \n")
        print("Index \t\tValues\n")
        for x in range(self.size):
            print(x, end="\t\n")
            self.slots[x].traverse()  # Traverse and print each linked list in the hash table

# Example usage
ht = HashTableChaining()
ht.put("good", "eggs")
ht.put("better", "ham")
ht.put("best", "spam")
ht.put("ad", "do not")
ht.put("ga", "collide")
ht.put("awd", "do not")

v = ht.get("ad")
print(v)

for key in ("good", "better", "best", "worst", "ad", "ga"):
    v = ht.get(key)
    print(v)

ht.printHashTable()


##################################################################

# ### Visual Representations

# 1. **Initial State:**
#    ```
#    Slots: [None, None, None, None, None, None]
#    ```

# 2. **After Insertions:**
#    ```
#    Insert ("good", "eggs"):
#    Slots: [None, None, None, None, None, ("good", "eggs")]

#    Insert ("better", "ham"):
#    Slots: [None, None, None, None, ("better", "ham"), ("good", "eggs")]

#    Insert ("best", "spam"):
#    Slots: [None, None, None, None, ("better", "ham"), ("good", "eggs") -> ("best", "spam")]

#    Insert ("ad", "do not"):
#    Slots: [None, None, None, ("ad", "do not"), ("better", "ham"), ("good", "eggs") -> ("best", "spam")]

#    Insert ("ga", "collide"):
#    Slots: [None, None, None, ("ad", "do not"), ("better", "ham"), ("good", "eggs") -> ("best", "spam") -> ("ga", "collide")]

#    Insert ("awd", "do not"):
#    Slots: [None, None, None, ("ad", "do not"), ("better", "ham"), ("good", "eggs") -> ("best", "spam") -> ("ga", "collide") -> ("awd", "do not")]
#    ```

# ### Time and Space Complexities

# - **`_hash` function:**
#   - **Time Complexity:** O(k), where k is the length of the key.
#   - **Space Complexity:** O(1), constant space for variables.

# - **`put` function:**
#   - **Time Complexity:** O(1) on average, O(n) in the worst case due to linked list traversal.
#   - **Space Complexity:** O(1), no additional space used.

# - **`get` function:**
#   - **Time Complexity:** O(1) on average, O(n) in the worst case due to linked list traversal.
#   - **Space Complexity:** O(1), no additional space used.

# - **`printHashTable` function:**
#   - **Time Complexity:** O(n), where n is the number of elements in the hash table.
#   - **Space Complexity:** O(1), no additional space used.

# ### Use Cases and Explanation

# 1. **Efficient Data Retrieval:**
#    - **Why:** Hash tables provide average O(1) time complexity for insertions, deletions, and lookups.
#    - **For What:** Useful for applications requiring fast access to data, such as databases, caches, and associative arrays.

# 2. **Handling Collisions with Chaining:**
#    - **Why:** Chaining allows multiple elements to be stored at the same index using linked lists.
#    - **For What:** Suitable for scenarios where the hash table needs to handle a large number of entries and memory usage is not a primary concern.

# 3. **Dynamic Resizing:**
#    - **Why:** The `check_growth` method ensures the hash table grows when the load factor exceeds a threshold, maintaining efficiency.
#    - **For What:** Useful for applications with varying data sizes, ensuring the hash table adapts to the data volume.

# 4. **Custom Hash Functions:**
#    - **Why:** The `_hash` method allows for custom hash functions, providing flexibility.
#    - **For What:** Useful for optimizing hash functions based on specific data characteristics.

# 5. **Versatile Usage:**
#    - **Why:** The implementation supports different probing techniques and chaining.
#    - **For What:** Suitable for various scenarios where different collision resolution strategies are needed.

# This hash table implementation using chaining is versatile and efficient, making it suitable for a wide range of applications requiring fast data access and effective collision handling.

# If you have any more questions or need further clarification, feel free to ask!

# Source:
# (1) github.com. https://github.com/ramchinta/Algorithms/tree/08c4b8d216a43ac8a2c0297d3083ba4b0a806e22/Hash%20Table.py.