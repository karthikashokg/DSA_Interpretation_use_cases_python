
def partition(unsorted_array, first_index, last_index):
    # If the sublist has only one element, return its index
    if first_index == last_index:
        return first_index
    else:
        # Find the median of medians for the sublist
        nearest_median = median_of_medians(unsorted_array[first_index:last_index])

    # Get the index of the nearest median in the sublist
    index_of_nearest_median = get_index_of_nearest_median(unsorted_array, first_index, last_index, nearest_median)
    # Swap the first element with the nearest median
    swap(unsorted_array, first_index, index_of_nearest_median)

    # Set the pivot to the first element
    pivot = unsorted_array[first_index]
    pivot_index = first_index
    index_of_last_element = last_index
    less_than_pivot_index = index_of_last_element
    greater_than_pivot_index = first_index + 1

    # This while loop is used to correctly place the pivot element at its correct position
    while 1:
        # Move the greater_than_pivot_index to the right as long as elements are less than the pivot
        while unsorted_array[greater_than_pivot_index] < pivot and greater_than_pivot_index < last_index:
            greater_than_pivot_index += 1
        # Move the less_than_pivot_index to the left as long as elements are greater than the pivot
        while unsorted_array[less_than_pivot_index] > pivot and less_than_pivot_index >= first_index:
            less_than_pivot_index -= 1

        # If the indices have not crossed, swap the elements
        if greater_than_pivot_index < less_than_pivot_index:
            temp = unsorted_array[greater_than_pivot_index]
            unsorted_array[greater_than_pivot_index] = unsorted_array[less_than_pivot_index]
            unsorted_array[less_than_pivot_index] = temp
        else:
            break

    # Place the pivot element at its correct position
    unsorted_array[pivot_index] = unsorted_array[less_than_pivot_index]
    unsorted_array[less_than_pivot_index] = pivot
    return less_than_pivot_index

def median_of_medians(elems):
    # Divide the list into sublists of 5 elements each
    sublists = [elems[j:j+5] for j in range(0, len(elems), 5)]
    medians = []
    # Find the median of each sublist
    for sublist in sublists:
        medians.append(sorted(sublist)[int(len(sublist)/2)])

    # If there are 5 or fewer medians, return the median of the medians
    if len(medians) <= 5:
        return sorted(medians)[int(len(medians)/2)]
    else:
        # Recursively find the median of the medians
        return median_of_medians(medians)

def get_index_of_nearest_median(array_list, first, second, median):
    # If the sublist has only one element, return its index
    if first == second:
        return first
    else:
        # Find the index of the median in the sublist
        return first + array_list[first:second].index(median)

def swap(array_list, first, index_of_nearest_median):
    # Swap the elements at the given indices
    temp = array_list[first]
    array_list[first] = array_list[index_of_nearest_median]
    array_list[index_of_nearest_median] = temp

def deterministic_select(array_list, left, right, k):
    # Partition the list and get the pivot index
    split = partition(array_list, left, right)
    # If the pivot index is the desired index, return the element
    if split == k:
        return array_list[split]
    # If the pivot index is less than the desired index, search in the right sublist
    elif split < k:
        return deterministic_select(array_list, split + 1, right, k)
    # If the pivot index is greater than the desired index, search in the left sublist
    else:
        return deterministic_select(array_list, left, split - 1, k)

# Example usage
stored = [3, 1, 10, 4, 6, 5]
# Find the 3rd smallest element (index 2)
print(deterministic_select(stored, 0, 5, 2))


# ### Time and Space Complexity

# - **Time Complexity**: 
#   - Worst Case: \(O(n \log n)\) due to the partitioning and recursive calls.
#   - Average Case: \(O(n)\) because the median of medians helps in reducing the number of elements to be considered in each recursive call.

# - **Space Complexity**: 
#   - \(O(n)\) due to the additional space required for the sublists and medians.

# ### Visual Interpretation

# Here's a visual representation of how the deterministic select algorithm works on the list `[3, 1, 10, 4, 6, 5]` to find the 3rd smallest element (index 2):

# 1. **Initial List**: `[3, 1, 10, 4, 6, 5]`

# 2. **Step 1**: Partition the list around the median of medians.
#    - Find the median of medians.
#    - Swap the median with the first element.
#    - Partition the list around the pivot.
#    - List after partitioning: `[3, 1, 5, 4, 6, 10]`
#    - Pivot index: 2

# 3. **Step 2**: Check if the pivot index is equal to k.
#    - If yes, return the element at the pivot index.
#    - If no, recursively call the function on the appropriate sublist.

# ### Enhanced Visual Flow

# Here's a more detailed visual flow of the deterministic select process with arrows indicating swaps and index changes:

# ```plaintext
# Initial List: [3, 1, 10, 4, 6, 5]

# Step 1: Partition around median of medians
# [3, 1, 10, 4, 6, 5]
#  ↓
# [3, 1, 5, 4, 6, 10]
# Pivot index: 2

# Step 2: Check pivot index
# Pivot index (2) == k (2)
# Return element at pivot index: 5
# ```

# ### Use Case: Finding the k-th Smallest Element

# Imagine you have a list of student scores and you want to find the 3rd smallest score. Here is the list of scores: `[3, 1, 10, 4, 6, 5]`.

# We'll use the deterministic select algorithm to find the 3rd smallest score (index 2).

# 1. **Initial List**: `[3, 1, 10, 4, 6, 5]`
# 2. **Step 1**: Partition the list around the median of medians.
#    - List after partitioning: `[3, 1, 5, 4, 6, 10]`
#    - Pivot index: 2
# 3. **Step 2**: Check if the pivot index is equal to k.
#    - Pivot index (2) == k (2)
#    - Return element at pivot index: 5

# This example demonstrates how the deterministic select algorithm works in a real-world scenario, finding the k-th smallest element in a list. If you have any more questions or need further clarification, feel free to ask!

# Source: Conversation with Copilot, 9/1/2024
# (1) github.com. https://github.com/apachecn/apachecn-python-zh/tree/63de9c961cf62843fb4361128e2f7cc30c7457fa/trans%2Fhandson-dsal-py%2F11.md.
# (2) github.com. https://github.com/andrewssamuel/search-algorithms/tree/e096fb8f63abc4ace70fd52e08ca9c9db8bda8ca/deterministic_search.py.
# (3) github.com. https://github.com/ramchinta/Algorithms/tree/08c4b8d216a43ac8a2c0297d3083ba4b0a806e22/DeterministicSelect.py.