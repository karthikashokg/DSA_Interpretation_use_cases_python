
def nearest_mid(input_list, low_index, upper_index, search_value):
    # Calculate the mid-point using the interpolation formula
    mid = low_index + ((upper_index - low_index) / (input_list[upper_index] - input_list[low_index])) * (search_value - input_list[low_index])
    return int(mid)  # Return the mid-point as an integer

def interpolation_search(ordered_list, search_value):
    low_index = 0  # Initialize the low index
    upper_index = len(ordered_list) - 1  # Initialize the upper index
    while low_index <= upper_index:
        mid_point = nearest_mid(ordered_list, low_index, upper_index, search_value)  # Calculate the mid-point
        if mid_point > upper_index or mid_point < low_index:
            return None  # Return None if the mid-point is out of bounds
        if ordered_list[mid_point] == search_value:
            return mid_point  # Return the mid-point index if the search value is found
        if search_value > ordered_list[mid_point]:
            low_index = mid_point + 1  # Adjust the low index if the search value is greater
        else:
            upper_index = mid_point - 1  # Adjust the upper index if the search value is smaller
    if low_index > upper_index:
        return None  # Return None if the search value is not found

# Example usage
list1 = [44, 60, 75, 100, 120, 230, 250]
a = interpolation_search(list1, 120)
print("Index position of value 120 is", a)  # Output: Index position of value 120 is 4

print(nearest_mid(list1, 0, 6, 120))  # Output: 4
# ```

# ### Time and Space Complexities

# - **Time Complexity:** O(log log n) on average, where n is the number of elements in the list. This is because interpolation search narrows down the search range more quickly than binary search for uniformly distributed data.
# - **Space Complexity:** O(1), as the algorithm uses a constant amount of extra space.

# ### Visual Representation

# 1. **Initial List:**
#    ```
#    [44, 60, 75, 100, 120, 230, 250]
#    ```

# 2. **Search for 120:**
#    - Initial range: [44, 60, 75, 100, 120, 230, 250]
#    - Calculate mid-point using interpolation formula:
#      ```
#      mid = 0 + ((6 - 0) / (250 - 44)) * (120 - 44)
#          = 0 + (6 / 206) * 76
#          = 0 + 0.0291 * 76
#          = 2.2116 ≈ 2
#      ```
#    - Mid-point: 75 (index 2)
#    - 120 > 75, so adjust the low index to 3
#    - New range: [100, 120, 230, 250]
#    - Calculate mid-point using interpolation formula:
#      ```
#      mid = 3 + ((6 - 3) / (250 - 100)) * (120 - 100)
#          = 3 + (3 / 150) * 20
#          = 3 + 0.02 * 20
#          = 3 + 0.4
#          = 3.4 ≈ 3
#      ```
#    - Mid-point: 100 (index 3)
#    - 120 > 100, so adjust the low index to 4
#    - New range: [120, 230, 250]
#    - Calculate mid-point using interpolation formula:
#      ```
#      mid = 4 + ((6 - 4) / (250 - 120)) * (120 - 120)
#          = 4 + (2 / 130) * 0
#          = 4 + 0
#          = 4
#      ```
#    - Mid-point: 120 (index 4)
#    - 120 == 120, found at index 4

# ### Use Cases and Explanation

# 1. **Efficient Search in Uniformly Distributed Lists:**
#    - **Why:** Interpolation search is faster than binary search for uniformly distributed data.
#    - **For What:** Useful in applications where data is uniformly distributed, such as in databases and search engines.

# 2. **Finding Elements in Ordered Data:**
#    - **Why:** Interpolation search leverages the order and distribution of elements to reduce the search space.
#    - **For What:** Suitable for scenarios where data is naturally ordered and uniformly distributed, such as in dictionaries and phone books.

# 3. **Algorithm Optimization:**
#    - **Why:** Interpolation search is a fundamental algorithm that can be used to optimize other algorithms.
#    - **For What:** Useful in various algorithmic problems, such as finding the square root of a number or solving optimization problems.

# 4. **Real-Time Systems:**
#    - **Why:** Interpolation search provides predictable and fast search times for uniformly distributed data.
#    - **For What:** Suitable for real-time systems where quick response times are critical, such as in embedded systems and robotics.

# ### Summary

# Interpolation search is a powerful algorithm for efficiently finding elements in uniformly distributed sorted lists. It has a logarithmic time complexity, making it much faster than binary search for large datasets with uniform distribution. It is widely used in various applications, including databases, search engines, and real-time systems.

# If you have any more questions or need further clarification, feel free to ask!