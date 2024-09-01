class HashItem:
    def __init__(self, key, value):
        self.key = key  # Initialize the key
        self.value = value  # Initialize the value

class HashTable:
    def __init__(self):
        self.size = 256  # Initial size of the hash table
        self.slots = [None for i in range(self.size)]  # Initialize slots with None
        self.count = 0  # Initialize the count of elements
        self.MAXLOADFACTOR = 0.65  # Maximum load factor before resizing
        self.prime_num = 5  # Prime number used for double hashing

    def check_growth(self):
        loadfactor = self.count / self.size  # Calculate the current load factor
        if loadfactor > self.MAXLOADFACTOR:
            print("Load factor before growing the hash table", self.count / self.size)
            self.growth()
            print("Load factor after growing the hash table", self.count / self.size)

    def growth(self):
        # Time Complexity: O(n) - Rehashing all elements.
        # Space Complexity: O(n) - New slots array.
        New_Hash_Table = HashTable()
        New_Hash_Table.size = 2 * self.size  # Double the size of the hash table
        New_Hash_Table.slots = [None for i in range(New_Hash_Table.size)]

        for i in range(self.size):
            if self.slots[i] != None:
                New_Hash_Table.put(self.slots[i].key, self.slots[i].value)

        self.size = New_Hash_Table.size
        self.slots = New_Hash_Table.slots

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
        # Time Complexity: O(1) on average, O(n) in the worst case due to linear probing.
        # Space Complexity: O(1) - No additional space used.
        item = HashItem(key, value)
        h = self._hash(key)

        while self.slots[h] != None:
            if self.slots[h].key == key:
                break
            h = (h + 1) % self.size  # Linear probing
        if self.slots[h] == None:
            self.count += 1
        self.slots[h] = item
        self.check_growth()

    def get(self, key):
        # Time Complexity: O(1) on average, O(n) in the worst case due to linear probing.
        # Space Complexity: O(1) - No additional space used.
        h = self._hash(key)
        while self.slots[h] != None:
            if self.slots[h].key == key:
                return self.slots[h].value
            h = (h + 1) % self.size  # Linear probing
        return None

    def put_quadratic(self, key, value):
        # Time Complexity: O(1) on average, O(n) in the worst case due to quadratic probing.
        # Space Complexity: O(1) - No additional space used.
        item = HashItem(key, value)
        h = self._hash(key)
        j = 1
        while self.slots[h] != None:
            if self.slots[h].key == key:
                break
            h = (h + j * j) % self.size  # Quadratic probing
            j += 1
        if self.slots[h] == None:
            self.count += 1
        self.slots[h] = item
        self.check_growth()

    def get_quadratic(self, key):
        # Time Complexity: O(1) on average, O(n) in the worst case due to quadratic probing.
        # Space Complexity: O(1) - No additional space used.
        h = self._hash(key)
        j = 1
        while self.slots[h] != None:
            if self.slots[h].key == key:
                return self.slots[h].value
            h = (h + j * j) % self.size  # Quadratic probing
            j += 1
        return None

    def h2(self, key):
        # Time Complexity: O(k) - k is the length of the key.
        # Space Complexity: O(1) - Constant space for variables.
        mult = 1
        hv = 0
        for ch in key:
            hv += mult * ord(ch)  # Calculate secondary hash value
            mult += 1
        return hv

    def put_double_hashing(self, key, value):
        # Time Complexity: O(1) on average, O(n) in the worst case due to double hashing.
        # Space Complexity: O(1) - No additional space used.
        item = HashItem(key, value)
        h = self._hash(key)
        j = 1
        while self.slots[h] != None:
            if self.slots[h].key == key:
                break
            h = (h + j * (self.prime_num - (self.h2(key) % self.prime_num))) % self.size  # Double hashing
            j += 1
        if self.slots[h] == None:
            self.count += 1
        self.slots[h] = item
        self.check_growth()

    def get_double_hashing(self, key):
        # Time Complexity: O(1) on average, O(n) in the worst case due to double hashing.
        # Space Complexity: O(1) - No additional space used.
        h = self._hash(key)
        j = 1
        while self.slots[h] != None:
            if self.slots[h].key == key:
                return self.slots[h].value
            h = (h + j * (self.prime_num - (self.h2(key) % self.prime_num))) % self.size  # Double hashing
            j += 1
        return None

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, key):
        return self.get(key)

# Example usage
ht = HashTable()
ht.put_quadratic("good", "eggs")
ht.put_quadratic("ad", "packt")
ht.put_quadratic("ga", "books")
v = ht.get_quadratic("ga")
print(v)

ht = HashTable()
ht.put("good", "eggs")
ht.put("better", "ham")
ht.put("best", "spam")
ht.put("ad", "do not")
ht.put("ga", "collide")
ht.put("awd", "do not")
ht.put("add", "do not")
ht.check_growth()

for key in ("good", "better", "best", "worst", "ad", "ga"):
    v = ht.get(key)
    print(v)

ht = HashTable()
ht.put_double_hashing("good", "eggs")
ht.put_double_hashing("better", "spam")
ht.put_double_hashing("best", "cool")
ht.put_double_hashing("ad", "donot")
ht.put_double_hashing("ga", "collide")
ht.put_double_hashing("awd", "hello")
ht.put_double_hashing("addition", "ok")
for key in ("good", "better", "best", "worst", "ad", "ga"):
    v = ht.get_double_hashing(key)
    print(v)
print("The number of elements is: {}".format(ht.count))

ht = HashTable()
ht["good"] = "eggs"
ht["better"] = "ham"
ht["best"] = "spam"
ht["ad"] = "do not"
ht["ga"] = "collide"
ht["data"] = "value"

for key in ("good", "better", "best", "worst", "ad", "ga"):
    v = ht[key]
    print(v)

print("The number of elements is: {}".format(ht.count))


#################################################################################3


# ### 1. **Chaining**
# In chaining, each slot in the hash table points to a linked list (or another data structure) of entries that hash to the same index.

# - **How it works:**
#   - Each slot in the hash table contains a pointer to a linked list.
#   - When a collision occurs, the new entry is added to the linked list at the corresponding slot.
#   - To search for an entry, the hash table index is computed, and the linked list at that index is traversed.

# - **Advantages:**
#   - Simple to implement.
#   - The hash table can handle an unlimited number of collisions.

# - **Disadvantages:**
#   - Requires additional memory for pointers.
#   - Performance can degrade if many entries hash to the same index (long linked lists).

# ### 2. **Open Addressing**
# In open addressing, all elements are stored within the hash table itself. When a collision occurs, the algorithm searches for the next available slot according to a probing sequence.

# #### a. **Linear Probing**
# - **How it works:**
#   - If a collision occurs at index `i`, the algorithm checks the next slot `(i + 1) % size`, then `(i + 2) % size`, and so on, until an empty slot is found.
  
# - **Advantages:**
#   - Simple to implement.
#   - Good cache performance due to locality of reference.

# - **Disadvantages:**
#   - Clustering: Consecutive occupied slots can lead to longer search times.

# #### b. **Quadratic Probing**
# - **How it works:**
#   - If a collision occurs at index `i`, the algorithm checks the slots `(i + 1^2) % size`, `(i + 2^2) % size`, `(i + 3^2) % size`, and so on.
  
# - **Advantages:**
#   - Reduces clustering compared to linear probing.

# - **Disadvantages:**
#   - Secondary clustering: Entries that hash to the same initial index follow the same probing sequence.

# #### c. **Double Hashing**
# - **How it works:**
#   - Uses a second hash function to determine the step size for probing.
#   - If a collision occurs at index `i`, the algorithm checks the slots `(i + j * h2(key)) % size`, where `h2` is the second hash function and `j` is the probe number.
  
# - **Advantages:**
#   - Minimizes clustering.
#   - Provides a more uniform distribution of entries.

# - **Disadvantages:**
#   - More complex to implement.
#   - Requires careful selection of the second hash function to ensure good performance.

# ### Visual Representation

# #### Chaining
# ```
# Index 0: -> (key1, value1) -> (key2, value2)
# Index 1: -> (key3, value3)
# Index 2: -> (key4, value4) -> (key5, value5)
# ```

# #### Linear Probing
# ```
# Index 0: (key1, value1)
# Index 1: (key2, value2)
# Index 2: (key3, value3)
# Index 3: (key4, value4)
# Index 4: (key5, value5)
# ```

# #### Quadratic Probing
# ```
# Index 0: (key1, value1)
# Index 1: (key2, value2)
# Index 4: (key3, value3)
# Index 9: (key4, value4)
# Index 16: (key5, value5)
# ```

# #### Double Hashing
# ```
# Index 0: (key1, value1)
# Index 1: (key2, value2)
# Index 3: (key3, value3)
# Index 7: (key4, value4)
# Index 11: (key5, value5)
# ```

# ### Use Cases

# - **Chaining:** Suitable for applications where the hash table needs to handle a large number of entries and memory usage is not a primary concern.
# - **Linear Probing:** Good for scenarios where cache performance is critical, and the load factor is kept low to minimize clustering.
# - **Quadratic Probing:** Useful when a moderate level of clustering is acceptable, and the hash table needs to handle a moderate number of entries.
# - **Double Hashing:** Ideal for applications requiring a more uniform distribution of entries and minimal clustering, even at higher load factors.

# Each collision handling strategy has its own strengths and weaknesses, and the choice of strategy depends on the specific requirements and constraints of the application.

# If you have any more questions or need further clarification, feel free to ask!