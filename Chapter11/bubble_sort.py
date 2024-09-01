
unordered_list = [5, 2]

temp = unordered_list[0]  # Store the first element in a temporary variable
unordered_list[0] = unordered_list[1]  # Assign the second element to the first position
unordered_list[1] = temp  # Assign the temporary variable (first element) to the second position

print(unordered_list)  # Output: [2, 5]
# ```
# - **Complexity**: O(1) for each assignment operation.
# - **Use Case**: This is a basic example of swapping two elements in a list.

#### Bubble Sort Function

def bubble_sort(unordered_list):
    iteration_number = len(unordered_list) - 1  # Calculate the number of iterations needed
    for i in range(iteration_number, 0, -1):  # Loop from the end to the start
        for j in range(i):  # Loop through the list up to the current iteration
            if unordered_list[j] > unordered_list[j + 1]:  # Compare adjacent elements
                temp = unordered_list[j]  # Swap if the current element is greater
                unordered_list[j] = unordered_list[j + 1]
                unordered_list[j + 1] = temp
# ```
# - **Complexity**: 
#   - Outer loop: O(n)
#   - Inner loop: O(n)
#   - Overall: O(n^2) in the worst and average cases.
# - **Use Case**: Bubble sort is a simple sorting algorithm suitable for small datasets or educational purposes.

#### Sorting Lists

my_list = [4, 3, 2, 1]
bubble_sort(my_list)
print(my_list)  # Output: [1, 2, 3, 4]

my_list = [1, 12, 3, 4]
bubble_sort(my_list)
print(my_list)  # Output: [1, 3, 4, 12]
# ```
# - **Complexity**: O(n^2) for each call to `bubble_sort`.

### Visual Representation of Bubble Sort

# # Let's visualize how bubble sort works on the list `[4, 3, 2, 1]`:

# 1. **Initial List**: `[4, 3, 2, 1]`
# 2. **First Pass**:
#    - Compare 4 and 3, swap: `[3, 4, 2, 1]`
#    - Compare 4 and 2, swap: `[3, 2, 4, 1]`
#    - Compare 4 and 1, swap: `[3, 2, 1, 4]`
# 3. **Second Pass**:
#    - Compare 3 and 2, swap: `[2, 3, 1, 4]`
#    - Compare 3 and 1, swap: `[2, 1, 3, 4]`
# 4. **Third Pass**:
#    - Compare 2 and 1, swap: `[1, 2, 3, 4]`
# 5. **Sorted List**: `[1, 2, 3, 4]`

# Here's a visual representation of the sorting process:

# ```plaintext
# Initial: [4, 3, 2, 1]
# Pass 1:  [3, 4, 2, 1]
#          [3, 2, 4, 1]
#          [3, 2, 1, 4]
# Pass 2:  [2, 3, 1, 4]
#          [2, 1, 3, 4]
# Pass 3:  [1, 2, 3, 4]
# ```

# Feel free to ask if you need any further assistance!