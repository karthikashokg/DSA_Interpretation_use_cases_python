
def merge_sort(unsorted_list):  
    if len(unsorted_list) == 1:  
        return unsorted_list  # Base case: if the list has only one element, return it
    
    mid_point = int(len(unsorted_list) / 2)  # Find the midpoint of the list
    first_half = unsorted_list[:mid_point]  # Divide the list into two halves
    second_half = unsorted_list[mid_point:]  
    
    half_a = merge_sort(first_half)  # Recursively sort the first half
    half_b = merge_sort(second_half)  # Recursively sort the second half
    
    return merge(half_a, half_b)  # Merge the two sorted halves

def merge(first_sublist, second_sublist):
    i = j = 0
    merged_list = []
    
    while i < len(first_sublist) and j < len(second_sublist):
        if first_sublist[i] < second_sublist[j]:
            merged_list.append(first_sublist[i])  # Append the smaller element to the merged list
            i += 1  
        else:
            merged_list.append(second_sublist[j])  
            j += 1
    
    while i < len(first_sublist):  # Append any remaining elements from the first sublist
        merged_list.append(first_sublist[i])  
        i += 1  
    
    while j < len(second_sublist):  # Append any remaining elements from the second sublist
        merged_list.append(second_sublist[j])  
        j += 1
    
    return merged_list  # Return the merged list

# Example usage
a = [11, 12, 7, 41, 61, 13, 16, 14]
print(merge_sort(a))  # Output: [7, 11, 12, 13, 14, 16, 41, 61]
# ```

# ### Time and Space Complexities

# - **Time Complexity**: The time complexity of merge sort is \(O(n \log n)\), where \(n\) is the number of elements in the list. This is because the list is repeatedly divided into halves (logarithmic splits) and each element is processed (linear merges).
# - **Space Complexity**: The space complexity is \(O(n)\) due to the additional space required for the temporary lists created during the merging process.

# ### Interpretation

# Merge sort is a divide-and-conquer algorithm that works by recursively dividing the list into smaller sublists, sorting those sublists, and then merging them back together. Here's a step-by-step interpretation:

# 1. **Divide**:
#    - The list is divided into two halves until each sublist contains only one element (base case).

# 2. **Conquer**:
#    - Each sublist is sorted recursively using the same merge sort algorithm.

# 3. **Combine**:
#    - The sorted sublists are merged back together to form a single sorted list.

# ### Example

# For the list `[11, 12, 7, 41, 61, 13, 16, 14]`, the merge sort algorithm works as follows:

# 1. **Initial List**:
#    ```
#    [11, 12, 7, 41, 61, 13, 16, 14]
#    ```

# 2. **Divide**:
#    - Split into two halves:
#      ```
#      [11, 12, 7, 41] and [61, 13, 16, 14]
#      ```

# 3. **Recursive Sort**:
#    - Sort each half:
#      ```
#      [11, 12, 7, 41] -> [7, 11, 12, 41]
#      [61, 13, 16, 14] -> [13, 14, 16, 61]
#      ```

# 4. **Merge**:
#    - Merge the sorted halves:
#      ```
#      [7, 11, 12, 41] and [13, 14, 16, 61] -> [7, 11, 12, 13, 14, 16, 41, 61]
#      ```

# The final sorted list is `[7, 11, 12, 13, 14, 16, 41, 61]`.

# Would you like any further details or another example?