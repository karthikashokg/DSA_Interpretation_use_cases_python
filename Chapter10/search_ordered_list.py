
def search_ordered(ordered_list, term):
    ordered_list_size = len(ordered_list)  # Get the size of the ordered list
    for i in range(ordered_list_size):
        if term == ordered_list[i]:  # If the term is found
            return i  # Return the index
        elif ordered_list[i] > term:  # If the current element is greater than the term
            return None  # Return None indicating the term is not found
    return None  # Return None if the term is not found after the loop

# Example usage
list1 = [2, 3, 4, 6, 7]

search_term = 6
index_position1 = search_ordered(list1, search_term)

if index_position1 is None:
    print("{} not found".format(search_term))
else:
    print("{} found at position {}".format(search_term, index_position1))  # Output: 6 found at position 3

list2 = ['book', 'data', 'packt', 'structure']

search_term2 = 'structure'
index_position2 = search_ordered(list2, search_term2)
if index_position2 is None:
    print("{} not found".format(search_term2))
else:
    print("{} found at position {}".format(search_term2, index_position2))  # Output: structure found at position 3
# ```

# ### Time and Space Complexities

# - **Time Complexity:** O(n), where n is the number of elements in the list. This is because the algorithm may need to check each element in the worst case.
# - **Space Complexity:** O(1), as the algorithm uses a constant amount of extra space.

# ### Visual Representation

# 1. **Initial List:**
#    ```
#    [2, 3, 4, 6, 7]
#    ```

# 2. **Search for 6:**
#    - Check 2: 6 > 2, move to next element
#    - Check 3: 6 > 3, move to next element
#    - Check 4: 6 > 4, move to next element
#    - Check 6: 6 == 6, found at index 3

# 3. **Search for 'structure':**
#    - Check 'book': 'structure' > 'book', move to next element
#    - Check 'data': 'structure' > 'data', move to next element
#    - Check 'packt': 'structure' > 'packt', move to next element
#    - Check 'structure': 'structure' == 'structure', found at index 3

# ### Use Cases and Explanation

# 1. **Simple Search in Small Lists:**
#    - **Why:** Linear search is straightforward and easy to implement.
#    - **For What:** Useful for small lists where the overhead of more complex algorithms is unnecessary.

# 2. **Finding Elements in Ordered Data:**
#    - **Why:** Linear search can be used when the list is ordered, and the search can terminate early if an element greater than the search term is found.
#    - **For What:** Suitable for scenarios where data is naturally ordered, such as in dictionaries and phone books.

# 3. **Algorithm Simplicity:**
#    - **Why:** Linear search does not require additional data structures or complex logic.
#    - **For What:** Useful in educational contexts to teach basic search algorithms and in simple applications where performance is not critical.

# 4. **Real-Time Systems:**
#    - **Why:** Linear search provides predictable and straightforward search times.
#    - **For What:** Suitable for real-time systems where quick implementation and simplicity are more important than performance, such as in embedded systems and simple data retrieval tasks.

# ### Summary

# Linear search is a simple and straightforward algorithm for finding elements in ordered lists. It has a linear time complexity, making it suitable for small lists or scenarios where simplicity is more important than performance. It is widely used in various applications, including small databases, educational contexts, and real-time systems.

# If you have any more questions or need further clarification, feel free to ask!