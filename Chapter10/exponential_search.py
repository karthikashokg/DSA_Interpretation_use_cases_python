
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

def exponential_search(A, search_value): 
    if A[0] == search_value:  # Check if the search value is at the first position
        return 0     
    index = 1 
    while index < len(A) and A[index] < search_value:  # Exponentially increase the index
        index *= 2        
    return binary_search_recursive(A, index // 2, min(index, len(A) - 1), search_value)  # Perform binary search in the found range

# Example usage
print(exponential_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 34, 40], 34))  # Output: 12
# ```

# ### Time and Space Complexities

# - **Exponential Search:**
#   - **Time Complexity:** O(log i) + O(log n) = O(log n), where i is the position of the search value and n is the number of elements in the list.
#   - **Space Complexity:** O(log n), due to the recursive call stack of binary search.

# - **Binary Search (Recursive):**
#   - **Time Complexity:** O(log n), where n is the number of elements in the list.
#   - **Space Complexity:** O(log n), due to the recursive call stack.

# ### Visual Representation

# 1. **Initial List:**
#    ```
#    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 34, 40]
#    ```

# 2. **Exponential Search for 34:**
#    - Initial check: 1 (index 0)
#    - Exponentially increase index: 2 (index 1), 4 (index 2), 8 (index 3), 16 (index 4), 32 (index 8), 64 (index 16)
#    - Found range: [8, 16]

# 3. **Binary Search in Range [8, 16]:**
#    - Initial range: [8, 16]
#    - Mid-point: 12 (index 12)
#    - 34 == 34, found at index 12

# ### Use Cases and Explanation

# 1. **Efficient Search in Large Sorted Lists:**
#    - **Why:** Exponential search is faster than linear search for large sorted lists.
#    - **For What:** Useful in applications where quick search operations are needed, such as in databases and search engines.

# 2. **Finding Elements in Ordered Data:**
#    - **Why:** Exponential search leverages the order of elements to reduce the search space.
#    - **For What:** Suitable for scenarios where data is naturally ordered, such as in dictionaries and phone books.

# 3. **Algorithm Optimization:**
#    - **Why:** Exponential search is a fundamental algorithm that can be used to optimize other algorithms.
#    - **For What:** Useful in various algorithmic problems, such as finding the square root of a number or solving optimization problems.

# 4. **Real-Time Systems:**
#    - **Why:** Exponential search provides predictable and fast search times.
#    - **For What:** Suitable for real-time systems where quick response times are critical, such as in embedded systems and robotics.

# ### Summary

# Exponential search is a powerful algorithm for efficiently finding elements in large sorted lists. It combines the benefits of exponential growth and binary search, making it much faster than linear search for large datasets. It is widely used in various applications, including databases, search engines, and real-time systems.

# If you have any more questions or need further clarification, feel free to ask!