
def search(unordered_list, term):
    for i, item in enumerate(unordered_list):  # Iterate over the list with index and item
        if term == unordered_list[i]:  # If the term is found
            return i  # Return the index
    return None  # Return None if the term is not found

# Example usage
list1 = [60, 1, 88, 10, 11, 600]

search_term = 10
index_position = search(list1, search_term)
print(index_position)  # Output: 3

list2 = ['packt', 'publish', 'data']
search_term2 = 'data'
index_position2 = search(list2, search_term2)
print(index_position2)  # Output: 2

if index_position is None:
    print("{} not found".format(search_term))
else:
    print("{} found at position {}".format(search_term, index_position))  # Output: 10 found at position 3

if index_position2 is None:
    print("{} not found".format(search_term2))
else:
    print("{} found at position {}".format(search_term2, index_position2))  # Output: data found at position 2
# ```

# ### Time and Space Complexities

# - **Time Complexity:** O(n), where n is the number of elements in the list. This is because the algorithm may need to check each element in the worst case.
# - **Space Complexity:** O(1), as the algorithm uses a constant amount of extra space.

# ### Visual Representation

# 1. **Initial List:**
#    ```
#    [60, 1, 88, 10, 11, 600]
#    ```

# 2. **Search for 10:**
#    - Check 60: 10 != 60, move to next element
#    - Check 1: 10 != 1, move to next element
#    - Check 88: 10 != 88, move to next element
#    - Check 10: 10 == 10, found at index 3

# 3. **Search for 'data':**
#    - Check 'packt': 'data' != 'packt', move to next element
#    - Check 'publish': 'data' != 'publish', move to next element
#    - Check 'data': 'data' == 'data', found at index 2

# ### Use Cases and Explanation

# 1. **Simple Search in Unordered Lists:**
#    - **Why:** Linear search is straightforward and easy to implement.
#    - **For What:** Useful for small lists where the overhead of more complex algorithms is unnecessary.

# 2. **Finding Elements in Unordered Data:**
#    - **Why:** Linear search can be used when the list is unordered, and no assumptions can be made about the order of elements.
#    - **For What:** Suitable for scenarios where data is randomly ordered, such as in unsorted arrays or lists.

# 3. **Algorithm Simplicity:**
#    - **Why:** Linear search does not require additional data structures or complex logic.
#    - **For What:** Useful in educational contexts to teach basic search algorithms and in simple applications where performance is not critical.

# 4. **Real-Time Systems:**
#    - **Why:** Linear search provides predictable and straightforward search times.
#    - **For What:** Suitable for real-time systems where quick implementation and simplicity are more important than performance, such as in embedded systems and simple data retrieval tasks.

# ### Summary

# Linear search is a simple and straightforward algorithm for finding elements in unordered lists. It has a linear time complexity, making it suitable for small lists or scenarios where simplicity is more important than performance. It is widely used in various applications, including small databases, educational contexts, and real-time systems.

# If you have any more questions or need further clarification, feel free to ask!