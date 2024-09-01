
def search_ordered(ordered_list, term):   
    print("Entering Linear Search") 
    ordered_list_size = len(ordered_list)  # Get the size of the ordered list
    for i in range(ordered_list_size):   
        if term == ordered_list[i]:  # If the term is found
            return i  # Return the index
        elif ordered_list[i] > term:  # If the current element is greater than the term
            return -1  # Return -1 indicating the term is not found
    return -1  # Return -1 if the term is not found after the loop

def jump_search(ordered_list, item): 
    import math
    print("Entering Jump Search") 
    list_size = len(ordered_list)  # Get the size of the ordered list
    block_size = int(math.sqrt(list_size))  # Calculate the block size for jumping
    i = 0  # Initialize the starting index
    while i != len(ordered_list) - 1 and ordered_list[i] <= item: 
        print("Block under consideration - {}".format(ordered_list[i: i + block_size])) 
        if i + block_size > len(ordered_list): 
            block_size = len(ordered_list) - i  # Adjust the block size if it exceeds the list size
            block_list = ordered_list[i: i + block_size] 
            j = search_ordered(block_list, item) 
            if j == -1: 
                print("Element not found") 
                return  
            return i + j  # Return the index if the item is found
        if ordered_list[i + block_size - 1] == item:            
            return i + block_size - 1  # Return the index if the item is found at the end of the block
        elif ordered_list[i + block_size - 1] > item:            
            block_array = ordered_list[i: i + block_size - 1] 
            j = search_ordered(block_array, item) 
            if j == -1: 
                print("Element not found") 
                return   
            return i + j  # Return the index if the item is found within the block
        i += block_size  # Move to the next block

# Example usage
print(jump_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 8))  # Output: 7
# ```

# ### Time and Space Complexities

# - **Jump Search:**
#   - **Time Complexity:** O(√n), where n is the number of elements in the list. This is because the algorithm jumps in blocks of size √n.
#   - **Space Complexity:** O(1), as the algorithm uses a constant amount of extra space.

# - **Linear Search (within blocks):**
#   - **Time Complexity:** O(√n) in the worst case, as it may need to search within a block of size √n.
#   - **Space Complexity:** O(1), as the algorithm uses a constant amount of extra space.

# ### Visual Representation

# 1. **Initial List:**
#    ```
#    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
#    ```

# 2. **Search for 8:**
#    - Initial block size: √11 ≈ 3
#    - Blocks:
#      - [1, 2, 3]
#      - [4, 5, 6]
#      - [7, 8, 9]
#    - Check block [1, 2, 3]: 8 > 3, move to next block
#    - Check block [4, 5, 6]: 8 > 6, move to next block
#    - Check block [7, 8, 9]: 8 is within this block
#    - Perform linear search within block [7, 8, 9]
#    - Found 8 at index 7

# ### Use Cases and Explanation

# 1. **Efficient Search in Large Sorted Lists:**
#    - **Why:** Jump search is faster than linear search for large sorted lists.
#    - **For What:** Useful in applications where quick search operations are needed, such as in databases and search engines.

# 2. **Finding Elements in Ordered Data:**
#    - **Why:** Jump search leverages the order of elements to reduce the search space.
#    - **For What:** Suitable for scenarios where data is naturally ordered, such as in dictionaries and phone books.

# 3. **Algorithm Optimization:**
#    - **Why:** Jump search is a fundamental algorithm that can be used to optimize other algorithms.
#    - **For What:** Useful in various algorithmic problems, such as finding the square root of a number or solving optimization problems.

# 4. **Real-Time Systems:**
#    - **Why:** Jump search provides predictable and fast search times.
#    - **For What:** Suitable for real-time systems where quick response times are critical, such as in embedded systems and robotics.

# ### Summary

# Jump search is a powerful algorithm for efficiently finding elements in large sorted lists. It combines the benefits of block jumping and linear search, making it much faster than linear search for large datasets. It is widely used in various applications, including databases, search engines, and real-time systems.

# If you have any more questions or need further clarification, feel free to ask!