
def Insertion_Sort(unsorted_list):
    # Loop over the list starting from the second element
    for index in range(1, len(unsorted_list)):
        search_index = index  # Initialize search_index to the current index
        insert_value = unsorted_list[index]  # Store the value to be inserted
        # Shift elements of the sorted segment to the right to make space for insert_value
        while search_index > 0 and unsorted_list[search_index-1] > insert_value:
            unsorted_list[search_index] = unsorted_list[search_index-1]
            search_index -= 1  # Move to the next position on the left
        # Insert the value at the correct position
        unsorted_list[search_index] = insert_value
    return unsorted_list

def Merge(first_sublist, second_sublist):
    i = j = 0
    merged_list = []
    # Merge the two sublists into a single sorted list
    while i < len(first_sublist) and j < len(second_sublist):
        if first_sublist[i] < second_sublist[j]:
            merged_list.append(first_sublist[i])
            i += 1
        else:
            merged_list.append(second_sublist[j])
            j += 1
    # Append any remaining elements from the first sublist
    while i < len(first_sublist):
        merged_list.append(first_sublist[i])
        i += 1
    # Append any remaining elements from the second sublist
    while j < len(second_sublist):
        merged_list.append(second_sublist[j])
        j += 1
    return merged_list

def Tim_Sort(arr, run):
    # Sort individual sublists of size 'run' using insertion sort
    for x in range(0, len(arr), run):
        arr[x : x + run] = Insertion_Sort(arr[x : x + run])
    runSize = run
    
    # Merge sorted sublists to form larger sorted sublists
    while runSize < len(arr):
        for x in range(0, len(arr), 2 * runSize):
            arr[x : x + 2 * runSize] = Merge(arr[x : x + runSize], arr[x + runSize: x + 2 * runSize])
        runSize = runSize * 2

# Example usage
arr = [4, 6, 3, 9, 2, 8, 7, 5]
run = 2

Tim_Sort(arr, run)
print(arr)
# ```

# ### Time and Space Complexity

# - **Time Complexity**: 
#   - Best, Average, and Worst Case: \(O(n \log n)\) due to the merge process and the use of insertion sort on small sublists.

# - **Space Complexity**: 
#   - \(O(n)\) because of the additional space required for merging sublists.

# ### Visual Interpretation

# Here's a visual representation of how the Tim Sort algorithm works on the list `[4, 6, 3, 9, 2, 8, 7, 5]` with a run size of 2:

# 1. **Initial List**: `[4, 6, 3, 9, 2, 8, 7, 5]`

# 2. **Step 1**: Sort sublists of size 2 using insertion sort.
#    - Before: `[4, 6, 3, 9, 2, 8, 7, 5]`
#    - After: `[4, 6, 3, 9, 2, 8, 7, 5]` (no change for first sublist)
#    - After: `[4, 6, 3, 9, 2, 8, 7, 5]` (no change for second sublist)
#    - After: `[4, 6, 3, 9, 2, 8, 7, 5]` (no change for third sublist)
#    - After: `[4, 6, 3, 9, 2, 8, 5, 7]` (swap 5 and 7 in fourth sublist)

# 3. **Step 2**: Merge sorted sublists to form larger sorted sublists.
#    - Before: `[4, 6, 3, 9, 2, 8, 5, 7]`
#    - Merge: `[4, 6]` and `[3, 9]` -> `[3, 4, 6, 9]`
#    - Merge: `[2, 8]` and `[5, 7]` -> `[2, 5, 7, 8]`
#    - After: `[3, 4, 6, 9, 2, 5, 7, 8]`

# 4. **Step 3**: Merge the larger sorted sublists to form the final sorted list.
#    - Before: `[3, 4, 6, 9, 2, 5, 7, 8]`
#    - Merge: `[3, 4, 6, 9]` and `[2, 5, 7, 8]` -> `[2, 3, 4, 5, 6, 7, 8, 9]`
#    - After: `[2, 3, 4, 5, 6, 7, 8, 9]`

# ### Enhanced Visual Flow

# Here's a more detailed visual flow of the Tim Sort process with arrows indicating swaps and index changes:

# ```plaintext
# Initial List: [4, 6, 3, 9, 2, 8, 7, 5]

# Step 1: Sort sublists of size 2
# [4, 6, 3, 9, 2, 8, 7, 5]
# (no change for first sublist)
# [4, 6, 3, 9, 2, 8, 7, 5]
# (no change for second sublist)
# [4, 6, 3, 9, 2, 8, 7, 5]
# (no change for third sublist)
# [4, 6, 3, 9, 2, 8, 5, 7]
#  ↓
# [4, 6, 3, 9, 2, 8, 5, 7]

# Step 2: Merge sorted sublists
# [4, 6, 3, 9, 2, 8, 5, 7]
#  ↓
# [3, 4, 6, 9, 2, 8, 5, 7]
#  ↓
# [3, 4, 6, 9, 2, 5, 7, 8]

# Step 3: Merge larger sorted sublists
# [3, 4, 6, 9, 2, 5, 7, 8]
#  ↓
# [2, 3, 4, 5, 6, 7, 8, 9]

# Sorted List: [2, 3, 4, 5, 6, 7, 8, 9]
# ```

# This example demonstrates how the Tim Sort algorithm works in a real-world scenario, sorting a list of numbers. If you have any more questions or need further clarification, feel free to ask!