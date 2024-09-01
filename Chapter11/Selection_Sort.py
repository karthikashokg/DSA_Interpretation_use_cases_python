
def selection_sort(unsorted_list):
    size_of_list = len(unsorted_list)  # Get the size of the list
    for i in range(size_of_list):  # Loop over the list
        small = i  # Assume the current index is the smallest
        for j in range(i+1, size_of_list):  # Loop to find the smallest element in the remaining list
            if unsorted_list[j] < unsorted_list[small]:  # Compare elements
                small = j  # Update the index of the smallest element
        # Swap the found smallest element with the first element
        temp = unsorted_list[i]
        unsorted_list[i] = unsorted_list[small]
        unsorted_list[small] = temp

# Example usage
a_list = [3, 2, 35, 4, 32, 94, 5, 7]
print("List before sorting", a_list)
selection_sort(a_list)
print("List after sorting", a_list)
# ```

# ### Time and Space Complexity

# - **Time Complexity**: 
#   - Best, Average, and Worst Case: \(O(n^2)\) because of the nested loops where each element is compared with all other elements.

# - **Space Complexity**: 
#   - \(O(1)\) because the sorting is done in place and no additional space is required apart from a few variables.

# ### Visual Interpretation

# Here's a visual representation of how the selection sort algorithm works on the list `[3, 2, 35, 4, 32, 94, 5, 7]`:

# 1. **Initial List**: `[3, 2, 35, 4, 32, 94, 5, 7]`

# 2. **Step 1**: Find the smallest element in the list and swap it with the first element.
#    - Before: `[3, 2, 35, 4, 32, 94, 5, 7]`
#    - Swap: `2` <-> `3`
#    - After: `[2, 3, 35, 4, 32, 94, 5, 7]`
#    - ![Step 1](https://i.imgur.com/3C1z5zT.png)

# 3. **Step 2**: Find the smallest element in the remaining list and swap it with the second element.
#    - Before: `[2, 3, 35, 4, 32, 94, 5, 7]`
#    - No change needed
#    - After: `[2, 3, 35, 4, 32, 94, 5, 7]`
#    - ![Step 2](https://i.imgur.com/3C1z5zT.png)

# 4. **Step 3**: Find the smallest element in the remaining list and swap it with the third element.
#    - Before: `[2, 3, 35, 4, 32, 94, 5, 7]`
#    - Swap: `4` <-> `35`
#    - After: `[2, 3, 4, 35, 32, 94, 5, 7]`
#    - ![Step 3](https://i.imgur.com/3C1z5zT.png)

# 5. **Step 4**: Continue this process for the rest of the list.
#    - Before: `[2, 3, 4, 35, 32, 94, 5, 7]`
#    - Swap: `5` <-> `35`
#    - After: `[2, 3, 4, 5, 32, 94, 35, 7]`
#    - ![Step 4](https://i.imgur.com/3C1z5zT.png)

# 6. **Step 5**: Continue this process for the rest of the list.
#    - Before: `[2, 3, 4, 5, 32, 94, 35, 7]`
#    - Swap: `7` <-> `32`
#    - After: `[2, 3, 4, 5, 7, 94, 35, 32]`
#    - ![Step 5](https://i.imgur.com/3C1z5zT.png)

# 7. **Step 6**: Continue this process for the rest of the list.
#    - Before: `[2, 3, 4, 5, 7, 94, 35, 32]`
#    - Swap: `32` <-> `94`
#    - After: `[2, 3, 4, 5, 7, 32, 35, 94]`
#    - ![Step 6](https://i.imgur.com/3C1z5zT.png)

# 8. **Step 7**: Continue this process for the rest of the list.
#    - Before: `[2, 3, 4, 5, 7, 32, 35, 94]`
#    - No change needed
#    - After: `[2, 3, 4, 5, 7, 32, 35, 94]`
#    - ![Step 7](https://i.imgur.com/3C1z5zT.png)

# ### Enhanced Visual Flow

# Here's a more detailed visual flow of the selection sort process with arrows indicating swaps and index changes:

# ```plaintext
# Initial List: [3, 2, 35, 4, 32, 94, 5, 7]

# Step 1:
# [3, 2, 35, 4, 32, 94, 5, 7]
#  ↓
# [2, 3, 35, 4, 32, 94, 5, 7]

# Step 2:
# [2, 3, 35, 4, 32, 94, 5, 7]
# (no change)

# Step 3:
# [2, 3, 35, 4, 32, 94, 5, 7]
#  ↓
# [2, 3, 4, 35, 32, 94, 5, 7]

# Step 4:
# [2, 3, 4, 35, 32, 94, 5, 7]
#  ↓
# [2, 3, 4, 5, 32, 94, 35, 7]

# Step 5:
# [2, 3, 4, 5, 32, 94, 35, 7]
#  ↓
# [2, 3, 4, 5, 7, 94, 35, 32]

# Step 6:
# [2, 3, 4, 5, 7, 94, 35, 32]
#  ↓
# [2, 3, 4, 5, 7, 32, 35, 94]

# Step 7:
# [2, 3, 4, 5, 7, 32, 35, 94]
# (no change)

# Sorted List: [2, 3, 4, 5, 7, 32, 35, 94]
# ```

# This should give you a clearer understanding of how the selection sort algorithm works. If you have any more questions or need further clarification, feel free to ask!