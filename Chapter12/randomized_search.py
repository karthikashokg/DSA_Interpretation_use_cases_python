
def partition(unsorted_array, first_index, last_index):
    # Choose the pivot element (first element in the array)
    pivot = unsorted_array[first_index]
    pivot_index = first_index
    index_of_last_element = last_index

    # Initialize pointers for elements greater and less than the pivot
    less_than_pivot_index = index_of_last_element
    greater_than_pivot_index = first_index + 1

    while True:
        # Move the greater_than_pivot_index to the right as long as elements are less than the pivot
        while unsorted_array[greater_than_pivot_index] < pivot and greater_than_pivot_index < last_index:
            greater_than_pivot_index += 1
        # Move the less_than_pivot_index to the left as long as elements are greater than the pivot
        while unsorted_array[less_than_pivot_index] > pivot and less_than_pivot_index >= first_index:
            less_than_pivot_index -= 1

        # If pointers have not crossed, swap the elements
        if greater_than_pivot_index < less_than_pivot_index:
            temp = unsorted_array[greater_than_pivot_index]
            unsorted_array[greater_than_pivot_index] = unsorted_array[less_than_pivot_index]
            unsorted_array[less_than_pivot_index] = temp
        else:
            break

    # Place the pivot element in its correct position
    unsorted_array[pivot_index] = unsorted_array[less_than_pivot_index]
    unsorted_array[less_than_pivot_index] = pivot

    # Return the index of the pivot element
    return less_than_pivot_index

def quick_select(array_list, start, end, k):
    # Partition the array and get the pivot index
    split = partition(array_list, start, end)
    # If the pivot index is the k-th position, return the element
    if split == k:
        return array_list[split]
    # If the pivot index is less than k, search in the right subarray
    elif split < k:
        return quick_select(array_list, split + 1, end, k)
    # If the pivot index is greater than k, search in the left subarray
    else:
        return quick_select(array_list, start, split - 1, k)

list1 = [3, 1, 10, 4, 6, 5]

print("The 2nd smallest element is", quick_select(list1, 0, 5, 1))
print("The 3rd smallest element is", quick_select(list1, 0, 5, 2))

stored = [3, 1, 10, 4, 6, 5]
print(stored)
print(quick_select(stored, 0, 5, 0))
stored = [3, 1, 10, 4, 6, 5]
print(quick_select(stored, 0, 5, 1))
stored = [3, 1, 10, 4, 6, 5]
print(quick_select(stored, 0, 5, 2))
stored = [3, 1, 10, 4, 6, 5]
print(quick_select(stored, 0, 5, 3))
stored = [3, 1, 10, 4, 6, 5]
print(quick_select(stored, 0, 5, 4))
stored = [3, 1, 10, 4, 6, 5]
print(quick_select(stored, 0, 5, 5))
# ```

# ### Time and Space Complexities

# - **Partition Function**:
#   - **Time Complexity**: \(O(n)\), where \(n\) is the number of elements in the array. This is because each element is compared once.
#   - **Space Complexity**: \(O(1)\), as it uses a constant amount of extra space.

# - **Quick Select Function**:
#   - **Time Complexity**: On average, \(O(n)\). In the worst case (when the pivot is always the smallest or largest element), it can degrade to \(O(n^2)\).
#   - **Space Complexity**: \(O(1)\), as it uses a constant amount of extra space.

# ### Visual Interpretation

# Imagine you have an array of numbers, and you want to find the k-th smallest element. Here's a step-by-step visual explanation:

# 1. **Initial Array**: `[3, 1, 10, 4, 6, 5]`
# 2. **Choose Pivot**: The first element, `3`, is chosen as the pivot.
# 3. **Partitioning**:
#    - Move elements less than `3` to the left and elements greater than `3` to the right.
#    - After partitioning, the array might look like this: `[1, 3, 10, 4, 6, 5]`.
# 4. **Pivot Position**: The pivot `3` is now in its correct position.
# 5. **Recursive Search**:
#    - If the pivot's position is the k-th position, return it.
#    - If not, recursively apply the same process to the left or right subarray.

# This process continues until the k-th smallest element is found.

# Would you like a visual diagram or any further explanation on any part of the code?

# Source: Conversation with Copilot, 9/1/2024
# (1) github.com. https://github.com/PacktPublishing/Hands-On-Data-Structures-and-Algorithms-with-Python-Second-Edition/tree/e3900012620ee5d8c17c8d43163b80179bd2cac4/Chapter11%2Frandomized_search.py.
# (2) github.com. https://github.com/kc0836/PythonDataStructures/tree/fc3805ba416b4cdcff96ceb05069e3d67561ac1b/Chapter11%2Frandomized_search.py.

###############use               case               ############################
# ### Step-by-Step Explanation with Visuals

# 1. **Initial Array**: `[3, 1, 10, 4, 6, 5]`
#    - **Pivot**: `3` (first element)
#    - **Goal**: Partition the array around the pivot.

# 2. **Partitioning**:
#    - **Initial State**:
#      ```
#      [3, 1, 10, 4, 6, 5]
#       ^
#      ```
#    - **Move `greater_than_pivot_index`**:
#      ```
#      [3, 1, 10, 4, 6, 5]
#       ^  ^
#      ```
#      - `1` is less than `3`, so move `greater_than_pivot_index` to the next element.
#      ```
#      [3, 1, 10, 4, 6, 5]
#       ^     ^
#      ```
#      - `10` is greater than `3`, stop here.

#    - **Move `less_than_pivot_index`**:
#      ```
#      [3, 1, 10, 4, 6, 5]
#       ^     ^        ^
#      ```
#      - `5` is greater than `3`, move `less_than_pivot_index` to the previous element.
#      ```
#      [3, 1, 10, 4, 6, 5]
#       ^     ^     ^
#      ```
#      - `6` is greater than `3`, move `less_than_pivot_index` to the previous element.
#      ```
#      [3, 1, 10, 4, 6, 5]
#       ^     ^  ^
#      ```
#      - `4` is greater than `3`, move `less_than_pivot_index` to the previous element.
#      ```
#      [3, 1, 10, 4, 6, 5]
#       ^     ^
#      ```

#    - **Swap Elements**:
#      ```
#      [3, 1, 5, 4, 6, 10]
#       ^     ^  ^
#      ```
#      - Swap `10` and `5`.

#    - **Continue Partitioning**:
#      ```
#      [3, 1, 5, 4, 6, 10]
#       ^        ^  ^
#      ```
#      - `5` is greater than `3`, stop here.
#      ```
#      [3, 1, 5, 4, 6, 10]
#       ^        ^
#      ```
#      - `4` is greater than `3`, stop here.

#    - **Final Swap**:
#      ```
#      [1, 3, 5, 4, 6, 10]
#          ^
#      ```
#      - Swap `3` with `1`.

# 3. **Pivot Position**:
#    - The pivot `3` is now in its correct position.
#    - Array after partitioning: `[1, 3, 5, 4, 6, 10]`
#    - Pivot index: `1`

# 4. **Recursive Search**:
#    - Since the pivot index `1` is equal to `k=1`, we have found the 2nd smallest element.

# ### Final Result
# - The 2nd smallest element in the array `[3, 1, 10, 4, 6, 5]` is `3`.

# Would you like any further details or another example?