
def binary_search(arr, start, end, key):
    while start <= end:  # Continue searching while the start index is less than or equal to the end index
        mid = start + (end - start) // 2  # Calculate the middle index to avoid overflow
        if arr[mid] == key:  # If the middle element is the key, return the index
            return mid  
        elif arr[mid] < key:  # If the middle element is less than the key, search in the right half
            start = mid + 1  
        else:  # If the middle element is greater than the key, search in the left half
            end = mid - 1  
    return -1  # If the key is not found, return -1

# Example usage
arr = [4, 6, 9, 13, 14, 18, 21, 24, 38] 
x = 13
result = binary_search(arr, 0, len(arr) - 1, x)  
print(result)  # Output: 3 (index of the key 13 in the array)
# ```

# ### Time and Space Complexities

# - **Time Complexity**: The time complexity of the binary search algorithm is \(O(\log n)\), where \(n\) is the number of elements in the array. This is because the search space is halved in each iteration.
# - **Space Complexity**: The space complexity is \(O(1)\) as the algorithm uses a constant amount of extra space.

# ### Interpretation

# The binary search algorithm is an efficient way to find the position of a target value within a sorted array. Here's a step-by-step interpretation:

# 1. **Initialization**:
#    - The function takes a sorted array `arr`, the starting index `start`, the ending index `end`, and the target value `key`.

# 2. **Calculate Middle Index**:
#    - The middle index `mid` is calculated to avoid overflow using the formula `mid = start + (end - start) // 2`.

# 3. **Comparison**:
#    - If the middle element `arr[mid]` is equal to the key, the function returns the middle index `mid`.
#    - If the middle element is less than the key, the search continues in the right half of the array by updating the `start` index to `mid + 1`.
#    - If the middle element is greater than the key, the search continues in the left half of the array by updating the `end` index to `mid - 1`.

# 4. **Repeat**:
#    - The process repeats until the `start` index is greater than the `end` index, indicating that the key is not present in the array.

# 5. **Return**:
#    - If the key is not found, the function returns `-1`.

# ### Example

# For the array `[4, 6, 9, 13, 14, 18, 21, 24, 38]` and the key `13`, the binary search algorithm works as follows:

# 1. **Initial State**:
#    - `start = 0`, `end = 8`
#    - `mid = 4` (element at index 4 is `14`)

# 2. **First Comparison**:
#    - `14` is greater than `13`, so search in the left half.
#    - Update `end = 3`

# 3. **Second Comparison**:
#    - `mid = 1` (element at index 1 is `6`)
#    - `6` is less than `13`, so search in the right half.
#    - Update `start = 2`

# 4. **Third Comparison**:
#    - `mid = 2` (element at index 2 is `9`)
#    - `9` is less than `13`, so search in the right half.
#    - Update `start = 3`

# 5. **Fourth Comparison**:
#    - `mid = 3` (element at index 3 is `13`)
#    - `13` is equal to `13`, so return `3`.

# The key `13` is found at index `3`.

# Would you like any further details or another example?