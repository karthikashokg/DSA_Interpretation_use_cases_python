
def binary_search_recursive(ordered_list, first_element_index, last_element_index, term):  
    if last_element_index < first_element_index:  # Base case: if the search range is invalid
        return None  # The term is not found
    else:  
        mid_point = first_element_index + ((last_element_index - first_element_index) // 2)  # Calculate the mid-point index
 
        if ordered_list[mid_point] > term:  # If the mid-point element is greater than the search term
            return binary_search_recursive(ordered_list, first_element_index, mid_point - 1, term)  # Search in the left half
        elif ordered_list[mid_point] < term:  # If the mid-point element is less than the search term
            return binary_search_recursive(ordered_list, mid_point + 1, last_element_index, term)  # Search in the right half
        else:  
            return mid_point  # The term is found at the mid-point index

# Example usage
list1 = [10, 30, 100, 120, 500]

search_term = 10
index_position1 = binary_search_recursive(list1, 0, len(list1) - 1, search_term)
if index_position1 is None:
    print("The data item {} is not found".format(search_term))
else:
    print("The data item {} is found at position {}".format(search_term, index_position1))  # Output: The data item 10 is found at position 0

list2 = ['book', 'data', 'packt', 'structure']

search_term2 = 'data'
index_position2 = binary_search_recursive(list2, 0, len(list2) - 1, search_term2)
if index_position2 is None:
    print("The data item {} is not found".format(search_term2))
else:
    print("The data item {} is found at position {}".format(search_term2, index_position2))  # Output: The data item data is found at position 1
# ```

# ### Time and Space Complexities

# - **Time Complexity:** O(log n), where n is the number of elements in the list. This is because the list is divided in half at each step.
# - **Space Complexity:** O(log n), due to the recursive call stack.

# ### Visual Representation

# 1. **Initial List:**
#    ```
#    [10, 30, 100, 120, 500]
#    ```

# 2. **Search for 10:**
#    - Initial range: [10, 30, 100, 120, 500]
#    - Mid-point: 100 (index 2)
#    - 10 < 100, so search in [10, 30]
#    - New mid-point: 10 (index 0)
#    - 10 == 10, found at index 0

# 3. **Search for 'data':**
#    - Initial range: ['book', 'data', 'packt', 'structure']
#    - Mid-point: 'packt' (index 2)
#    - 'data' < 'packt', so search in ['book', 'data']
#    - New mid-point: 'data' (index 1)
#    - 'data' == 'data', found at index 1

# ### Use Cases and Explanation

# 1. **Efficient Search in Sorted Lists:**
#    - **Why:** Recursive binary search is much faster than linear search for large sorted lists.
#    - **For What:** Useful in applications where quick search operations are needed, such as in databases and search engines.

# 2. **Finding Elements in Ordered Data:**
#    - **Why:** Recursive binary search leverages the order of elements to reduce the search space.
#    - **For What:** Suitable for scenarios where data is naturally ordered, such as in dictionaries and phone books.

# 3. **Algorithm Optimization:**
#    - **Why:** Recursive binary search is a fundamental algorithm that can be used to optimize other algorithms.
#    - **For What:** Useful in various algorithmic problems, such as finding the square root of a number or solving optimization problems.

# 4. **Real-Time Systems:**
#    - **Why:** Recursive binary search provides predictable and fast search times.
#    - **For What:** Suitable for real-time systems where quick response times are critical, such as in embedded systems and robotics.

# ### Summary

# Recursive binary search is a powerful algorithm for efficiently finding elements in sorted lists. It has a logarithmic time complexity, making it much faster than linear search for large datasets. It is widely used in various applications, including databases, search engines, and real-time systems.

# If you have any more questions or need further clarification, feel free to ask!