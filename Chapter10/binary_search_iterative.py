
def binary_search_iterative(ordered_list, term):  
    size_of_list = len(ordered_list) - 1  # Get the index of the last element
    index_of_first_element = 0  # Initialize the index of the first element
    index_of_last_element = size_of_list  # Initialize the index of the last element

    while index_of_first_element <= index_of_last_element:  
        mid_point = (index_of_first_element + index_of_last_element) // 2  # Calculate the mid-point index
        if ordered_list[mid_point] == term:  # If the mid-point element is the search term
            return mid_point  # Return the index of the mid-point element
        if term > ordered_list[mid_point]:  # If the search term is greater than the mid-point element
            index_of_first_element = mid_point + 1  # Move the first index to mid-point + 1
        else:  # If the search term is less than the mid-point element
            index_of_last_element = mid_point - 1  # Move the last index to mid-point - 1

    if index_of_first_element > index_of_last_element:  
        return None  # Return None if the element is not found

# Example usage
store = [1, 4, 5, 12, 43, 54, 60, 77]
a = binary_search_iterative(store, 2)
print("Index position of value 2 is", a)  # Output: None

print(binary_search_iterative(store, 7))  # Output: None

print(binary_search_iterative(store, 60))  # Output: 6

list1 = [10, 30, 100, 120, 500]
search_term = 10
index_position1 = binary_search_iterative(list1, search_term)
if index_position1 is None:
    print("The data item {} is not found".format(search_term))
else:
    print("The data item {} is found at position {}".format(search_term, index_position1))  # Output: The data item 10 is found at position 0

list2 = ['book', 'data', 'packt', 'structure']
search_term2 = 'structure'
index_position2 = binary_search_iterative(list2, search_term2)
if index_position2 is None:
    print("The data item {} is not found".format(search_term2))
else:
    print("The data item {} is found at position {}".format(search_term2, index_position2))  # Output: The data item structure is found at position 3


#################################################

# ### Time and Space Complexities

# - **Time Complexity:** O(log n), where n is the number of elements in the list. This is because the list is divided in half at each step.
# - **Space Complexity:** O(1), as the algorithm uses a constant amount of extra space.

# ### Visual Representation

# 1. **Initial List:**
#    ```
#    [1, 4, 5, 12, 43, 54, 60, 77]
#    ```

# 2. **Search for 60:**
#    - Initial range: [1, 4, 5, 12, 43, 54, 60, 77]
#    - Mid-point: 43 (index 4)
#    - 60 > 43, so search in [54, 60, 77]
#    - New mid-point: 60 (index 6)
#    - 60 == 60, found at index 6

# 3. **Search for 2:**
#    - Initial range: [1, 4, 5, 12, 43, 54, 60, 77]
#    - Mid-point: 43 (index 4)
#    - 2 < 43, so search in [1, 4, 5, 12]
#    - New mid-point: 4 (index 1)
#    - 2 < 4, so search in [1]
#    - New mid-point: 1 (index 0)
#    - 2 > 1, no more elements to search, not found

# ### Use Cases and Explanation

# 1. **Efficient Search in Sorted Lists:**
#    - **Why:** Binary search is much faster than linear search for large sorted lists.
#    - **For What:** Useful in applications where quick search operations are needed, such as in databases and search engines.

# 2. **Finding Elements in Ordered Data:**
#    - **Why:** Binary search leverages the order of elements to reduce the search space.
#    - **For What:** Suitable for scenarios where data is naturally ordered, such as in dictionaries and phone books.

# 3. **Algorithm Optimization:**
#    - **Why:** Binary search is a fundamental algorithm that can be used to optimize other algorithms.
#    - **For What:** Useful in various algorithmic problems, such as finding the square root of a number or solving optimization problems.

# 4. **Real-Time Systems:**
#    - **Why:** Binary search provides predictable and fast search times.
#    - **For What:** Suitable for real-time systems where quick response times are critical, such as in embedded systems and robotics.

# ### Summary

# Binary search is a powerful algorithm for efficiently finding elements in sorted lists. It has a logarithmic time complexity, making it much faster than linear search for large datasets. It is widely used in various applications, including databases, search engines, and real-time systems.

# If you have any more questions or need further clarification, feel free to ask!